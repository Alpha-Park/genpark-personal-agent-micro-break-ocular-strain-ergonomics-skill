# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Micro Break Ocular Strain Ergonomics Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentMicroBreakOcularStrainErgonomics

mcp = FastMCP("PersonalAgentMicroBreakOcularStrainErgonomics")
client = PersonalAgentMicroBreakOcularStrainErgonomics()

@mcp.tool()
def calculate_ciliary_ocular_strain(
    screen_time_continuous_minutes: float,
    viewing_distance_cm: float = 50.0,
    ambient_lux: float = 350.0,
    screen_nits: float = 300.0
) -> str:
    """Calculates accommodation diopters, suppressed blink rate, and 20-20-20 micro-break urgency."""
    import json
    return json.dumps(client.calculate_ciliary_ocular_strain(
        screen_time_continuous_minutes, viewing_distance_cm, ambient_lux, screen_nits
    ), indent=2)

@mcp.tool()
def calculate_cervical_spine_torque(
    head_tilt_angle_degrees: float = 30.0,
    head_mass_kg: float = 5.0
) -> str:
    """Calculates Hansraj biomechanical cervical spine load and ergonomic corrections."""
    import json
    return json.dumps(client.calculate_cervical_spine_torque(
        head_tilt_angle_degrees, head_mass_kg
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
