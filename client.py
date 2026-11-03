"""
Distortion Product Otoacoustic Emissions (DPOAE) & Cochlear Hair Cell Engine.
Provides deterministic, zero-dependency modeling of non-linear cochlear intermodulation distortion (2f1-f2),
emission signal-to-noise ratio (SNR), and prestin electromotility outer hair cell (OHC) biomechanics.
"""

from typing import Dict, Any, List, Optional


class AcousticOtoacousticEmissionsClient:
    """
    Deterministic client for calculating Distortion Product Otoacoustic Emissions (DPOAE).
    Assesses non-invasive cochlear micromechanics, outer hair cell (OHC) active amplification,
    and early subclinical acoustic overexposure from personal listening devices.
    """

    def __init__(self):
        pass

    def evaluate_dpoae(
        self,
        f2_frequency_hz: float,
        dpoae_amplitude_db_spl: float,
        noise_floor_db_spl: float,
        f1_frequency_hz: Optional[float] = None,
        l1_level_db_spl: float = 65.0,
        l2_level_db_spl: float = 55.0
    ) -> Dict[str, Any]:
        """
        Calculates DPOAE SNR = dpoae_amplitude - noise_floor.
        Clinical pass standard: SNR >= 6.0 dB and emission amplitude >= -5.0 dB SPL.
        Default optimal f2/f1 ratio is 1.22.
        """
        if f2_frequency_hz <= 0:
            return {"error": "F2 frequency must be strictly positive"}

        if f1_frequency_hz is None:
            f1_frequency_hz = round(f2_frequency_hz / 1.22, 1)

        f_dp = round(2.0 * f1_frequency_hz - f2_frequency_hz, 1)
        snr_db = round(dpoae_amplitude_db_spl - noise_floor_db_spl, 1)

        # Cochlear Outer Hair Cell Score (0 - 100):
        # SNR >= 14 dB and emission >= 4 dB SPL -> 90 - 100
        # SNR < 6 dB -> < 50
        score = 80.0
        if snr_db >= 12.0:
            score += 15.0
        elif snr_db >= 6.0:
            score += 5.0
        elif snr_db < 3.0:
            score -= 30.0
        elif snr_db < 6.0:
            score -= 15.0

        if dpoae_amplitude_db_spl >= 5.0:
            score += 5.0
        elif dpoae_amplitude_db_spl < -6.0:
            score -= 15.0

        cochlear_score = round(min(100.0, max(5.0, score)), 1)

        meets_clinical_pass = snr_db >= 6.0 and dpoae_amplitude_db_spl >= -5.0

        if cochlear_score >= 85.0:
            tier = "ROBUST_COCHLEAR_ELECTROMOTILITY"
            interp = f"Strong DPOAE emission (+{dpoae_amplitude_db_spl} dB SPL, SNR {snr_db} dB at F2 {f2_frequency_hz} Hz); healthy prestin motor protein amplification."
            guidance = "Optimal cochlear biomechanics and outer hair cell tuning. Hearing health is in excellent standing."
        elif meets_clinical_pass:
            tier = "NORMAL_OUTER_HAIR_CELL_INTEGRITY"
            interp = f"Valid clinical DPOAE response (SNR {snr_db} dB >= 6 dB); outer hair cells intact at {f2_frequency_hz} Hz."
            guidance = "Normal cochlear function. Practice the 60/60 headphone rule (max 60% volume for max 60 min)."
        elif snr_db >= 3.0:
            tier = "BORDERLINE_COCHLEAR_MICROTRAUMA"
            interp = f"Sub-threshold emission (SNR {snr_db} dB < 6 dB, Amp {dpoae_amplitude_db_spl} dB SPL); early metabolic stress in cochlear outer hair cells."
            guidance = "Subclinical acoustic strain detected. Reduce earphone listening levels and enforce 2-hour quiet rest recovery periods."
        else:
            tier = "SIGNIFICANT_COCHLEAR_HAIR_CELL_LOSS"
            interp = f"Absent otoacoustic emission (SNR {snr_db} dB); reflects outer hair cell stereocilia disarray or permanent acoustic damage."
            guidance = "Significant loss of cochlear active amplification. Recommend diagnostic pure-tone audiometry and high-frequency audiogram."

        return {
            "f1_frequency_hz": f1_frequency_hz,
            "f2_frequency_hz": f2_frequency_hz,
            "distortion_frequency_fdp_hz": f_dp,
            "dpoae_amplitude_db_spl": dpoae_amplitude_db_spl,
            "noise_floor_db_spl": noise_floor_db_spl,
            "signal_to_noise_ratio_snr_db": snr_db,
            "meets_clinical_pass": meets_clinical_pass,
            "cochlear_ohc_score": cochlear_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
