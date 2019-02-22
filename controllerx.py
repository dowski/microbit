import random
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
        new_y = controller['y'] + random.randint(-1, 1)
        if -1 < new_y < 5:
            controller['y'] = new_y
    if a_press:
        if controller['x'] > 0:
            controller['x'] -= 1
    elif b_press:
        if controller['x'] < 4:
            controller['x'] += 1
    display.set_pixel(controller['x'], controller['y'], 9)
    sleep(100)