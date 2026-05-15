# THE GHOST-MATRIX FORENSIC BIBLE (V10)
## Master Reference for Sovereign VM Construction
## Date: 04-28-2026

### 🛡️ PILLAR I: DIGITAL EXORCISM (THE ISOLATION)
**Finding**: Standard CPython initialization triggers an upward landmark traversal. If any VirtioFS bridge contains `pyvenv.cfg` or `lib/python3.x`, the interpreter "hijacks" that prefix, leading to "Parasitic Prefixing."

**The Protocol**:
1. **Physical Binary Anchor**: Find the absolute path of the Python binary (`readlink -f`).
2. **The ._pth Kill-Switch**: Create `python3._pth` next to the physical binary.
3. **Configuration**:
   ```text
   ../lib/python3.12
   ../lib/python3.12/lib-dynload
   site-packages
   import site
   ```
4. **Result**: The interpreter becomes "path-blind" to the host.

### 🔗 PILLAR II: DETERMINISTIC ABI LINKING (THE SOVEREIGN BUNDLE)
**Finding**: Relying on `LD_LIBRARY_PATH` or system loaders leads to ABI drift when bridging between host/guest substrates.

**The Protocol**:
1. **Vendoring**: Copy all headers and `.so` files into `SovereignHub/include` and `SovereignHub/lib`.
2. **RPATH Injection**: During `pip install` or `make`, use:
   `LDFLAGS="-Wl,-rpath='\$ORIGIN/../../lib' -Wl,--disable-new-dtags"`
3. **Verification**: `readelf -d [ext.so] | grep RPATH` must show the relative `$ORIGIN` path.
4. **Result**: The bundle is portable and substrate-independent.

### 🌉 PILLAR III: VIRTIOFS PERMISSION MASKING (THE BRIDGE)
**Finding**: SELinux "Silent Masking" hides inodes in VirtioFS mounts if the security context is missing.

**The Protocol**:
1. **Mount Command**: 
   `sudo mount -t virtiofs [TAG] /mnt/path -o context="system_u:object_r:virt_content_t:s0"`
2. **Verification**: `ls -Z /mnt/path` should show the `virt_content_t` label.

### 🏗️ PILLAR IV: GLIBC COMPATIBILITY (THE WIRE-IN)
**Finding**: Compilation fails on modern kernels due to `pthread_yield` removal.

**The Protocol**:
1. **Source Patching**: Replace all instances of `pthread_yield()` with `sched_yield()`.
2. **Header Inclusion**: Ensure `<sched.h>` is included in the source.

---
### 🖥️ PILLAR V: INFRASTRUCTURE & DISPLAY STABILIZATION
**Finding**: Forensic work is hindered by erratic display scaling and VirtioFS attribute loss.

**The Protocol**:
1. **XML Config**: Use `qxl` video driver and `virtio-serial` for Spice.
2. **VirtioFS Access**: Use `accessmode='passthrough'` for the bridge to preserve uid/gid mappings.
3. **Guest Agent**: Install and enable `spice-vdagent` inside the guest to allow resolution auto-scaling.

### 🕸️ PILLAR VI: THE SYMLINK DEREFERENCING TRAP
**Finding**: The "Ghost" can survive if the `._pth` file is placed next to a symlink (e.g., `/usr/bin/python3`). Python dereferences the link *before* looking for the configuration file.

**The Protocol**:
1. **Discovery**: `REAL_BIN=$(readlink -f /usr/bin/python3)`
2. **Placement**: Place `python3.x._pth` in the same directory as `$REAL_BIN`.
3. **Verification**: `python3 -S -c "import sys; print(sys.path)"` should show **zero** external directories.

---
**FINAL SUMMARY FOR THE NEW BUILD**:
1. Start with **Debian 12** or **Ubuntu 24.04**.
2. Deploy **Standalone Python** via `python-build-standalone`.
3. Apply **._pth isolation** to the **Physical Binary**.
4. Configure **Triple-Bridge VirtioFS** with `passthrough` and `SELinux context`.
5. Enable **Spice VDAgent** for display stability.
