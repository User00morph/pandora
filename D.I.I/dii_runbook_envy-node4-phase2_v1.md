# D.I.I — NODE 4 PHASE 2 RUNBOOK
## Copy-paste runbook — always-on conversion

**Created 2026-09-21.** Companion to `dii_SOP_envy-node4-build_v1.md`.
Phase 1 is CLOSED: wiped, Ubuntu 26.04.1 installed, LUKS on.

**Node facts (verified 2026-09-21):**
| Fact | Value |
|---|---|
| Envy IP | `192.168.5.64` (**moved from .63 — DHCP churn; Tailscale fixes this in Block 2**) |
| MacBook IP | `192.168.4.39` |
| Username | `morph` |
| LAN | `192.168.4.0/22` (**/22, not /24** — range is 192.168.4.0–192.168.7.255) |
| SSH | OpenSSH 10.2p1, installed + running |

> **Paste in Ubuntu terminal is `Ctrl+Shift+V`,** not `Ctrl+V`.

---

## BLOCK 1 — SSH KEY (do this first)

Gives the MacBook keyless access so the rest of Phase 2 runs remotely.

```bash
mkdir -p ~/.ssh && chmod 700 ~/.ssh
echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIChAomf6x5JOxIoyMGpr0IrCHxH2gEe/FbrpOw13DgXs' >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
cat ~/.ssh/authorized_keys
```

Expect exactly one line starting `ssh-ed25519 AAAAC3Nza`.
**Stop here and tell Claude.** Everything below can then run from the MacBook.

---

## BLOCK 0 — RECON ✅ COMPLETE 2026-09-21

Run by Claude over SSH. **Results — do not re-run:**

| Fact | Verified value |
|---|---|
| Hostname | `morph-HP-Envy-x360-2-in-1-Laptop-15-fe0xxx` |
| OS | Ubuntu 26.04.1 LTS, kernel `7.0.0-31-generic` |
| **LUKS device** | **`/dev/nvme0n1p3`** |
| LUKS UUID | `a9531f34-112d-40c5-8c2b-4b733c1762f2` |
| Layout | **LUKS → LVM → ext4** — the SOP never accounted for the LVM layer |
| Free space | 429G, 3% used |
| crypttab | `dm_crypt-0 UUID=a9531f34-... none luks` |
| TPM | `/dev/tpm0` + **`/dev/tpmrm0`** — resource manager present ✅ |
| BIOS / Gate 3 | **PENDING** — see Block 1.5 |

Enrollment targets **`p3`** — the LUKS container, **not** the LVM volume above it.

---

## HOW THIS RUNS — division of labour

Claude drives the node over SSH but **cannot answer a `sudo` password prompt**
(the session is non-interactive). Rather than granting permanent passwordless root,
the split is:

- **Claude runs** every unprivileged command — reads, checks, verification, diagnosis.
- **Morph pastes** the privileged blocks below. Each is self-contained and ends by
  printing what Claude needs to see next.

This keeps least-permissions intact. **No NOPASSWD sudoers file is created.**

---

## BLOCK 1.5 — GATE 3 READING (paste on the Envy)

```bash
sudo dmidecode -s bios-version
```

`F.08` → the BIOS update never ran. **Deferred ticket, NOT a blocker.** Do not stall Phase 2.

---

## BLOCK 0 (original recon — superseded, kept for reference)


```bash
sudo apt install -y tpm2-tools
{ echo "=== BIOS ==="        ; sudo dmidecode -s bios-version
  echo "=== LSBLK ==="       ; lsblk -f
  echo "=== TPM DEVICES ===" ; ls -l /dev/tpm*
  echo "=== CRYPTTAB ==="    ; cat /etc/crypttab
  echo "=== SECUREBOOT ===" ; sudo mokutil --sb-state
  echo "=== OS ==="          ; lsb_release -d; uname -r
} 2>&1 | tee ~/block0.txt
```

What each answers:
- **BIOS** — `F.08` means Gate 3 never ran. Deferred ticket, **not** a blocker.
- **LSBLK** — find the row with FSTYPE `crypto_LUKS`. That device goes in Block 3. **Never assume `p3`.**
- **CRYPTTAB** — the existing mapping line we amend.
- **SECUREBOOT** — context for the PCR 7 binding.

---

## BLOCK 2 — BASE PACKAGES + NETWORK

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y unattended-upgrades curl
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

`tailscale up` prints a URL — open it, authenticate, join the tailnet.

---

## BLOCK 3 — TPM-BOUND LUKS  🔴 THE GATE

**Two defects existed in the old SOP. Both fixed here:**
1. `--tpm2-pld=7` is not a flag. It is `--tpm2-pcrs=`.
2. Enrollment alone is a **silent no-op** — nothing told initramfs to ask the TPM,
   so the node would still prompt for a passphrase on every boot.

### 🔴 WRITE THE LUKS PASSPHRASE DOWN ON PAPER BEFORE RUNNING THIS.
PCR 7 changes on any BIOS update, Secure Boot toggle, or TPM clear.
The passphrase is the only way back into the disk.

Replace `/dev/nvme0n1p3` with the real `crypto_LUKS` device from Block 0.

```bash
sudo systemd-cryptenroll --tpm2-device=auto --tpm2-pcrs=7 /dev/nvme0n1p3
```

Then add `tpm2-device=auto` to the options column in `/etc/crypttab`.
**Exact change on this machine** — the options field is currently just `luks`:
```
BEFORE: dm_crypt-0 UUID=a9531f34-112d-40c5-8c2b-4b733c1762f2 none luks
AFTER:  dm_crypt-0 UUID=a9531f34-112d-40c5-8c2b-4b733c1762f2 none luks,tpm2-device=auto
```
Then rebuild:

```bash
sudo update-initramfs -u -k all
```

### Proof condition
**Reboot and do not touch the keyboard.** The gate closes only when the machine
returns to a login prompt unattended. A zero exit code proves nothing.

### Fallback — Clevis (expect to need this on Ubuntu)
Ubuntu's `cryptsetup-initramfs` has historically ignored `tpm2-device=auto`.

```bash
sudo apt install -y clevis clevis-luks clevis-initramfs
sudo clevis luks bind -d /dev/nvme0n1p3 tpm2 '{"pcr_bank":"sha256","pcr_ids":"7"}'
sudo update-initramfs -u -k all
```

---

## BLOCK 4 — ALWAYS-ON CONVERSION

Run only after Block 3's reboot test passes.

```bash
sudo systemctl set-default multi-user.target
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
```

Lid must not suspend — edit `/etc/systemd/logind.conf`:
```
HandleLidSwitch=ignore
HandleLidSwitchExternalPower=ignore
HandleLidSwitchDocked=ignore
```
```bash
sudo systemctl restart systemd-logind
```

GUI on demand: `sudo systemctl isolate graphical.target`
Back to console: `sudo systemctl isolate multi-user.target`

---

## BLOCK 5 — DOCKER

```bash
sudo apt install -y docker.io docker-compose-v2
sudo usermod -aG docker $USER
```
Log out and back in for group membership to take effect.

---

## PHASE 2 COMPLETION CRITERIA

- [ ] Boots unattended to console, no passphrase prompt
- [ ] SSH reachable over Tailscale **with the lid closed**
- [ ] Wi-Fi (AX211) confirmed working
- [ ] `systemctl isolate graphical.target` brings the desktop back
- [ ] Survives a full power-cycle without human hands

---

*D.I.I | Node 4 | Volume tier 7–8B — NOT the brain. Synthesis belongs to the Oracle.*
