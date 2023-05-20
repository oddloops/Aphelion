import matplotlib.pyplot as plt
from matplotlib import animation

from simulation_setup import *
from simulation_select import *

# Grab and animate the simulation
fig, ax = plt.subplots(figsize=(12, 8))
fig.canvas.manager.set_window_title('Aphelion')
fig.suptitle('Solar System Simulation', y = 0.9)

ax.set_aspect('equal')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.grid()

# Mercury object
mercury_color = "#808080"
line_mercury, = ax.plot([], [], '-', lw=1, color=mercury_color)
point_mercury, = ax.plot([], [], marker="o", markersize=3, markeredgecolor=mercury_color, markerfacecolor=mercury_color)
text_mercury = ax.text(mercury.aphelion, 0, 'Mercury')

# Venus object
venus_color = "#DDBA7D"
line_venus, = ax.plot([], [], '-', lw=1, color=venus_color)
point_venus, = ax.plot([], [], marker="o", markersize=5, markeredgecolor=venus_color, markerfacecolor=venus_color)
text_venus = ax.text(venus.aphelion, 0, 'Venus')

# Earth object
earth_color = "#2C7BB6"  # hex code for greenish blue
line_earth, = ax.plot([], [], '-', lw=1, color="blue")
point_earth, = ax.plot([], [], marker="o", markersize=6, markeredgecolor=earth_color, markerfacecolor=earth_color)
text_earth = ax.text(earth.aphelion, 0, 'Earth')

# Mars object
mars_color = "#FF0000"
line_mars, = ax.plot([], [], '-', lw=1, color=mars_color)
point_mars, = ax.plot([], [], marker="o", markersize=4, markeredgecolor=mars_color, markerfacecolor=mars_color)
text_mars = ax.text(mars.aphelion, 0, 'Mars')

# Jupiter object
jupiter_color = "#FF4500"
line_jupiter, = ax.plot([], [], '-', lw=1, color=jupiter_color)
point_jupiter, = ax.plot([], [], marker="o", markersize=8, markeredgecolor=jupiter_color, markerfacecolor=jupiter_color)
text_jupiter = ax.text(jupiter.aphelion, 0, 'Jupiter')

# Saturn object
saturn_color = "#FFD700"
line_saturn, = ax.plot([], [], '-', lw=1, color=saturn_color)
point_saturn, = ax.plot([], [], marker="o", markersize=8, markeredgecolor=saturn_color, markerfacecolor=saturn_color)
text_saturn = ax.text(saturn.aphelion, 0, 'Saturn')

# Uranus object
uranus_color = "#00FFFF"
line_uranus, = ax.plot([], [], '-', lw=1, color=uranus_color)
point_uranus, = ax.plot([], [], marker="o", markersize=8, markeredgecolor=uranus_color, markerfacecolor=uranus_color)
text_uranus = ax.text(uranus.aphelion, 0, 'Uranus')

# Neptune object
neptune_color = "#0000FF"
line_neptune, = ax.plot([], [], '-', lw=1, color=neptune_color)
point_neptune, = ax.plot([], [], marker="o", markersize=8, markeredgecolor=neptune_color, markerfacecolor=neptune_color)
text_neptune = ax.text(neptune.aphelion, 0, 'Neptune')

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

    uranus_x_data.append(uranus_x_list[i])
    uranus_y_data.append(uranus_y_list[i])

    neptune_x_data.append(neptune_x_list[i])
    neptune_y_data.append(neptune_y_list[i])

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

    line_uranus.set_data(uranus_x_data, uranus_y_data)
    point_uranus.set_data(uranus_x_list[i:i+1], uranus_y_list[i:i+1])
    text_uranus.set_position((uranus_x_list[i], uranus_y_list[i]))

    line_neptune.set_data(neptune_x_data, neptune_y_data)
    point_neptune.set_data(neptune_x_list[i:i+1], neptune_y_list[i:i+1])
    text_neptune.set_position((neptune_x_list[i], neptune_y_list[i]))

    point_sun.set_data(sun_x_list[i:i+1], sun_y_list[i:i+1])
    text_sun.set_position((sun_x_list[i], sun_y_list[i]))

    ax.axis('equal')
    ax.set_xlim(-selected_AU * AU, selected_AU * AU)
    ax.set_ylim(-selected_AU * AU, selected_AU * AU)

    return line_mercury, line_venus, line_earth, line_mars, line_jupiter, line_saturn, line_uranus, line_neptune, \
           point_sun, point_mercury, point_venus, point_earth, point_mars, point_jupiter, point_saturn, point_uranus, point_neptune, \
           text_sun, text_mercury, text_venus, text_earth, text_mars, text_jupiter, text_saturn, text_uranus, text_neptune


# box = ax.get_position()
# ax.set_position([box.x0, box.y0 + box.height * 0.1,
#                  box.width, box.height * 0.9])
ax.legend(
    [point_sun, point_mercury, point_venus, point_earth, point_mars, point_jupiter, point_saturn, point_uranus, point_neptune], 
    ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
    loc='center left',
    bbox_to_anchor=(1, 0.84),
    fancybox=True, 
    shadow=True, 
)
anim = animation.FuncAnimation(fig, func=update, frames=len(earth_x_list), interval=1, blit=True)

plt.show()