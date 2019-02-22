import random
from microbit import *


cards = [
    Image.HAPPY,
    Image.HEART,
    Image.TRIANGLE,
    Image.DIAMOND,
    Image.RABBIT,
    Image.PACMAN,
    Image.DUCK,
    Image.HOUSE,
    Image.XMAS,
    Image.GHOST,
    Image.TORTOISE,
    Image.MUSIC_CROTCHET,
] * 2
assert len(cards) == 24

board = []
for row in range(5):
    for column in range(5):
        if row == 2 and column == 2:
            # We have an even number of cards - skip the middle LED
            board.append(None)
            continue
        image = cards.pop(random.randrange(0, len(cards)))
        card = {
            'image': image,
            'x': column,
            'y': row,
        }
        board.append(card)
controller = {
    'x': 2,
    'y': 2,
}

last_guess = None
matches = []
while True:
    a_press = button_a.was_pressed()
    b_press = button_b.was_pressed()
    if a_press and b_press:
        card = board[controller['y'] * 5 + controller['x']]
        if card:
            display.show(card['image'])
            sleep(1000)
            if last_guess:
                if last_guess != card and last_guess['image'] == card['image']:
                    for i in range(10):
                        display.clear()
                        sleep(50)
                        display.show(card['image'])
                        sleep(50)
                    matches.append(card['image'])
                last_guess = None
                controller['x'] = 2
                controller['y'] = 2
            else:
                last_guess = card
    elif a_press:
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
    for card in board:
        if not card:
            if controller['x'] != 2 or controller['y'] != 2:
                display.set_pixel(2, 2, 0)
        elif card['x'] != controller['x'] or card['y'] != controller['y']:
            if card['image'] not in matches:
                brightness = 1
            else:
                brightness = 0
            display.set_pixel(card['x'], card['y'], brightness)
    display.set_pixel(controller['x'], controller['y'], 9)
    sleep(100)