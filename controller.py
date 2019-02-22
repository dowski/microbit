"""An example of a controller that can be moved around the microbit display.

Use the A and B buttons to move.

When moving left, if it reaches the edge of the screen it moves up a row and over
to the right. If moving right, if it reaches the edge it moves down a row and over
to the left. It also wraps when it reaches the top/bottom of the screen.
"""
from microbit import *

controller = {
    'x': 2,
    'y': 2,
}

while True:
    a_press = button_a.was_pressed()
    b_press = button_b.was_pressed()
    if a_press or b_press:
        display.set_pixel(controller['x'], controller['y'], 0)
    if a_press:
        if controller['x'] == 0:
            controller['x'] = 4
            if controller['y'] == 0:
                controller['y'] = 4
            else:
                controller['y'] -= 1
        else:
            controller['x'] -= 1
    elif b_press:
        if controller['x'] == 4:
            controller['x'] = 0
            if controller['y'] == 4:
                controller['y'] = 0
            else:
                controller['y'] += 1
        else:
            controller['x'] += 1
    display.set_pixel(controller['x'], controller['y'], 9)
    sleep(100)