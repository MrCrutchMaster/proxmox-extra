VM Create
---------------------------------------------------

Tested on proxmox 8.0.4 on HUANANZHI X99 F8 + Xeon E5 2680 V4

1. Download TCRP (https://github.com/pocopico/tinycore-redpill/releases)

```
curl --location https://github.com/pocopico/tinycore-redpill/releases/download/v0.10.0.0/tinycore-redpill.v0.10.0.0.img.gz --output /var/lib/vz/template/iso/tinycore-redpill.v0.10.0.0.img.gz
gzip --decompress /var/lib/vz/template/iso/tinycore-redpill.v0.10.0.0.img.gz
```

2. Create VM

```
# set vm id
id=100

# create disk for sata0
pvesm alloc local-zfs ${id} vm-${id}-disk-0 25G

# create vm
qm create ${id} \
  --args "-drive 'if=none,id=synoboot,format=raw,file=/var/lib/vz/template/iso/tinycore-redpill.v0.10.0.0.img' -device 'qemu-xhci,addr=0x18' -device 'usb-storage,drive=synoboot,bootindex=1'" \
  --cores 2 \
  --cpu host \
  --machine q35 \
  --memory 4096 \
  --name DSM7 \
  --tags 7.2,TCRP \
  --net0 virtio,bridge=vmbr0 \
  --numa 0 \
  --onboot 0 \
  --ostype l26 \
  --scsihw virtio-scsi-pci \
  --sata0 local-zfs:vm-${id}-disk-0,discard=on,size=25G,ssd=1 \
  --sockets 1 \
  --tablet 1

# if you want to autostart VM
qm set ${id} --onboot 1 
```

3. Passthrough disks/controllers

see manual in dir above

XPenology install 
---------------------------------------------------

1. Configure loader

```
ssh tc@<IP>
pass: P@ssw0rd

./rploader.sh update now
./rploader.sh fullupgrade now
./rploader.sh satamap now
./rploader.sh identifyusb now
./rploader.sh serialgen DS918+
./rploader.sh backup
./rploader.sh build ds918p-7.2.0-64570 withfriend
sudo reboot
```

2. Install Synology

- Wait a few minutes
- Go to VM ip address and install DSM_DS918+7.2.0-64570.pat file
- Reboot
- Load `Tiny Core With Friend`
- Wait a few minutes
- Go to VM ip address configure it, disable updates
- Go to NAS "Control Panel" > "Updates and Restore" and make manual update with UPD_DS918+7.2.0-64570-2.pat & UPD_DS918+7.2.0-64570-3.pat




