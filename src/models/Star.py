from utils.Physics import Physics

from models.CelestialBody import CelestialBody

class Star(CelestialBody):
    """
    A class to represent a star.

    Attributes:
    -----------
    mass (float): Mass of the star in kilograms (kg).
    radius (float): Radius of the star in meters (m).
    luminosity (float): Luminosity of the star in Watts (W). Default is 0.
    temperature (float): Surface temperature of the star in Kelvin (K). Default is 0.
    """
    def __init__(self, mass, radius, luminosity=0, temperature=0):
        super().__init__(mass, radius)
        self.luminosity = luminosity   # (Watts (W))
        self.temperature = temperature # (Kelvin (K))

    def get_escape_velocity(self):
        if self.radius == 0:
            raise ValueError("Radius cannot be zero")
        return Physics.escape_velocity(self.mass, self.radius)
    
    def get_surface_gravity(self):
        return super().get_surface_gravity()