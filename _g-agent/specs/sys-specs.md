# SYSTEM SPECIFICATIONS (SOVEREIGN INFRASTRUCTURE)
## Session Snapshot: 2026-04-26

This document serves as the ground-truth hardware and OS constraint sheet for all agentic engineering and "Wire-In" builds. All generated engineering prompts must ingest these specs to ensure binary compatibility and resource optimization.

### 🖥️ Machine Spec Sheet
| Component | Spec | Planning Relevance |
|---|---|---|
| **Host OS** | `Pop!_OS 24.04 LTS` | Stable Linux base for ML tooling. |
| **Kernel** | `Linux 6.18.7-76061807-generic` | Modern kernel with current NVIDIA driver support. |
| **Motherboard** | `ASUS PRIME X570-P` | AM4 desktop platform. |
| **CPU** | `AMD Ryzen 9 3900X` | `12` cores / `24` threads, boost up to `4.67 GHz`. |
| **RAM** | `125 GiB` total | Large memory headroom for feature engineering and parallel jobs. |
| **Swap** | `19 GiB` | Safety margin. |
| **GPU** | `NVIDIA Quadro P4000` | Pascal Architecture, 1792 CUDA Cores. |
| **VRAM** | `8 GB GDDR5` | 243 GB/s Bandwidth, 256-bit Interface. |
| **Compute** | `5.3 TFLOPS` | Peak Single Precision FP32 Performance. |
| **I/O & Display** | `4x DP 1.4` | Up to 4x 5K (5120x2880) @ 60Hz. |
| **NVIDIA Driver** | `580.126.18` | Current installed host driver. |
| **CUDA** | `13.0` | CUDA-capable stack present on host. |
| **Root Filesystem** | `ext4` on `CT500P1SSD8 NVMe` | Fast primary workspace disk. |
| **Root Capacity** | `449 GiB` mounted | `~321 GiB` free local room. |
| **Python** | `Python 3.13.12` | Very new interpreter; env pinning recommended. |
| **Git** | `2.43.0` | Tooling baseline confirmed. |

### 🔬 Planning Constraints & Advantages
*   **VRAM Bottleneck & Mitigation**: `8 GiB` VRAM is the primary constraint for large ML workflows. 
    *   **Primary Topology**: Local quantized execution is the default target for most workflows. 
    *   **Offload Fallbacks**: When hardware constraints strictly prohibit local execution (e.g., massive models), the Agent should consider these hybrid compute fallbacks:
        *   **Microsoft Foundry Local**: (Q-bit compatible architecture) `https://github.com/microsoft/Foundry-Local.git`
        *   **Kaggle Run Extension**: `https://marketplace.visualstudio.com/items?itemName=DataQuanta.vscode-kaggle-run`
        *   **Google Colab Extension**: `https://marketplace.visualstudio.com/items?itemName=Google.colab`
*   **Memory Advantage**: `125 GiB` system RAM is excellent for large-scale preprocessing, backtesting, and multi-process data pipelines.
*   **Storage Strategy**: Hot data/environments on NVMe root; datasets/cache on Samsung 2TB SSD; cold archives on 3.6T HDD.
