# 🔍 TECHNICAL OUTLINE: VM01-B AMNESIC BITNET
## HITL Analysis: Version B (Alpine + Bonsai 8B)
## Date: May 14, 2026

### **1. Executive Premise**
- **Objective**: Deploy a 1-bit 8-billion parameter agent on an 8GB P4000 without sacrificing intelligence for VRAM.
- **Substrate**: Alpine Linux (Diskless/RAM-only) for absolute amnesic properties.
- **Model**: PrismML Bonsai 8B (Native 1-bit) via QVAC Fabric (Vulkan).

### **2. Exploit Anatomy (Substrate Breakdown)**
- **Stage 1: The Host Layer (Alpine Linux)**:
    - **Mechanism**: `sysctl` to disable IPv6 SLAAC leakage. 
    - **Optimization**: `limits.conf` hard-tuning to allow the non-root KVM user to lock the Guest RAM + 40MB buffer (preventing VFIO_MAP_DMA errors).
- **Stage 2: The Inference Engine (QVAC Fabric)**:
    - **Mechanism**: Vulkan compute backend. Bypasses the need for modern CUDA Compute Capability.
    - **Performance**: 1.15 GB VRAM footprint. Lossless 1-bit ternary logic preservation.
- **Stage 3: The Agentic Orchestrator (OpenCode)**:
    - **Mechanism**: `OPENCODE_DISABLE_AUTOUPDATE=true` + `--pure` flag for absolute air-gapped isolation.
    - **Connectivity**: Tor-transparent proxy routing with `mcp_timeout: "never"` to handle 60s+ latency spikes.

### **3. Execution Proofs**
- **Visual Evidence**:
    - Headless `xvfb` virtual framebuffer running the OpenCode TUI in memory.
    - `autocutsel` bridge for clipboard-to-context data transfers.
- **Forensic Verification**:
    - The "Amnesic" reboot test. Zero data persistent in the `tmpfs` root after power loss.

### **4. Hardware/OPSEC Audit**
- **VRAM Delta**: 1.15 GB (Model) + 150 MB (Host OS) = 1.3 GB Total. ~84% VRAM available for context expansion.
- **Anonymity**: Mandatory Tor stream isolation. Zero IP leakage verified via bridge-level IPv6 disabling.
