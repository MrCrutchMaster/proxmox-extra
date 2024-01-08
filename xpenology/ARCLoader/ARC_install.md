VM Create
---------------------------------------------------

Tested on Proxmox 8.0.4 + Huananzhi X99-F8 + Xeon E5 2680 V4

Tested on Proxmox 8.1.3 + Huananzhi X99-F8D Plus + 2*Xeon E5 2680 V4

1. Download ARCLoader (https://github.com/AuxXxilium/arc/releases)

```
apt install unzip
curl --location https://github.com/AuxXxilium/arc/releases/download/23.11.18/arc-23.11.18.img.zip --output /var/lib/vz/template/iso/arc-23.11.18.img.zip
unzip -p /var/lib/vz/template/iso/arc-23.11.18.img.zip > /var/lib/vz/template/iso/arc-23.11.182.img
rm /var/lib/vz/template/iso/arc-23.11.18.img.zip
```

2. Create VM

```
# set vm id
id=101

# create disk for sata1
pvesm alloc local-zfs ${id} vm-${id}-disk-1 25G

# create vm
qm create ${id} \
  --cores 2 \
  --cpu host \
  --machine q35 \
  --memory 4096 \
  --name DSM7 \
  --tags 7.2,ARC \
  --net0 e1000,bridge=vmbr0 \
  --numa 0 \
  --onboot 0 \
  --ostype l26 \
  --scsihw virtio-scsi-pci \
  --sata1 local-zfs:vm-${id}-disk-1,discard=on,size=25G,ssd=1 \
  --sockets 1 \
  --tablet 1

# import loader as disk and make it bootable
qm importdisk ${id} /var/lib/vz/template/iso/arc-23.11.18.img local-zfs
qm set ${id} --sata0 local-zfs:vm-${id}-disk-0
qm set ${id} --boot order='sata0'

# if you want to autostart VM
qm set ${id} --onboot 1 
```

3. Passthrough disks/controllers

see [manual](https://github.com/MrCrutchMaster/different/blob/main/xpenology_proxmox/disk_passthrough.md)

XPenology install 
---------------------------------------------------

1. Configure loader

```
Choose Model:
  DS1520+
Choose version:
  7.2
Arc Patch Model:
  1 Yes
Mac Settings:
  select first
Macsys Settings
  2 Yes
DSM Extensions:
  amepatch
  cpuinfo
  reboot
Build now?
  1 Yes
Arc Build
  OK
Boot Now?
  1 Yes
```

2. Install Synology

- Wait a few minutes
- Go to VM ip address and install DSM_DS1520+7.2.1-69057..pat file
- Reboot
- Wait a few minutes
- Go to VM ip address configure it, disable updates
