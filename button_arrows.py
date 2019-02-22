"""The microbit only has two buttons, but we can use combinations of presses for more actions.

In this example multiple presses of A and B are used to show arrows pointing in different
directions on the display.
"""
from microbit import *

BUTTONS_TO_ARROWS = {
    'AA': Image.ARROW_W,
    'AB': Image.ARROW_N,
    'BB': Image.ARROW_E,
    'BA': Image.ARROW_S,
}

pressed = []
while True:
    if button_a.was_pressed():
        pressed.append('A')
    elif button_b.was_pressed():
        pressed.append('B')

    if len(pressed) == 2:
        key = "".join(pressed)
        display.show(BUTTONS_TO_ARROWS[key])
        pressed = []