import matplotlib.pyplot as plt
from matplotlib import animation

from simulation_setup import *

# Grab and animate the simulation
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.grid()

# Earth object
earth_color = "#2C7BB6"  # hex code for greenish blue
line_earth, = ax.plot([], [], '-', lw=1, color="blue")
point_earth, = ax.plot([], [], marker="o", markersize=6, markeredgecolor=earth_color, markerfacecolor=earth_color)
text_earth = ax.text(earth_aphelion, 0, 'Earth')

# Sun object
sun_color = "#F4F71C"  # hex code for yellow-orange
point_sun, = ax.plot([], [], marker="o", markersize=18, markeredgecolor=sun_color, markerfacecolor=sun_color)
text_sun = ax.text(0, 0, 'Sun')

# Celestial Body Tracks
earth_x_data, earth_y_data = [], []
sun_x_data, sun_y_data = [], []

def update(i):
    earth_x_data.append(earth_x_list[i])
    earth_y_data.append(earth_y_list[i])
    
    line_earth.set_data(earth_x_data, earth_y_data)
    point_earth.set_data(earth_x_list[i:i+1], earth_y_list[i:i+1])
    text_earth.set_position((earth_x_list[i], earth_y_list[i]))

    point_sun.set_data(sun_x_list[i:i+1], sun_y_list[i:i+1])
    text_sun.set_position((sun_x_list[i], sun_y_list[i]))

    ax.axis('equal')
    ax.set_xlim(-2 * earth_aphelion, 2 * earth_aphelion)
    ax.set_ylim(-2 * earth_aphelion, 2 * earth_aphelion)

    return line_earth, point_sun, point_earth, text_earth, text_sun

anim = animation.FuncAnimation(fig, func=update, frames=len(earth_x_list), interval=1, blit=True)
plt.show()
