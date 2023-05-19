import math

class Physics:
    # Constants
    G = 6.67430e-11 # Gravitational Constant (m^3/kg/s^2)
    SOLAR_MASS = 1.989e30 # in kilograms (kg)
    AU =  1.496e11  # in meters (m)
    days_in_secs = 24 * 60.0 * 60.0

    # Equations
    @staticmethod
    def change_in_velocity (acceleration, delta_time):
        """
        Calculate the velocity after delta time (dv = a * dt)

        Args:
            acceleration (float): The acceleration of a object (m / s^2)
            delta_time (float): change in time (s)
        
        Return:
            float: Change in velocity (m/s)
        """
        return acceleration * delta_time

    @staticmethod
    def change_in_displacement (velocity, delta_velocity, delta_time):
        """
        Calculate the change of displacement (dd = (v + dv) * dt)

        Args:
            velocity (float): velocity of the object (m/s)
            delta_velocity (float): change in velocity (m/s)
            delta_time (float): change in time (s)

        Result:
            float: the change in displacement (m)
        """
        return (velocity + delta_velocity) * delta_time
    
    @staticmethod
    def newton_second_law(mass, acceleration):
        """
        Calculate force using Newon's Second Law (F = ma)

        Args:
            mass (float): The mass of an object (kg)
            acceleration (float): The acceleration of the object (m/s^2)

        Return:
            float: The force applied to the object in Newtons (N)
        """
        return mass * acceleration

    @classmethod
    def law_of_universial_gravitation(cls, mass1, mass2, r=1):
        """
        Calculate Newton's Law of Universial Gravitation (F=-G(Mm/r^2))

        Args:
            G (float): Gravitational Constant
            mass1 (float): mass of object 1 (kg)
            mass2 (float): mass of object 2 (kg)
            r (float): distance between object1 & object2's center (m)

        Return:
            float: Gravitational force of attaction in Newtons (N)

        Notes:
            The gravitational constant `G` used in the calculation is a class constant that has a default value of 6.67430e-11 m^3/kg/s^2. 
            It can be overridden by setting the class attribute `G` to a different value explicitly before calling this method.
        """
        return cls.G * (mass1 * mass2) / (r**2)
    
    @classmethod
    def gravitational_acceleration(cls, mass, r):
        """
        Calculates the gravitational acceration of a celestial body (G*M/r^2)

        Args:
            G (float): Gravitational Constant
            mass (float): Mass of the object exerting gravitational force (kg)
            r (float): Distance between object and center of object exerting the gravitational force center (m)

        Return:
            float: Gravitational acceleration (m/s^2)
        """
        return cls.G * mass / r ** 2

    @classmethod
    def escape_velocity(cls, mass, r):
        """
        Calculates the escape velocity of a celestial body (Sqrt(2GM / r))

        Args:
            G (float): Gravitational Constant
            mass (float): Mass of the attracting object
            r (float): Radius of the attracting object
        """
        return math.sqrt(2 * cls.G * mass / r)