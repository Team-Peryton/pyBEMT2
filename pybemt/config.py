from dataclasses import dataclass, field
from typing import List


@dataclass
class Config:
    """
    rpm - rpm of propeller
    v_inf - freestream

    nblades - number of blades
    diameter - diameter of propeller 
    radius_hub - radius of the central hub (non blade)
    section - list of aerofoils
    radius - positions of aerfoils, chord and pitch data
    chord - chord of section at radius
    pitch - pitch of section at radius

    rho
    mu
    """
    # case
    rpm: float = 0.0
    v_inf: float = 0.0
    twist: float = 0.0
    rotor: bool = True # Turbine mode if False
    
    # rotor
    n_blades: int = 2
    diameter: float = 0.0
    radius_hub: float = 0.0

    section: List[str] = field(default_factory=[])
    radius: List[float] = field(default_factory=[])
    chord: List[float] = field(default_factory=[])
    pitch: List[float] = field(default_factory=[])

    # optional rotor 2
    coaxial:bool = False
    rpm2: float = 0.0
    twist2: float = 0.0
    dz: float = 0.0

    # fluid
    rho: float = 1.225
    mu: float = 1.81e-5
    
    # turbine
    pvap: int = 0
    patm: int = 0
    depth: float = 0.0
