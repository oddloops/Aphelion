import tkinter as tk
from tkinter import ttk
import subprocess
import sys

from simulation_2d import *

planets = {
    "": 0,
    "Mercury": 0.5,
    "Venus": 0.7,
    "Earth": 1.05,
    "Mars": 2,
    "Jupiter": 8,
    "Saturn": 12,
    "Uranus": 25,
    "Neptune": 35
}

def on_select_planet():
    global selected_AU
    selected_value = select_planet_var.get()
    if selected_value:
        selected_AU = planets[selected_value]
        window.destroy()
        run_simulation_2d()

def run_simulation_2d():
    subprocess.run(["python", "src\simulation_2d.py"])

def on_close():
    sys.exit()

window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_close)  # Handle window close event
window.rowconfigure([0, 1], weight=1, minsize=50)
window.columnconfigure([0, 1], weight=1, minsize=75)

for i in range(2):
    for j in range(0, 2):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

select_planet_label = tk.Label(text="Select a planet:")
select_planet_label.grid(row=0, column=0, padx=5, pady=5)

select_planet_var = tk.StringVar()
select_planet_dropdown = ttk.OptionMenu(window, select_planet_var, *planets.keys())
select_planet_dropdown.grid(row=0, column=1, padx=5, pady=5)

select_planet_button_ok = tk.Button(text="OK!", command=on_select_planet)
select_planet_button_ok.grid(row=1, column=0, padx=5, pady=5)

select_planet_button_exit = tk.Button(text="Exit", command=on_close)
select_planet_button_exit.grid(row=1, column=1, padx=5, pady=5)
window.mainloop()
