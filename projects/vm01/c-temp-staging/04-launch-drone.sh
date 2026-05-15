#!/bin/bash
# 🛸 VOID-DRONE: MASTER WIRE-IN SCRIPT (V2)
# Target: Alpine Linux 3.19.9 (Extended)
# Hardware: NVIDIA Quadro P4000 (PCI 09:00.0)

ISO_PATH="../data/alpine-extended-3.19.9-x86_64.iso"
DISK_PATH="../data/void-drone.qcow2"
VRAM="8G"

# Ensure we are running as root
if [[ $EUID -ne 0 ]]; then
   echo "CRITICAL: This script requires root privileges for VFIO passthrough."
   echo "Run with: sudo ./launch-drone.sh"
   exit 1
fi

# Create the disk image if missing
if [ ! -f "$DISK_PATH" ]; then
    echo ">>> Initializing 40GB amnesic disk image..."
    qemu-img create -f qcow2 "$DISK_PATH" 40G
fi

echo ">>> Hijacking Quadro P4000 [09:00.0] and [09:00.1]..."

# Note: kvm=off and hv_vendor_id=null are critical to hide the hypervisor from NVIDIA drivers
qemu-system-x86_64 \
  -enable-kvm \
  -m $VRAM \
  -cpu host,kvm=off,hv_vendor_id=null \
  -smp 4,sockets=1,cores=4,threads=1 \
  -drive file="$DISK_PATH",format=qcow2,if=virtio \
  -cdrom "$ISO_PATH" \
  -net nic,model=virtio -net user \
  -vga none \
  -display none \
  -device vfio-pci,host=09:00.0,multifunction=on \
  -device vfio-pci,host=09:00.1 \
  -boot d
