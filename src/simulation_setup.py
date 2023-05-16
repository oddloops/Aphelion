from models.Planet import Planet
from models.Star import Star
from utils.Physics import Physics

# Celestial Bodies
earth = Planet(5.972e24, 6.371e6)
sun = Star(1.989e30, 6.957e8, 3.828e+29, 5773.15)

AU = 1.5e11  # meters

# Constants for Earth Sun
average_earth_sun_distance = 1.496e11
earth_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, earth.mass, 1) # using radius during simulation calculation
earth_aphelion = 1.521e11 # Farthest Earth to Sun distance (1.017 Astronomical Unit)
earth_velocity_aphelion = 29290
earth_eccentricity = 0.01671
earth_perihelon = earth_aphelion * (1 - earth_eccentricity) # Closest Earth to Sun distance (0.983 AU)

# starting conditions
# Sun
sun_x, sun_y, sun_z = 0, 0, 0
sun_velocity_x, sun_velocity_y, sun_velocity_z = 0, 0, 0

# Earth
earth_x, earth_y, earth_z = earth_perihelon, 0, 0
earth_velocity_x, earth_velocity_y, earth_velocity_z = 0, earth_velocity_aphelion, 0

# Time
time = 0
delta_time = 1 * Physics.days_in_secs # frames move in this time

# Positions of Celestial Bodies
sun_x_list, sun_y_list, sun_z_list = [], [], []
earth_x_list, earth_y_list, earth_z_list = [], [], []

# Start simulation
while time < 1 * 365 * Physics.days_in_secs:
    ###### The Earth #######
    # For Earth, compute G force on Earth
    radius_x, radius_y, radius_z = earth_x - sun_x, earth_y - sun_y, earth_z - sun_z
    magnitude_vector_3 = (radius_x ** 2 + radius_y ** 2 + radius_z ** 2) ** 1.5   # magnitude of vector
    force_earth_x = -earth_gravitational_constant * radius_x / magnitude_vector_3
    force_earth_y = -earth_gravitational_constant * radius_y / magnitude_vector_3
    force_earth_z = -earth_gravitational_constant * radius_z / magnitude_vector_3

    # Update quantities (F = ma -> a = F / m)
    earth_velocity_x += force_earth_x * delta_time / earth.mass
    earth_velocity_y += force_earth_y * delta_time / earth.mass
    earth_velocity_z += force_earth_z * delta_time / earth.mass

    # Update Earth position
    earth_x += earth_velocity_x * delta_time
    earth_y += earth_velocity_y * delta_time
    earth_z += earth_velocity_z * delta_time

    # Save the Earth position
    earth_x_list.append(earth_x)
    earth_y_list.append(earth_y)
    earth_z_list.append(earth_z)

    ###### The Sun #######
    sun_velocity_x += -force_earth_x * delta_time / sun.mass
    sun_velocity_y += -force_earth_y * delta_time / sun.mass
    sun_velocity_z += -force_earth_z * delta_time / sun.mass

    # Update Sun position
    sun_x += sun_velocity_x * delta_time
    sun_y += sun_velocity_y * delta_time
    sun_z += sun_velocity_z * delta_time

    # Save the Sun position
    sun_x_list.append(sun_x)
    sun_y_list.append(sun_y)
    sun_z_list.append(sun_z)

    # Update delta time
    time += delta_time