# D.I.I — NODE 4 BOOT RECOVERY
## initramfs missing cryptsetup — repair from live USB

**2026-09-21.** Node 4 will not boot. Drops to `(initramfs)` BusyBox shell.
**Data is intact.** This is a broken boot image, not a broken disk.

---

## WHAT HAPPENED

```
(initramfs) cryptsetup open /dev/nvme0n1p3 dm_crypt-0
sh: cryptsetup: not found
ALERT! /dev/mapper/ubuntu--vg-ubuntu--lv does not exist. Dropping to a shell!
```

Ubuntu's `cryptsetup-initramfs` hook parses `/etc/crypttab` when building the image.
It hit `tpm2-device=auto`, did not recognize it, and **bailed out — producing an
initramfs with no unlock tooling at all.** No cryptsetup binary means no passphrase
prompt, no TPM attempt, nothing. Just a dead end.

**ROOT CAUSE: Ubuntu's initramfs does not support `tpm2-device=auto`.**
It does not ignore the option — it fails closed and strips the unlock tooling.
**Do not put that option in crypttab on Ubuntu. Use Clevis instead.**

**PROCESS FAILURE:** the rebuilt initramfs was never verified before rebooting.
One check would have caught it while the machine was still up:
```bash
lsinitramfs /boot/initrd.img-$(uname -r) | grep -c cryptsetup   # must be > 0
```
**This check is now mandatory before any reboot that follows an initramfs rebuild.**

---

## MACHINE FACTS

| | |
|---|---|
| LUKS device | `/dev/nvme0n1p3` |
| LUKS UUID | `a9531f34-112d-40c5-8c2b-4b733c1762f2` |
| Mapper name | `dm_crypt-0` |
| Root LV | `/dev/mapper/ubuntu--vg-ubuntu--lv` |
| /boot | `/dev/nvme0n1p2` |
| EFI | `/dev/nvme0n1p1` |

---

## RECOVERY

### 1 — Boot the Ubuntu USB
Insert the stick. Power on, tap **F9** at POST for the one-time boot menu.
Choose the USB. At the GRUB menu pick **Try Ubuntu** (NOT Install).

Open a terminal: `Ctrl`+`Alt`+`T`

### 2 — Confirm the disk looks as expected
```bash
lsblk -f
```
Expect `nvme0n1p3` as `crypto_LUKS`.

### 3 — Unlock the disk
```bash
sudo cryptsetup open /dev/nvme0n1p3 dm_crypt-0
```
Prompts for the LUKS passphrase. Nothing echoes while typing.

```bash
sudo vgchange -ay
```

### 4 — Mount everything
```bash
sudo mount /dev/mapper/ubuntu--vg-ubuntu--lv /mnt
sudo mount /dev/nvme0n1p2 /mnt/boot
sudo mount /dev/nvme0n1p1 /mnt/boot/efi
for d in dev dev/pts proc sys run; do sudo mount --bind /$d /mnt/$d; done
```

### 5 — Enter the installed system
```bash
sudo chroot /mnt
```

### 6 — Revert the crypttab option
```bash
sed -i 's|,tpm2-device=auto||' /etc/crypttab && cat /etc/crypttab
```
Must print: `dm_crypt-0 UUID=a9531f34-... none luks`  ← back to plain `luks`

### 7 — Rebuild the initramfs
```bash
update-initramfs -u -k all
```

### 8 — 🔴 VERIFY BEFORE REBOOTING — the step that was skipped last time
```bash
lsinitramfs /boot/initrd.img-$(ls /lib/modules | head -1) | grep -c cryptsetup
```
**Must return a number greater than 0.** If it returns `0`, STOP — do not reboot.
Rebooting on a `0` puts you right back at the `(initramfs)` prompt.

### 9 — Exit and reboot
```bash
exit
sudo umount -R /mnt
sudo reboot
```
Remove the USB stick as it restarts.

**Expect a passphrase prompt on this boot — that is correct.** We are back to
a plain LUKS setup. TPM unlock comes next, via Clevis.

---

## AFTER RECOVERY — the Clevis path

Clevis integrates with Ubuntu's initramfs properly rather than fighting it.

```bash
sudo apt install -y clevis clevis-luks clevis-initramfs
sudo clevis luks bind -d /dev/nvme0n1p3 tpm2 '{"pcr_bank":"sha256","pcr_ids":"7"}'
sudo update-initramfs -u -k all
lsinitramfs /boot/initrd.img-$(uname -r) | grep -c cryptsetup   # VERIFY > 0 FIRST
sudo reboot
```

Optional cleanup — remove the failed systemd-cryptenroll token in keyslot 1:
```bash
sudo systemd-cryptenroll --wipe-slot=tpm2 /dev/nvme0n1p3
```
Keyslot 0 (passphrase) must always remain.

---

*D.I.I | Node 4 | Recovery doc | Keyslot 0 passphrase is the fallback — always.*
