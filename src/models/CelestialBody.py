import abc

class CelestialBody(metaclass=abc.ABCMeta):
    def __init__(self, mass, radius):
        """
        Abstract base class representing a celestial body.
        
        Attributes:
            mass (float): The mass of the celestial body in kilograms (kg).
            radius (float): The radius of the celestial body in meters (m).
            
        Methods:
            get_escape_velocity(): Abstract method that returns the escape velocity of the celestial body.
            get_surface_gravity(): Abstract method that returns the surface gravity of the celestial body.
        """
        self.mass = mass
        self.radius = radius

    @abc.abstractmethod
    def get_escape_velocity(self):
        pass

    @abc.abstractmethod
    def get_surface_gravity(self):
        pass