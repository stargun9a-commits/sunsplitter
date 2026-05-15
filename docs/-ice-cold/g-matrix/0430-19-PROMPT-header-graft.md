# SKY-CRANE RESEARCH PROMPT (V19): PYTHON-DEV HEADER GRAFT DEADLOCK

## 🎯 OBJECTIVE
Resolve the "Missing Header" deadlock for the Genesis Prime forensic sensor ignition. The goal is to provide a deterministic method for installing or extracting Python 3.11 development headers (`Python.h`, `pyconfig.h`) on a Pop!_OS 24.04 (Noble) host to graft them into a network-isolated VM running Python 3.11.

## 🛠️ INFRASTRUCTURE CONTEXT
- **HOST OS**: Pop!_OS 24.04 LTS (Noble)
- **HOST PYTHON**: 3.12.3 (Default)
- **GUEST OS**: Minimal forensic substrate (Debian-based)
- **GUEST PYTHON**: 3.11
- **NETWORK STATUS**: Total Guest Isolation. Host is under stateful DPI firewall.
- **BRIDGE**: Shared directory mounted at `/mnt/bridges/hub` in the guest.

## 🔍 RESEARCH REQUIREMENTS
Perform a deep technical analysis of the following:

### 1. The Noble-to-Bullseye Header Gap
- Identify the correct package name or repository (e.g., deadsnakes/ppa) to install `python3.11-dev` on Ubuntu 24.04 (Noble).
- If the package is deprecated in Noble, find a way to manually download the `.deb` for Python 3.11 headers from the Debian/Ubuntu archive.

### 2. Surgical Header Extraction
- Provide a command-line sequence to extract `Python.h` and the architecture-specific `pyconfig.h` from a `.deb` file without installing it, to facilitate a clean graft into the Hub.

### 3. PyBGPStream Cross-Version Compilation
- Verify if compiling `pybgpstream` extension against headers from a slightly different sub-version (e.g. 3.11.2 vs 3.11.9) poses binary compatibility risks within the forensic substrate.

### 4. Zero-Dependency PIP Bypass
- Confirm the definitive method for installing `setuptools` and its dependencies (like `wheel`) from raw source code within a network-blackout environment where `pip` is unavailable.

## 📜 ATTACHED CONTEXT
- [0430-roadmap.md](file:///home/conrad/workspace/PROJECTS/g-matrix/docs/staging/0430-roadmap.md): Current project status and sensor ignition phase.
- [Crafting a Sham Wandio Library.md](file:///home/conrad/workspace/PROJECTS/g-matrix/docs/staging/Crafting%20a%20Sham%20Wandio%20Library.md): Details on the build-time deception architecture.
- [0430-1904-report.md](file:///home/conrad/workspace/PROJECTS/g-matrix/docs/staging/0430-1904-report.md): The Genesis Graft operational history.

## 🏁 OUTPUT
Provide a definitive "Build-In" report that includes the exact shell commands to be executed on the Host and Guest to finalize the sensor ignition.
