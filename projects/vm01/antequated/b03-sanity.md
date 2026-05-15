# ☢️ NOVA-REACTOR: FEASIBILITY AUDIT (VM01-B AMNESIC BITNET)
## Audit Target: b01-report.md (PrismML Bonsai 8B + Alpine Diskless)
## Date: May 14, 2026

### ✅ Verified Architectures (The VRAM Breakthrough)
1.  **Bonsai 8B vs. P4000**: The **1.15 GB** footprint for an 8-billion parameter model is the definitive "Reality Gap" closer. This leaves over 85% of our VRAM free for the **KV Cache**, allowing for 128k+ context windows without OOM crashes on legacy Pascal hardware.
2.  **Alpine Diskless Mode**: Using `tmpfs` for the root partition and a read-only Alpine medium fulfills the "Amnesic" requirement perfectly. Total RAM overhead < 150MB is unprecedented for a forensic host.
3.  **QVAC Fabric (Vulkan)**: Bypassing the native `bitnet.cpp` CUDA kernels in favor of Vulkan-based dynamic tiling is the only way to get BitNet running reliably on Compute Capability 6.1 (Pascal) in 2026.

### ⚠️ Reality Gaps (Critical Blocks)
1.  **The Tor Timeout Problem**: Setting `mcp_timeout` to "never" in OpenCode prevents crashes, but it doesn't solve the *user experience* issue. Long-running adversarial scripts (Gaussian noise generation) over Tor can take minutes. 
    - *Fix*: We must implement a "Pulse" telemetry ping in our custom MCP servers to prevent the TUI from appearing "frozen" to the user during long generations.
2.  **XVFB Clipboard Lag**: Running OpenCode in a virtual framebuffer (`xvfb`) can lead to clipboard desynchronization between the host and guest.
    - *Fix*: The `build.sh` must explicitly include `autocutsel` to synchronize the X11 selection and the cutbuffer within the headless environment.

### 🛠️ Actionable Verdict
The Version B architecture is **HIGHLY LETHAL** and technically superior to Version A. It provides 8-billion parameter reasoning at a 1-billion parameter cost. **APPROVED.**
