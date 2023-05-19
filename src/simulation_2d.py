import matplotlib.pyplot as plt
from matplotlib import animation

from simulation_setup import *

# Grab and animate the simulation
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.grid()

# Mercury object
line_mercury, = ax.plot([], [], '-', lw=1, color="brown")
point_mercury, = ax.plot([], [], marker="o", markersize=3, markeredgecolor="brown", markerfacecolor="brown")
text_mercury = ax.text(mercury.aphelion, 0, 'Mercury')

# Venus object
line_venus, = ax.plot([], [], '-', lw=1, color="pink")
point_venus, = ax.plot([], [], marker="o", markersize=5, markeredgecolor="pink", markerfacecolor="pink")
text_venus = ax.text(venus.aphelion, 0, 'Venus')

# Earth object
earth_color = "#2C7BB6"  # hex code for greenish blue
line_earth, = ax.plot([], [], '-', lw=1, color="blue")
point_earth, = ax.plot([], [], marker="o", markersize=6, markeredgecolor=earth_color, markerfacecolor=earth_color)
text_earth = ax.text(earth.aphelion, 0, 'Earth')

# Mars object
line_mars, = ax.plot([], [], '-', lw=1, color="red")
point_mars, = ax.plot([], [], marker="o", markersize=4, markeredgecolor="red", markerfacecolor="red")
text_mars = ax.text(mars.aphelion, 0, 'Mars')

# Jupiter object
line_jupiter, = ax.plot([], [], '-', lw=1, color="red")
point_jupiter, = ax.plot([], [], marker="o", markersize=8, markeredgecolor="red", markerfacecolor="red")
text_jupiter = ax.text(jupiter.aphelion, 0, 'Jupiter')

# Saturn object
line_saturn, = ax.plot([], [], '-', lw=1, color="purple")
point_saturn, = ax.plot([], [], marker="o", markersize=8, markeredgecolor="purple", markerfacecolor="purple")
text_saturn = ax.text(saturn.aphelion, 0, 'Saturn')

# Sun object
sun_color = "#F4F71C"  # hex code for yellow-orange
point_sun, = ax.plot([], [], marker="o", markersize=16, markeredgecolor=sun_color, markerfacecolor=sun_color)
text_sun = ax.text(0, 0, 'Sun')

def update(i):
    mercury_x_data.append(mercury_x_list[i])
    mercury_y_data.append(mercury_y_list[i])

    venus_x_data.append(venus_x_list[i])
    venus_y_data.append(venus_y_list[i])

    earth_x_data.append(earth_x_list[i])
    earth_y_data.append(earth_y_list[i])

    mars_x_data.append(mars_x_list[i])
    mars_y_data.append(mars_y_list[i])
    
    jupiter_x_data.append(jupiter_x_list[i])
    jupiter_y_data.append(jupiter_y_list[i])

    saturn_x_data.append(saturn_x_list[i])
    saturn_y_data.append(saturn_y_list[i])

    line_mercury.set_data(mercury_x_data, mercury_y_data)
    point_mercury.set_data(mercury_x_list[i:i+1], mercury_y_list[i:i+1])
    text_mercury.set_position((mercury_x_list[i], mercury_y_list[i]))

    line_venus.set_data(venus_x_data, venus_y_data)
    point_venus.set_data(venus_x_list[i:i+1], venus_y_list[i:i+1])
    text_venus.set_position((venus_x_list[i], venus_y_list[i]))

    line_earth.set_data(earth_x_data, earth_y_data)
    point_earth.set_data(earth_x_list[i:i+1], earth_y_list[i:i+1])
    text_earth.set_position((earth_x_list[i], earth_y_list[i]))

    line_mars.set_data(mars_x_data, mars_y_data)
    point_mars.set_data(mars_x_list[i:i+1], mars_y_list[i:i+1])
    text_mars.set_position((mars_x_list[i], mars_y_list[i]))

    line_jupiter.set_data(jupiter_x_data, jupiter_y_data)
    point_jupiter.set_data(jupiter_x_list[i:i+1], jupiter_y_list[i:i+1])
    text_jupiter.set_position((jupiter_x_list[i], jupiter_y_list[i]))

    line_saturn.set_data(saturn_x_data, saturn_y_data)
    point_saturn.set_data(saturn_x_list[i:i+1], saturn_y_list[i:i+1])
    text_saturn.set_position((saturn_x_list[i], saturn_y_list[i]))

    point_sun.set_data(sun_x_list[i:i+1], sun_y_list[i:i+1])
    text_sun.set_position((sun_x_list[i], sun_y_list[i]))

    ax.axis('equal')
    ax.set_xlim(-12 * AU, 12 * AU)
    ax.set_ylim(-12 * AU, 12 * AU)

    return line_mercury, line_venus, line_earth, line_mars, line_jupiter, line_saturn, \
           point_sun, point_mercury, point_venus, point_earth, point_mars, point_jupiter, point_saturn, \
           text_sun, text_mercury, text_venus, text_earth, text_mars, text_jupiter, text_saturn

anim = animation.FuncAnimation(fig, func=update, frames=len(earth_x_list), interval=1, blit=True)
plt.show()