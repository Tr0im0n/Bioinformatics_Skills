"""
Author: Tom Van Wersch
Date: 13-05-2024
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from scipy.integrate import odeint


def plants_hare_lynx(y, t, a1, a2, b1, b2, d1, d2):
    """Used differential equations"""
    # Unpack y into individual variables for readability
    y1, y2, y3 = y
    # Calculate intermediate values
    ratio = 10
    grass_eaten_by_hares = a1 * y1 * y2 / (1 + b1 * y1)
    hares_eaten_by_lynx = a2 * y2 * y3 / (1 + b2 * y2)
    grass_grown = y1 * (1 - y1)
    hares_died = d1 * y2
    lynx_died = d2 * y3
    # Compute the derivatives
    dydt0 = grass_grown - grass_eaten_by_hares
    dydt1 = grass_eaten_by_hares - hares_died - hares_eaten_by_lynx * ratio
    dydt2 = hares_eaten_by_lynx - lynx_died
    # Return the derivatives as a numpy array
    return np.array([dydt0, dydt1, dydt2])


def get_slider_axes(n: int = 9):
    """create list of sliders"""
    return [plt.axes((0.05, 0.9 - i * 0.08, 0.35, 0.05)) for i in range(n)]


def simulate_outside(ax, slider_list, time_points):
    """ Takes the values from the 9 sliders, \n
        solves the system of ODE's, \n
        clears and makes the new plot."""
    print("Called")
    y0 = tuple(slider.val for slider in slider_list[:3])
    args = tuple(slider.val for slider in slider_list[3:])
    y_solved = odeint(plants_hare_lynx, y0, time_points, args=args)
    ax.clear()
    ax.plot(time_points, y_solved, label=("Grass", "Hares", "Lynx"))
    ax.grid()
    ax.legend()
    plt.draw()


def main():
    # Make plot
    fig, ax = plt.subplots(1, 1, figsize=(16, 9))
    plt.subplots_adjust(left=0.5, right=0.98)
    # Make sliders
    slider_axes = get_slider_axes(9)
    grass_slider = Slider(slider_axes[0], "Grass", 0.1, 1, valinit=0.8, valstep=0.1)
    hares_slider = Slider(slider_axes[1], "Hares", 0.1, 1, valinit=0.2, valstep=0.1)
    lynx_slider = Slider(slider_axes[2], "Lynx", 0.4, 1.2, valinit=0.8, valstep=0.1)

    a1_slider = Slider(slider_axes[3], "a1", 1, 10, valinit=5, valstep=1)
    a2_slider = Slider(slider_axes[4], "a2", 0.05, 0.45, valinit=0.1, valstep=0.05)
    b1_slider = Slider(slider_axes[5], "b1", 1, 10, valinit=3, valstep=1)
    b2_slider = Slider(slider_axes[6], "b2", 1, 10, valinit=2, valstep=1)
    d1_slider = Slider(slider_axes[7], "d1", 0.2, 0.6, valinit=0.4, valstep=0.05)
    d2_slider = Slider(slider_axes[8], "d2", 0.005, 0.015, valinit=0.01, valstep=0.001)
    slider_list = [grass_slider, hares_slider, lynx_slider,
                   a1_slider, a2_slider, b1_slider, b2_slider, d1_slider, d2_slider]

    time_points = np.arange(200)

    def on_button_clicked(event):
        simulate_outside(ax, slider_list, time_points)

    # Make button
    button_ax = plt.axes((0.2, 0.05, 0.2, 0.1))
    button = Button(button_ax, "Simulate [space]")
    button.on_clicked(on_button_clicked)

    # Make it also simulate on pressing space
    def on_key_press(event):
        if event.key == ' ':
            simulate_outside(ax, slider_list, time_points)
    fig.canvas.mpl_connect('key_press_event', on_key_press)

    simulate_outside(ax, slider_list, time_points)
    plt.show()


if __name__ == "__main__":
    main()


# The following are unused functions


def phl_tom(t, y, m1, m2, h1, h2, d1, d2):
    """This is not used!"""
    y0, y1, y2 = y
    # Calculate intermediate values
    term1 = m1 * y0 * y1 / (h1 + y0)
    term2 = m2 * y1 * y2 / (h2 + y1)
    # Compute the derivatives
    dydt0 = y0 * (1 - y0) - term1
    dydt1 = term1 - term2 - d1 * y1
    dydt2 = term2 - d2 * y2
    # Return the derivatives as a numpy array
    return np.array([dydt0, dydt1, dydt2])


def test1():
    """Also not used"""
    slider_axes = get_slider_axes(6)
    m1_slider = Slider(slider_axes[0], "m1", 1, 9, valinit=5, valstep=1)
    m2_slider = Slider(slider_axes[1], "m2", 1, 9, valinit=5, valstep=1)
    h1_slider = Slider(slider_axes[2], "h1", 1, 9, valinit=5, valstep=1)
    h2_slider = Slider(slider_axes[3], "h2", 1, 9, valinit=5, valstep=1)
    d1_slider = Slider(slider_axes[4], "d1", 1, 9, valinit=5, valstep=1)
    d2_slider = Slider(slider_axes[5], "d2", 1, 9, valinit=5, valstep=1)
