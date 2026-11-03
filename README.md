# Distortion Product Otoacoustic Emissions (DPOAE) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Distortion Product Otoacoustic Emissions (DPOAE), cochlear outer hair cell biomechanics, and headphone noise damage.

```mermaid
flowchart TD
    DualTones["Primary Pure Tones (F1: 65 dB, F2: 55 dB)"] --> EarCanalProbe["Low-Noise Sensitive Miniature Microphone"]
    EarCanalProbe --> SpectralAnalysis["FFT Extraction of 2F1 - F2 Distortion Peak"]
    SpectralAnalysis --> SNR_Engine["Signal-to-Noise Ratio & Clinical Pass Logic"]
    SNR_Engine --> CochlearScore["Cochlear Outer Hair Cell Resilience Engine"]
    CochlearScore --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Clinical Audiological Standards**: Implements clinical pass criteria ($SNR \ge 6 \text{ dB}$, $Amp \ge -5 \text{ dB SPL}$).
- **Early Noise Overexposure Detection**: Identifies outer hair cell fatigue before pure-tone hearing threshold loss occurs.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import AcousticOtoacousticEmissionsClient

client = AcousticOtoacousticEmissionsClient()
result = client.evaluate_dpoae(
    f2_frequency_hz=2000.0,
    dpoae_amplitude_db_spl=8.5,
    noise_floor_db_spl=-12.5
)
print("DPOAE SNR:", result["signal_to_noise_ratio_snr_db"], "dB")
print("Classification:", result["classification"])
```

## License
Apache-2.0
