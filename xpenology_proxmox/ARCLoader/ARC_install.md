VM Create
---------------------------------------------------

Tested on proxmox 8.0.4

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
id=104

# create vm
qm create ${id} \
  --cores 2 \
  --cpu host \
  --machine q35 \
  --memory 4096 \
  --name DSM7 \
  --net0 e1000,bridge=vmbr0 \
  --numa 0 \
  --onboot 0 \
  --ostype l26 \
  --scsihw virtio-scsi-pci \
  --sata1 local-zfs:vm-${id}-disk-0,discard=on,size=25G,ssd=1 \
  --sockets 1 \
  --tablet 1

qm importdisk ${id} /var/lib/vz/template/iso/arc-23.11.18.img local-zfs
qm set ${id} --sata0 local-zfs:vm-${id}-disk-0
qm set ${id} --boot order='sata0'
```

3. Passthrough disks/controllers

see manual in dir above

XPenology install 
---------------------------------------------------

```
CHoose model:
  DS1520
Choose version:
  7.2
Patch:
  AME
  reboot
Build now?
  Yes
```