# D.I.I — NODE 4 PHASE 2 RUNBOOK
## Copy-paste runbook — always-on conversion

**Created 2026-09-21.** Companion to `dii_SOP_envy-node4-build_v1.md`.
Phase 1 is CLOSED: wiped, Ubuntu 26.04.1 installed, LUKS on.

**Node facts (verified 2026-09-21):**
| Fact | Value |
|---|---|
| Envy IP (LAN) | `192.168.5.64` — **do not rely on this, it moved .63→.64 in one session** |
| **Tailnet IP** | **`100.64.176.25`** — permanent, survives DHCP ✅ |
| MagicDNS | `morph-hp-envy-x360-2-in-1-laptop-15-fe0xxx.tail2c389a.ts.net` |
| Tailnet | `tail2c389a.ts.net`, owner `emoefe1838@` |
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
| BIOS / Gate 3 | **`F.08` — CONFIRMED 2026-09-21. The update never ran.** Deferred ticket, NOT a blocker. ⚠️ If ever flashed later it changes PCR 7 and breaks TPM unlock → re-enrollment required. |

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

## BLOCK 1.5 — GATE 3 READING ✅ COMPLETE — result: `F.08`

The BIOS update never ran before the wipe. Windows is gone, so HP Support Assistant
is no longer an option. **This is now a deferred ticket, not a blocker** — the gain was
Raptor Lake-U microcode and power-management tuning, which matters only if the node
shows instability under sustained inference load.

Revisit only if Phase 3 benchmarking shows thermal or power anomalies.

**⚠️ Coupling to remember:** flashing the BIOS later changes PCR 7, which breaks
TPM-bound LUKS unlock and forces re-enrollment. Keep the passphrase on paper.

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

## BLOCK 2 — BASE PACKAGES + NETWORK  ← YOU ARE HERE

**State verified 2026-09-21 over SSH:** 34 pending updates. `curl`, `tailscale`,
`docker` all ABSENT. `git` present. Default target still `graphical.target`.

**Order matters** — the Tailscale installer is a shell script fetched *with* curl,
so curl must exist first. The original block had these reversed.

### 2a — updates + curl (the long one, 34 packages)
```bash
sudo apt update && sudo apt upgrade -y && sudo apt install -y curl unattended-upgrades
```

Let it fully finish before 2b.

### 2b — Tailscale
```bash
curl -fsSL https://tailscale.com/install.sh | sh && sudo tailscale up
```

`tailscale up` prints a URL. Open it in the Envy's browser and authenticate.
This gives the node a **permanent address** — the LAN IP already moved
`.63 → .64` in a single session, which is why no other machine should ever
address this node by DHCP IP.

### ⚠️ Before you start
- **The upgrade may pull a new kernel → reboot required.**
  TPM unlock is NOT configured yet, so the node **will stop and demand the LUKS
  passphrase**. Have it in hand. You are sitting at the machine, so this is fine.
- **Do NOT reboot this node remotely until Block 3 passes.** It cannot come back
  without a human. That gap is exactly what Block 3 closes.

### Report back
```bash
tailscale ip -4
```

---

## BLOCK 3 — TPM-BOUND LUKS  🔴 THE GATE

**Two defects existed in the old SOP. Both fixed here:**
1. `--tpm2-pld=7` is not a flag. It is `--tpm2-pcrs=`.
2. Enrollment alone is a **silent no-op** — nothing told initramfs to ask the TPM,
   so the node would still prompt for a passphrase on every boot.

### 🔴 STEP ZERO — VERIFY THE PASSPHRASE, THEN WRITE IT ON PAPER

The SOP said "keep the passphrase." That is advice you can follow and still be wrong,
because it never said to **prove** the passphrase you remember is the one in the header.
Test it non-destructively first — this unlocks and modifies nothing:

```bash
sudo cryptsetup luksOpen --test-passphrase /dev/nvme0n1p3 && echo "PASSPHRASE OK"
```

Also confirm which keyslots exist. TPM enrollment **adds** a slot, it does not replace
yours — verifying your slot survives is what makes the fallback real rather than assumed:

```bash
sudo cryptsetup luksDump /dev/nvme0n1p3 | grep -E "^Keyslot|^Version|^Cipher|Tokens"
```

**Do this BEFORE enrollment, not after.** Today a lost passphrase costs an afternoon —
the disk is days old and nearly empty. After TPM binding it costs the entire inference
tier the moment firmware state shifts. And with Gate 3 deferred, a firmware change is
already on the backlog.

### 🔴 THEN WRITE IT ON PAPER — not in a manager on this machine.
PCR 7 changes on any BIOS update, Secure Boot toggle, or TPM clear.
The passphrase is the only way back into the disk.

Replace `/dev/nvme0n1p3` with the real `crypto_LUKS` device from Block 0.

✅ Passphrase verified against the header 2026-09-21.

### 3a — enroll the TPM
Prompts for your **existing LUKS passphrase**. Adds a new keyslot; yours stays.
```bash
sudo systemd-cryptenroll --tpm2-device=auto --tpm2-pcrs=7 /dev/nvme0n1p3
```

### 3b — confirm a TPM token now exists
```bash
sudo cryptsetup luksDump /dev/nvme0n1p3 | grep -A3 Tokens
```
Expect a `systemd-tpm2` token. **If nothing appears, STOP** — 3c onward is pointless.

Then add `tpm2-device=auto` to the options column in `/etc/crypttab`.
**Exact change on this machine** — the options field is currently just `luks`:
```
BEFORE: dm_crypt-0 UUID=a9531f34-112d-40c5-8c2b-4b733c1762f2 none luks
AFTER:  dm_crypt-0 UUID=a9531f34-112d-40c5-8c2b-4b733c1762f2 none luks,tpm2-device=auto
```
### 3c — patch crypttab (exact command for this machine)
```bash
sudo sed -i 's|none luks$|none luks,tpm2-device=auto|' /etc/crypttab && cat /etc/crypttab
```
Must print: `dm_crypt-0 UUID=a9531f34-... none luks,tpm2-device=auto`

### 3d — rebuild the initramfs
```bash
sudo update-initramfs -u -k all
```

### 3e — REBOOT, HANDS OFF THE KEYBOARD
```bash
sudo reboot
```
**Be physically at the machine.** Watch what happens at the encryption prompt.

- **Comes back on its own → GATE CLOSED.** ✅
- **Asks for the passphrase → not a failure.** Type it, log in, go to the Clevis fallback.
  Ubuntu's initramfs ignoring `tpm2-device=auto` is the *expected* outcome, not a fault.

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
