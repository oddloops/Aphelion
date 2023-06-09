from models.Planet import Planet
from models.Star import Star
from utils.Physics import Physics

AU = Physics.AU  # meters

# Celestial Bodies
sun = Star(1.989e30, 6.957e8, 3.828e29, 5773.15)
mercury = Planet(3.30104e23, 2.4397e6, 0.20563593, 6.9818e10, 38860)
venus = Planet(4.8673e24, 6.0518e6, 0.00677672, 1.08941e11, 34780)
earth = Planet(5.9722e24, 6.371e6, 0.01671123, 1.521e11, 29290, 1)
mars = Planet(6.4169e23, 3.3895e6, 0.0933941, 2.49261e11, 21971, 2)
jupiter = Planet(1.89813e27, 6.9911e7, 0.04838624, 8.16363e11, 12440, 95, 3)
saturn = Planet(5.6832e26, 5.8232e7, 0.05386179, 1.506527e12, 9140, 83, 7)
uranus = Planet(8.68103e25, 2.5362e7, 0.04725744, 3.00139e12, 6490, 27, 13)
neptune = Planet(1.0241e26, 2.4622e7, 0.00859048, 4.558857e12, 5370, 14, 5)

# Gravitational Constants
mercury_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, mercury.mass)
venus_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, venus.mass)
earth_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, earth.mass) # using radius during simulation calculation
mars_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, mars.mass)
jupiter_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, jupiter.mass)
saturn_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, saturn.mass)
uranus_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, uranus.mass)
neptune_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, neptune.mass)

# starting conditions
# Sun
sun_x, sun_y, sun_z = 0, 0, 0
sun_velocity_x, sun_velocity_y, sun_velocity_z = 0, 0, 0

# Mercury
mercury_x, mercury_y, mercury_z = mercury.aphelion, 0, 0
mercury_velocity_x, mercury_velocity_y, mercury_velocity_z = 0, mercury.min_orbit_velocity, 0

# Venus
venus_x, venus_y, venus_z = venus.aphelion, 0, 0
venus_velocity_x, venus_velocity_y, venus_velocity_z = 0, venus.min_orbit_velocity, 0

# Earth
earth_x, earth_y, earth_z = earth.aphelion, 0, 0
earth_velocity_x, earth_velocity_y, earth_velocity_z = 0, earth.min_orbit_velocity, 0

# Mars
mars_x, mars_y, mars_z = mars.aphelion, 0, 0
mars_velocity_x, mars_velocity_y, mars_velocity_z = 0, mars.min_orbit_velocity, 0

# Jupiter
jupiter_x, jupiter_y, jupiter_z = jupiter.aphelion, 0, 0
jupiter_velocity_x, jupiter_velocity_y, jupiter_velocity_z = 0, jupiter.min_orbit_velocity, 0

# Saturn
saturn_x, saturn_y, saturn_z = saturn.aphelion, 0, 0
saturn_velocity_x, saturn_velocity_y, saturn_velocity_z = 0, saturn.min_orbit_velocity, 0

# Uranus
uranus_x, uranus_y, uranus_z = uranus.aphelion, 0, 0
uranus_velocity_x, uranus_velocity_y, uranus_velocity_z = 0, uranus.min_orbit_velocity, 0

# Neptune
neptune_x, neptune_y, neptune_z = neptune.aphelion, 0, 0
neptune_velocity_x, neptune_velocity_y, neptune_velocity_z = 0, neptune.min_orbit_velocity, 0

# Time
time = 0
delta_time = 1 * Physics.days_in_secs # frames move in this time

# Positions of Celestial Bodies
sun_x_list, sun_y_list, sun_z_list = [], [], []
mercury_x_list, mercury_y_list, mercury_z_list = [], [], []
venus_x_list, venus_y_list, venus_z_list = [], [], []
earth_x_list, earth_y_list, earth_z_list = [], [], []
mars_x_list, mars_y_list, mars_z_list = [], [], []
jupiter_x_list, jupiter_y_list, jupiter_z_list = [], [], []
saturn_x_list, saturn_y_list, saturn_z_list = [], [], []
uranus_x_list, uranus_y_list, uranus_z_list = [], [], []
neptune_x_list, neptune_y_list, neptune_z_list = [], [], []

# Simulation data
while time < 165 * 365 * Physics.days_in_secs:
    ###### Mercury ######
    # Mercury G force
    mercury_radius_x, mercury_radius_y, mercury_radius_z = mercury_x - sun_x, mercury_y - sun_y, mercury_z - sun_z
    mercury_magnitude_vector_3 = (mercury_radius_x ** 2 + mercury_radius_y ** 2 + mercury_radius_z ** 2) ** 1.5
    force_mercury_x = -mercury_gravitational_constant * mercury_radius_x / mercury_magnitude_vector_3
    force_mercury_y = -mercury_gravitational_constant * mercury_radius_y / mercury_magnitude_vector_3
    force_mercury_z = -mercury_gravitational_constant * mercury_radius_z / mercury_magnitude_vector_3

    # Update quantities (F = ma -> a = F / m)
    mercury_velocity_x += force_mercury_x * delta_time / mercury.mass
    mercury_velocity_y += force_mercury_y * delta_time / mercury.mass
    mercury_velocity_z += force_mercury_z * delta_time / mercury.mass

    # Update position
    mercury_x += mercury_velocity_x * delta_time
    mercury_y += mercury_velocity_y * delta_time
    mercury_z += mercury_velocity_z * delta_time

    # Save position
    mercury_x_list.append(mercury_x)
    mercury_y_list.append(mercury_y)
    mercury_z_list.append(mercury_z)

    ###### Venus ######
    # Venus G force
    venus_radius_x, venus_radius_y, venus_radius_z = venus_x - sun_x, venus_y - sun_y, venus_z - sun_z
    venus_magnitude_vector_3 = (venus_radius_x ** 2 + venus_radius_y ** 2 + venus_radius_z ** 2) ** 1.5
    force_venus_x = -venus_gravitational_constant * venus_radius_x / venus_magnitude_vector_3
    force_venus_y = -venus_gravitational_constant * venus_radius_y / venus_magnitude_vector_3
    force_venus_z = -venus_gravitational_constant * venus_radius_z / venus_magnitude_vector_3

    # Update quantities (F = ma -> a = F / m)
    venus_velocity_x += force_venus_x * delta_time / venus.mass
    venus_velocity_y += force_venus_y * delta_time / venus.mass
    venus_velocity_z += force_venus_z * delta_time / venus.mass

    # Update position
    venus_x += venus_velocity_x * delta_time
    venus_y += venus_velocity_y * delta_time
    venus_z += venus_velocity_z * delta_time

    # Save position
    venus_x_list.append(venus_x)
    venus_y_list.append(venus_y)
    venus_z_list.append(venus_z)

    ###### The Earth ######
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

    ###### Mars ######
    # Mars G force
    mars_radius_x, mars_radius_y, mars_radius_z = mars_x - sun_x, mars_y - sun_y, mars_z - sun_z
    mars_magnitude_vector_3 = (mars_radius_x ** 2 + mars_radius_y ** 2 + mars_radius_z ** 2) ** 1.5
    force_mars_x = -mars_gravitational_constant * mars_radius_x / mars_magnitude_vector_3
    force_mars_y = -mars_gravitational_constant * mars_radius_y / mars_magnitude_vector_3
    force_mars_z = -mars_gravitational_constant * mars_radius_z / mars_magnitude_vector_3

    # Update quantities (F = ma -> a = F / m)
    mars_velocity_x += force_mars_x * delta_time / mars.mass
    mars_velocity_y += force_mars_y * delta_time / mars.mass
    mars_velocity_z += force_mars_z * delta_time / mars.mass

    # Update Earth position
    mars_x += mars_velocity_x * delta_time
    mars_y += mars_velocity_y * delta_time
    mars_z += mars_velocity_z * delta_time

    # Save the Earth position
    mars_x_list.append(mars_x)
    mars_y_list.append(mars_y)
    mars_z_list.append(mars_z)

    ###### Jupiter ######
    # Jupiter G force
    jupiter_radius_x, jupiter_radius_y, jupiter_radius_z = jupiter_x - sun_x, jupiter_y - sun_y, jupiter_z - sun_z
    jupiter_magnitude_vector_3 = (jupiter_radius_x ** 2 + jupiter_radius_y ** 2 + jupiter_radius_z ** 2) ** 1.5
    force_jupiter_x = -jupiter_gravitational_constant * jupiter_radius_x / jupiter_magnitude_vector_3
    force_jupiter_y = -jupiter_gravitational_constant * jupiter_radius_y / jupiter_magnitude_vector_3
    force_jupiter_z = -jupiter_gravitational_constant * jupiter_radius_z / jupiter_magnitude_vector_3

    # Update quantities (F = ma -> a = F / m)
    jupiter_velocity_x += force_jupiter_x * delta_time / jupiter.mass
    jupiter_velocity_y += force_jupiter_y * delta_time / jupiter.mass
    jupiter_velocity_z += force_jupiter_z * delta_time / jupiter.mass

    # Update Earth position
    jupiter_x += jupiter_velocity_x * delta_time
    jupiter_y += jupiter_velocity_y * delta_time
    jupiter_z += jupiter_velocity_z * delta_time

    # Save the Earth position
    jupiter_x_list.append(jupiter_x)
    jupiter_y_list.append(jupiter_y)
    jupiter_z_list.append(jupiter_z)

    ###### Saturn ######
    # Saturn G force
    saturn_radius_x, saturn_radius_y, saturn_radius_z = saturn_x - sun_x, saturn_y - sun_y, saturn_z - sun_z
    saturn_magnitude_vector_3 = (saturn_radius_x ** 2 + saturn_radius_y ** 2 + saturn_radius_z ** 2) ** 1.5
    force_saturn_x = -saturn_gravitational_constant * saturn_radius_x / saturn_magnitude_vector_3
    force_saturn_y = -saturn_gravitational_constant * saturn_radius_y / saturn_magnitude_vector_3
    force_saturn_z = -saturn_gravitational_constant * saturn_radius_z / saturn_magnitude_vector_3

    # Update quantities (F = ma -> a = F / m)
    saturn_velocity_x += force_saturn_x * delta_time / saturn.mass
    saturn_velocity_y += force_saturn_y * delta_time / saturn.mass
    saturn_velocity_z += force_saturn_z * delta_time / saturn.mass

    # Update Earth position
    saturn_x += saturn_velocity_x * delta_time
    saturn_y += saturn_velocity_y * delta_time
    saturn_z += saturn_velocity_z * delta_time

    # Save the Earth position
    saturn_x_list.append(saturn_x)
    saturn_y_list.append(saturn_y)
    saturn_z_list.append(saturn_z)

    ###### Uranus ######
    # Uranus G force
    uranus_radius_x, uranus_radius_y, uranus_radius_z = uranus_x - sun_x, uranus_y - sun_y, uranus_z - sun_z
    uranus_magnitude_vector_3 = (uranus_radius_x ** 2 + uranus_radius_y ** 2 + uranus_radius_z ** 2) ** 1.5
    force_uranus_x = -uranus_gravitational_constant * uranus_radius_x / uranus_magnitude_vector_3
    force_uranus_y = -uranus_gravitational_constant * uranus_radius_y / uranus_magnitude_vector_3
    force_uranus_z = -uranus_gravitational_constant * uranus_radius_z / uranus_magnitude_vector_3

    # Update quantities (F = ma -> a = F / m)
    uranus_velocity_x += force_uranus_x * delta_time / uranus.mass
    uranus_velocity_y += force_uranus_y * delta_time / uranus.mass
    uranus_velocity_z += force_uranus_z * delta_time / uranus.mass

    # Update Earth position
    uranus_x += uranus_velocity_x * delta_time
    uranus_y += uranus_velocity_y * delta_time
    uranus_z += uranus_velocity_z * delta_time

    # Save the Earth position
    uranus_x_list.append(uranus_x)
    uranus_y_list.append(uranus_y)
    uranus_z_list.append(uranus_z)

    ###### Neptune ######
    # Neptune G force
    neptune_radius_x, neptune_radius_y, neptune_radius_z = neptune_x - sun_x, neptune_y - sun_y, neptune_z - sun_z
    neptune_magnitude_vector_3 = (neptune_radius_x ** 2 + neptune_radius_y ** 2 + neptune_radius_z ** 2) ** 1.5
    force_neptune_x = -neptune_gravitational_constant * neptune_radius_x / neptune_magnitude_vector_3
    force_neptune_y = -neptune_gravitational_constant * neptune_radius_y / neptune_magnitude_vector_3
    force_neptune_z = -neptune_gravitational_constant * neptune_radius_z / neptune_magnitude_vector_3

    # Update quantities (F = ma -> a = F / m)
    neptune_velocity_x += force_neptune_x * delta_time / neptune.mass
    neptune_velocity_y += force_neptune_y * delta_time / neptune.mass
    neptune_velocity_z += force_neptune_z * delta_time / neptune.mass

    # Update Earth position
    neptune_x += neptune_velocity_x * delta_time
    neptune_y += neptune_velocity_y * delta_time
    neptune_z += neptune_velocity_z * delta_time

    # Save the Earth position
    neptune_x_list.append(neptune_x)
    neptune_y_list.append(neptune_y)
    neptune_z_list.append(neptune_z)

    ###### The Sun ######
    sun_velocity_x += -(force_mercury_x + force_venus_x + force_earth_x + force_mars_x + force_jupiter_x + force_saturn_x + force_uranus_x + force_neptune_x) * delta_time / sun.mass
    sun_velocity_y += -(force_mercury_y + force_venus_y + force_earth_y + force_mars_y + force_jupiter_y + force_saturn_y + force_uranus_y + force_neptune_y) * delta_time / sun.mass
    sun_velocity_z += -(force_mercury_z + force_venus_z + force_earth_z + force_mars_z + force_jupiter_z + force_saturn_z + force_uranus_z + force_neptune_z) * delta_time / sun.mass

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

# Celestial Body Tracks for simulation plot
mercury_x_data, mercury_y_data = [], []
venus_x_data, venus_y_data = [], []
earth_x_data, earth_y_data = [], []
mars_x_data, mars_y_data = [], []
jupiter_x_data, jupiter_y_data = [], []
saturn_x_data, saturn_y_data = [], []
uranus_x_data, uranus_y_data = [], []
neptune_x_data, neptune_y_data = [], []
sun_x_data, sun_y_data = [], []