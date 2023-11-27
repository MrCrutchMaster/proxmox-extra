SATA controller passthrough
---------------------------------------------------

Best variant


enable in grub
```
nano /etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on pcie_acs_override=downstream,multifunction"
update-grub
```

enable in kernel
``` 
nano /etc/kernel/cmdline
intel_iommu=on
proxmox-boot-tool refresh
```
reboot machine

HDD passthrough
---------------------------------------------------

Not all hdd functions will be supported
```
100 - VMID 
wwn-0x50023031000e1956 - disk id from ls -l /dev/disk/by-id/
```

`qm set 100 -scsi1 /dev/disk/by-id/ata-PLEXTOR_PX-128M5Pro_P02346116262`

HDD Spindown
---------------------------------------------------
For HDD passthrough case

Since the Synology VM can't control your hardware because of Proxmox, Proxmox must spin down your harddrives when idle for x time.
You can do this with "hdparm".

1. Install hdparm 
```
apt-get install update
apt-get install hdparm
```

2. Now configure the idle time for spin down (this goes for each drive)
```
hdparm -S 120 /dev/sdb
hdparm -S 120 /dev/sdc
```
-S means standby and 120 means 10 minutes


