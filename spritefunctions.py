import random
from microbit import *

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

def make_sprite(x, y, brightness=9):
    return {'x': x, 'y': y, 'brightness': brightness, 'direction': UP}

def show_sprite(sprite):
    display.set_pixel(sprite['x'], sprite['y'], sprite['brightness'])

def hide_sprite(sprite):
    display.set_pixel(sprite['x'], sprite['y'], 0)

def move_sprite(sprite):
    if sprite['direction'] == UP:
        if sprite['y'] == 0:
            sprite['direction'] = DOWN
        else:
            hide_sprite(sprite)
            sprite['y'] -= 1
            show_sprite(sprite)
    elif sprite['direction'] == DOWN:
        if sprite['y'] == 4:
            sprite['direction'] = UP
        else:
            hide_sprite(sprite)
            sprite['y'] += 1
            show_sprite(sprite)
    elif sprite['direction'] == LEFT:
        if sprite['x'] == 0:
            sprite['direction'] = RIGHT
        else:
            hide_sprite(sprite)
            sprite['x'] -= 1
            show_sprite(sprite)
    elif sprite['direction'] == RIGHT:
        if sprite['x'] == 4:
            sprite['direction'] = LEFT
        else:
            hide_sprite(sprite)
            sprite['x'] += 1
            show_sprite(sprite)

always_on = make_sprite(2, 2, 7)

random_sprites = []

for i in range(3):
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    random_sprites.append(make_sprite(x, y, 6))

while True:
    for sprite in random_sprites:
        move_sprite(sprite)
        if random.random() > 0.80:
            sprite['direction'] = DIRECTIONS[random.randrange(len(DIRECTIONS))]
    show_sprite(always_on)
    sleep(500)