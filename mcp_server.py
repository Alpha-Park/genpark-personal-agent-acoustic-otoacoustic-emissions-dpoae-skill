"""
MCP Server for Distortion Product Otoacoustic Emissions (DPOAE) Skill.
Exposes JSON-RPC Model Context Protocol tools for assessing cochlear micromechanics and outer hair cell health.
"""

import sys
import json
from typing import Dict, Any
from client import AcousticOtoacousticEmissionsClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_dpoae",
                "description": "Calculates DPOAE 2f1-f2 distortion product frequency, SNR, clinical pass/fail, and cochlear outer hair cell score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "f2_frequency_hz": {
                            "type": "number",
                            "description": "F2 primary acoustic frequency in Hz (e.g. 2000.0 Hz or 4000.0 Hz)."
                        },
                        "dpoae_amplitude_db_spl": {
                            "type": "number",
                            "description": "Measured distortion product emission amplitude in dB SPL (e.g. +7.5 dB SPL)."
                        },
                        "noise_floor_db_spl": {
                            "type": "number",
                            "description": "Background noise level in dB SPL (e.g. -11.0 dB SPL)."
                        },
                        "f1_frequency_hz": {
                            "type": "number",
                            "description": "Optional F1 frequency in Hz (defaults to F2 / 1.22)."
                        },
                        "l1_level_db_spl": {
                            "type": "number",
                            "description": "L1 primary level in dB SPL (typically 65.0 dB SPL).",
                            "default": 65.0
                        },
                        "l2_level_db_spl": {
                            "type": "number",
                            "description": "L2 primary level in dB SPL (typically 55.0 dB SPL).",
                            "default": 55.0
                        }
                    },
                    "required": ["f2_frequency_hz", "dpoae_amplitude_db_spl", "noise_floor_db_spl"]
                }
            }
        ]
    }


def handle_request(client: AcousticOtoacousticEmissionsClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_dpoae":
            f1_val = args.get("f1_frequency_hz")
            if f1_val is not None:
                f1_val = float(f1_val)

            res = client.evaluate_dpoae(
                f2_frequency_hz=float(args.get("f2_frequency_hz", 2000.0)),
                dpoae_amplitude_db_spl=float(args.get("dpoae_amplitude_db_spl", 5.0)),
                noise_floor_db_spl=float(args.get("noise_floor_db_spl", -10.0)),
                f1_frequency_hz=f1_val,
                l1_level_db_spl=float(args.get("l1_level_db_spl", 65.0)),
                l2_level_db_spl=float(args.get("l2_level_db_spl", 55.0))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = AcousticOtoacousticEmissionsClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
