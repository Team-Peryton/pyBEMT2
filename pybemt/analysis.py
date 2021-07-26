import math

def speed_of_sound(gamma, pressure, density):
    return math.sqrt(gamma*(pressure/density))


def tip_speed(rpm, diameter):
    """
    Assumes standard atmosphere sea level conditions
    rpm
    diameter: meters
    returns: Mach speed at tip
    """
    return ( (diameter * math.pi * rpm) / 60 ) / speed_of_sound(1.4,101325,1.225)


def max_rpm_from_tip_speed(diameter):
    """
    for a given diameter, return the max RPM to stay within 0.7 mach tip speed
    """
    return (0.7 * speed_of_sound(1.4,101325,1.225) * 60)/(math.pi * diameter)