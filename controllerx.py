"""A simple controller that moves across the X-axis at the bottom of the display.

Use the A and B buttons to move.

When the edge is reached, it doesn't move further.
"""
import random
from microbit import *

controller = {
    'x': 2,
    'y': 4,
}

while True:
    a_press = button_a.was_pressed()
    b_press = button_b.was_pressed()
    if a_press or b_press:
        display.set_pixel(controller['x'], controller['y'], 0)
    if a_press:
        if controller['x'] > 0:
            controller['x'] -= 1
    elif b_press:
        if controller['x'] < 4:
            controller['x'] += 1
    display.set_pixel(controller['x'], controller['y'], 9)
    sleep(100)