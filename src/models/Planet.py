from utils.Physics import Physics
from models.CelestialBody import CelestialBody

class Planet(CelestialBody):
    def __init__(self, mass, radius, eccentricity, aphelion, min_orbit_velocity, satellites=0, rings=0):
        """
        Class representing a planet.
        
        Attributes:
            mass (float): The mass of the planet in kilograms (kg).
            radius (float): The radius of the planet in meters (m).
            eccentricity (float): The eccentricity of the planet's orbit.
            aphelion (float): The distance from the planet to the Sun at its farthest point in meters (m).
            min_orbit_velocity (float): The velocity of the planet at its nearest point to the Sun in meters per second (m/s).
            satellites (int): The number of satellites (moons) the planet has.
            rings (int): The number of rings the planet has.
            
        Methods:
            get_escape_velocity(): Returns the escape velocity of the planet.
            get_surface_gravity(): Returns the surface gravity of the planet.
        """
        super().__init__(mass, radius)
        self.eccentricity = eccentricity
        self.aphelion = aphelion
        self.min_orbit_velocity = min_orbit_velocity
        self.perihelion = aphelion * (1 - eccentricity)
        self.satellites = satellites
        self.rings = rings

    def get_escape_velocity(self):
        """
        Calculates and returns the escape velocity of the planet.
        
        Returns:
            The escape velocity of the planet in meters per second (m/s).
        """
        if self.radius == 0:
            raise ValueError("Radius cannot be zero")
        return Physics.escape_velocity(self.mass, self.radius)
    
    def get_surface_gravity(self):
        """
        Calculates and returns the surface gravity of the planet.
        
        Returns:
            The surface gravity of the planet in meters per second squared (m/s^2).
        """
        if self.radius == 0:
            raise ValueError("Radius cannot be zero")
        return Physics.gravitational_acceleration(self.mass, self.radius)