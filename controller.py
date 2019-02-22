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