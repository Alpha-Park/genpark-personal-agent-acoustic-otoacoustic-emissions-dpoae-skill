"""
Example Usage: Distortion Product Otoacoustic Emissions (DPOAE) Evaluation.
Demonstrates non-invasive assessment of cochlear outer hair cell biomechanics and SNR.
"""

from client import AcousticOtoacousticEmissionsClient


def main():
    client = AcousticOtoacousticEmissionsClient()
    print("=== Distortion Product Otoacoustic Emissions (DPOAE) Demo ===")

    # Test Case 1: Healthy normal cochlear outer hair cells (2 kHz primary)
    res1 = client.evaluate_dpoae(
        f2_frequency_hz=2000.0,
        dpoae_amplitude_db_spl=8.5,
        noise_floor_db_spl=-12.5,
        l1_level_db_spl=65.0,
        l2_level_db_spl=55.0
    )
    print("\nTest Case 1: Healthy Cochlear Amplification (2000 Hz)")
    print(f"  F1: {res1['f1_frequency_hz']} Hz | F2: {res1['f2_frequency_hz']} Hz | 2f1-f2: {res1['distortion_frequency_fdp_hz']} Hz")
    print(f"  Emission: {res1['dpoae_amplitude_db_spl']} dB SPL | Noise: {res1['noise_floor_db_spl']} dB SPL")
    print(f"  SNR: {res1['signal_to_noise_ratio_snr_db']} dB | Clinical Pass: {res1['meets_clinical_pass']}")
    print(f"  Cochlear Score: {res1['cochlear_ohc_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Subclinical acoustic trauma / excessive earphone exposure (4 kHz notch)
    res2 = client.evaluate_dpoae(
        f2_frequency_hz=4000.0,
        dpoae_amplitude_db_spl=-4.0,
        noise_floor_db_spl=-8.5
    )
    print("\nTest Case 2: Subclinical High-Frequency Noise Damage (4000 Hz)")
    print(f"  Emission: {res2['dpoae_amplitude_db_spl']} dB SPL | SNR: {res2['signal_to_noise_ratio_snr_db']} dB")
    print(f"  Clinical Pass: {res2['meets_clinical_pass']}")
    print(f"  Cochlear Score: {res2['cochlear_ohc_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
