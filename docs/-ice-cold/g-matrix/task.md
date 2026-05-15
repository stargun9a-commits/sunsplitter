# GENESIS PRIME: OPERATIONAL CHECKLIST

## [PHASE 3] SENSOR IGNITION: THE BINDING
- [x] **SHAM HANDSHAKE**: Implement Wandio V18.11 stubs to satisfy linker probes.
- [x] **C-CORE BUILD**: Successfully compile and install `libbgpstream` 2.2.0.
- [/] **PY-BINDING GRAFT**: Finalize `pybgpstream` Python bindings.
    - [x] Graft `pybgpstream` source into the Hub.
    - [x] Graft `setuptools` source/wheels into the Hub.
    - [ ] **BLOCKER**: Graft `python3.11-dev` headers from Host (Noble) to Guest.
- [ ] **SENSOR ASSERTION**: Verify `import pybgpstream` within the isolated substrate.

## [PHASE 4] AUTONOMOUS DISCOVERY
- [ ] **DISCOVERY IGNITION**: Launch `matrix-discovery-v2.py`.
- [ ] **MRT ARCHIVE LINK**: Map local MRT forensic data to the sensor feed.
- [ ] **HARDWARE BLINDING**: Execute PCI unbind logic to seal the NICs.
- [ ] **VSOCK TELEMETRY**: Establish the out-of-band log stream to the Host.

## [PHASE 5] AUDIT & ANALYSIS
- [ ] **BGP FOOTPRINTING**: Initiate 6-minute anomaly persistence detection.
- [ ] **GHOST-HUNTER REPORTING**: Generate cryptographically sealed forensic logs.
