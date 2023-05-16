from models.Planet import Planet
from models.Star import Star
from utils.Physics import Physics

# Celestial Bodies
earth = Planet(5.972e24, 6.371e6)
sun = Star(1.989e30, 6.957e8, 3.828e+29, 5773.15)

# Constants for Earth Sun
average_earth_sun_distance = 1.496e11
AU = 1.521e11 # Earth to Sun distance
earth_velocity_aphelion =  29290
earth_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, earth.mass, average_earth_sun_distance)

