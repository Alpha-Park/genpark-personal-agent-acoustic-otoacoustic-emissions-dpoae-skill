---
name: genpark-personal-agent-acoustic-otoacoustic-emissions-dpoae-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for evaluating Distortion Product Otoacoustic Emissions (DPOAE), cochlear outer hair cell biomechanics, and headphone noise damage.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Distortion Product Otoacoustic Emissions (DPOAE) Skill

A sovereign personal agent capability for assessing cochlear outer hair cell (OHC) active amplification, calculating non-linear intermodulation distortion ($2f_1 - f_2$), and early detection of subclinical acoustic trauma from headphone usage.

## Core Capabilities
- **Distortion Product Frequency Derivation**: Calculates $2f_1 - f_2$ intermodulation emissions based on standard $f_2/f_1 = 1.22$ ratio.
- **Signal-to-Noise Ratio (SNR)**: Computes emission margin above probe noise floor against clinical pass criteria ($\ge 6\text{ dB}$).
- **Cochlear OHC Health Score**: 0-100 index quantifying prestin motor protein active biomechanical amplification.
- **Auditory Hygiene Guidance**: Implements the 60/60 rule and quiet acoustic recovery schedules.

## Fast Invocation
```python
from client import AcousticOtoacousticEmissionsClient

client = AcousticOtoacousticEmissionsClient()
res = client.evaluate_dpoae(
    f2_frequency_hz=2000.0,
    dpoae_amplitude_db_spl=8.5,
    noise_floor_db_spl=-12.5
)
print("DPOAE SNR:", res["signal_to_noise_ratio_snr_db"], "dB")
print("Cochlear Score:", res["cochlear_ohc_score"])
```
