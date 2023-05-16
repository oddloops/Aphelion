from models.Planet import Planet
from models.Star import Star
from utils.Physics import Physics

# Celestial Bodies
earth = Planet(5.972e24, 6.371e6)
sun = Star(1.989e30, 6.957e8, 3.828e+29, 5773.15)

# Constants for Earth Sun
average_earth_sun_distance = 1.496e11
earth_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, earth.mass, average_earth_sun_distance)
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

sun_x_list, sun_y_list, sun_z_list = [], [], []
earth_x_list, earth_y_list, earth_z_list = [], [], []

# Start simulation
while time < 1 * 364 * Physics.days_in_secs:
    ###### The Earth #######
    # For Earth, compute G force on Earth
    radius_x, radius_y, radius_z = earth_x - sun_x, earth_y - sun_y, earth_z - sun_z
    mag_vector_3 = (radius_x ** 2 + radius_y ** 2 + radius_z ** 2) ** 1.5
    force_earth_x = -earth_gravitational_constant * radius_x / mag_vector_3
    force_earth_y = -earth_gravitational_constant * radius_y / mag_vector_3
    force_earth_z = -earth_gravitational_constant * radius_z / mag_vector_3

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

print(earth_x_list)

import matplotlib.pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots(figsize=(10,10))
ax.set_aspect('equal')
ax.grid()

line_e,     = ax.plot([],[],'-g',lw=1,c='blue')
point_e,    = ax.plot([earth_aphelion], [0], marker="o"
                      , markersize=4
                      , markeredgecolor="blue"
                      , markerfacecolor="blue")
text_e      = ax.text(earth_aphelion,0,'Earth')

point_s,    = ax.plot([0], [0], marker="o"
                      , markersize=7
                      , markeredgecolor="yellow"
                      , markerfacecolor="yellow")
text_s      = ax.text(0,0,'Sun')

exdata,eydata = [],[]                   # earth track
sxdata,sydata = [],[]                   # sun track

def update(i):
    exdata.append(earth_x_list[i])
    eydata.append(earth_y_list[i])
    
    line_e.set_data(exdata,eydata)
    point_e.set_data(earth_x_list[i],earth_y_list[i])
    text_e.set_position((earth_x_list[i],earth_y_list[i]))

    point_s.set_data(sun_x_list[i],sun_y_list[i])
    text_s.set_position((sun_x_list[i],sun_y_list[i]))

    ax.axis('equal')
    ax.set_xlim(-2*earth_aphelion,2*earth_aphelion)
    ax.set_ylim(-2*earth_aphelion,2*earth_aphelion)

    return line_e,point_s,point_e,text_e,text_s

anim = animation.FuncAnimation(fig
                                ,func=update
                                ,frames=len(earth_x_list)
                                ,interval=1
                                ,blit=True)
plt.show()