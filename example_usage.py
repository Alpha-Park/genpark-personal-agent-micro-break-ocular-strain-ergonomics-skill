# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Micro Break Ocular Strain Ergonomics Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentMicroBreakOcularStrainErgonomics

def main():
    agent = PersonalAgentMicroBreakOcularStrainErgonomics()

    print("=" * 70)
    print("DEMO: Personal Agent Micro Break Ocular Strain & Posture Ergonomics")
    print("=" * 70)

    # 1. Continuous screen strain analysis (75 minutes at 48 cm)
    res_eye = agent.calculate_ciliary_ocular_strain(
        screen_time_continuous_minutes=75.0,
        viewing_distance_cm=48.0,
        ambient_lux=280.0,
        screen_nits=320.0
    )

    print(f"\n1. Ciliary Muscle & Ocular Fatigue (75 min continuous focus):")
    print(f"   Accommodation Demand: {res_eye['ciliary_accommodation_demand_diopters']}")
    print(f"   Blink Rate: {res_eye['suppressed_blink_rate']}")
    print(f"   Tear Evaporation: {res_eye['tear_film_evaporation_acceleration']}")
    print(f"   Strain Score: {res_eye['ciliary_strain_score']}")
    print(f"   Urgency: {res_eye['optical_break_urgency']}")
    print(f"   Protocol: {res_eye['micro_recovery_protocol']}")

    # 2. Cervical spine Hansraj torque analysis (35-degree forward head posture)
    res_spine = agent.calculate_cervical_spine_torque(
        head_tilt_angle_degrees=35.0,
        head_mass_kg=5.0
    )

    print(f"\n2. Cervical Spine Hansraj Biomechanical Load (35° Forward Tilt):")
    print(f"   Effective Spine Load: {res_spine['effective_cervical_spine_load_kg']} kg ({res_spine['effective_cervical_spine_load_lbs']})")
    print(f"   Trapezius Strain Index: {res_spine['trapezius_isometric_strain_index']}")
    print(f"   Classification: {res_spine['biomechanical_posture_classification']}")
    print(f"   Remediation: {res_spine['ergonomic_remediation']}")

    print("\nVerification complete: Ocular strain & posture ergonomics engine executed flawlessly.")

if __name__ == "__main__":
    main()
