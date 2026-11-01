# -*- coding: utf-8 -*-
"""
Personal Agent Micro Break Ocular Strain Ergonomics Client
Zero-dependency ciliary accommodation spasm modeler, Hansraj cervical spine torque
calculator, tear film break-up time estimator, and 20-20-20 micro-recovery scheduler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentMicroBreakOcularStrainErgonomics:
    """
    Quantifies continuous visual terminal display strain, ciliary muscle fatigue,
    Hansraj cervical spine gravitational torque, and schedules posture/optical micro-breaks.
    """

    def calculate_ciliary_ocular_strain(
        self,
        screen_time_continuous_minutes: float,
        viewing_distance_cm: float = 50.0,
        ambient_lux: float = 350.0,
        screen_nits: float = 300.0
    ) -> Dict[str, Any]:
        """
        Calculates ocular accommodation demand (diopters), blink rate suppression,
        and tear film evaporation risk from continuous computer monitor use.
        """
        mins = max(1.0, min(720.0, float(screen_time_continuous_minutes)))
        dist = max(20.0, min(150.0, float(viewing_distance_cm)))
        amb_lux = max(10.0, min(5000.0, float(ambient_lux)))
        nits = max(50.0, min(1500.0, float(screen_nits)))

        # Accommodation demand in diopters (D = 100 / distance_cm)
        diopters = round(100.0 / dist, 2)

        # Blink rate suppression: normal resting rate of 18 blinks/min drops to ~4-6 blinks/min
        blink_rate_blinks_min = round(max(3.5, 18.0 - (diopters * 3.5) - min(8.0, mins * 0.05)), 1)
        tear_evaporation_multiplier = round(18.0 / max(3.5, blink_rate_blinks_min), 2)

        # Contrast luminance ratio between display and ambient
        # Ideal ambient lux to screen nit ratio is approximately 1:1 to 1:2
        luminance_ratio = round(nits / max(10.0, amb_lux), 2)
        contrast_strain = abs(luminance_ratio - 1.0) * 12.0

        # Cumulative ciliary strain index (0 - 100 pts)
        ciliary_strain = round(min(100.0, (mins * 0.45 * diopters) + contrast_strain), 1)

        # 20-20-20 rule compliance status
        if mins >= 60.0:
            urgency = "IMMEDIATE OPTICAL INTERVENTION REQUIRED"
            break_rx = "Mandatory 30-second distant gaze (>20 feet / 6 meters), 10 voluntary full blinks, and warm palm palming."
        elif mins >= 25.0:
            urgency = "MICRO-BREAK RECOMMENDED"
            break_rx = "Execute 20-20-20 rule: Look at a target 20 feet away for 20 seconds to completely disengage the ciliary muscle."
        else:
            urgency = "NOMINAL VISUAL ENDURANCE"
            break_rx = "Visual fatigue well-buffered. Next 20-20-20 reset due in " + str(int(20.0 - (mins % 20.0))) + " minutes."

        return {
            "continuous_screen_minutes": mins,
            "viewing_distance_cm": dist,
            "ciliary_accommodation_demand_diopters": f"{diopters} D",
            "suppressed_blink_rate": f"{blink_rate_blinks_min} blinks/min (Normal: 18 bpm)",
            "tear_film_evaporation_acceleration": f"{tear_evaporation_multiplier}x faster dry eye progression",
            "ciliary_strain_score": f"{ciliary_strain} / 100",
            "optical_break_urgency": urgency,
            "micro_recovery_protocol": break_rx
        }

    def calculate_cervical_spine_torque(
        self,
        head_tilt_angle_degrees: float = 30.0,
        head_mass_kg: float = 5.0
    ) -> Dict[str, Any]:
        """
        Calculates gravitational moment torque and effective weight on the cervical spine
        using Dr. Kenneth Hansraj's bio-mechanical cervical spine model.
        """
        deg = max(0.0, min(75.0, float(head_tilt_angle_degrees)))
        mass = max(3.0, min(8.0, float(head_mass_kg)))

        # Hansraj biomechanical empirical scaling:
        # 0 deg: ~5kg, 15 deg: ~12kg, 30 deg: ~18kg, 45 deg: ~22kg, 60 deg: ~27kg
        rad = math.radians(deg)
        torque_factor = 1.0 + (math.sin(rad) * 4.45)
        effective_cervical_load_kg = round(mass * torque_factor, 1)
        effective_load_lbs = round(effective_cervical_load_kg * 2.20462, 1)

        # Upper trapezius and levator scapulae isometric strain percentage
        trapezius_ischemic_strain_pct = round(min(100.0, (effective_cervical_load_kg / 27.0) * 100.0), 1)

        if deg <= 10.0:
            posture_status = "Neutral Alignment (Optimal Craniovertebral Angle)"
            correction = "Ideal biomechanical axial alignment. Minimal muscular tension."
        elif deg <= 25.0:
            posture_status = "Mild Anterior Head Translation"
            correction = "Elevate monitor by 5-8 cm so top third of screen aligns with eye level."
        elif deg <= 40.0:
            posture_status = "Moderate Cervical Kyphosis Strain"
            correction = "Significant posterior cervical muscle load. Perform 5 chin tuck retractions and elevate display."
        else:
            posture_status = "Severe 'Text-Neck' Cervical Facet Compression"
            correction = "CRITICAL: 60 lbs equivalent load on C5-C7 vertebrae. Stand immediately, execute thoracic extension, and raise screen to eye level."

        return {
            "head_tilt_angle_degrees": deg,
            "head_mass_kg": mass,
            "effective_cervical_spine_load_kg": effective_cervical_load_kg,
            "effective_cervical_spine_load_lbs": f"{effective_load_lbs} lbs",
            "trapezius_isometric_strain_index": f"{trapezius_ischemic_strain_pct}% of max capacity",
            "biomechanical_posture_classification": posture_status,
            "ergonomic_remediation": correction
        }
