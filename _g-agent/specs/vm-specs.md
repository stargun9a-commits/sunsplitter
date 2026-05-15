# VM SPECIFICATIONS (VOID-DRONE SOVEREIGN WORKSTATION)
## Session Snapshot: 2026-04-26

These specifications represent the "Golden Image" configuration for the VOID-DRONE forensic workstation. They ensure high-performance NVIDIA acceleration and hardware anonymity.

### 🖥️ VOID-DRONE Architecture
| Component | Setting | Purpose |
|---|---|---|
| **Guest OS** | `Debian 12 Minimal (X11)` | Deterministic OS with stable X11 for qxl/spice. |
| **Graphics (Dual-Block)** | `qxl` + `spice-vdagent` | Perfect clipboard/drag-and-drop stability on X11. |
| **Display Mode** | `100% Native (1:1)` | Prevents high-res lag and geometry crashes. |
| **Host Scaling Fix** | `Additional Scale: 0%` | Ensures logical resolution parity. |
| **Shared Bridge** | `virtiofs (void_drone_hub)` | Bidirectional forensic data pipe. |
| **Identity** | `System76 (Spoofed SMBIOS)` | Anonymity and hardware masking. |
| **CPU Pinning** | `8 vCPUs (Host-Passthrough)` | Scaled for optimal local simulation. |
| **Memory** | `16 GiB (Static)` | Scaled for local simulation stability. |

### 🛠️ Hardware Bridges
- **GPU**: NVIDIA Quadro P4000 (via EGL-Headless)
- **Filesystem**: `virtiofs` mounted as `/home/conrad/void_drone_hub`
- **Network**: Isolated bridge with randomized MAC.

---
**Protocol:** Reference these specs when generating VM-side hardening scripts or data extraction payloads.
