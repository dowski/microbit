"""This program demonstrates a how you can use functions.

It builds on the previous idea of using a dictionary to represent a "sprite"
on the screen and adds functions to operate on the sprite. The functions can
be used to make, show, hide and move sprites.

If you run it on your micro:bit it will create a few sprites that move around
the screen randomly. They kind of look like little red ants.

"""
import random
from microbit import *

# It's normal to define constants at the top of your program. Here are
# a few that we'll use for sprite movement directions.
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

def make_sprite(x, y, brightness=9):
    """This function will return a new sprite given some x and y coordinates.

    You can optionally give it the brightness for the sprite too.

    """
    return {'x': x, 'y': y, 'brightness': brightness, 'direction': UP}

def show_sprite(sprite):
    """This shows the given sprite at its (x, y) coordinates on the microbit.

    """
    display.set_pixel(sprite['x'], sprite['y'], sprite['brightness'])

def hide_sprite(sprite):
    """This hides the given sprite so it no longer shows on the screen.

    """
    display.set_pixel(sprite['x'], sprite['y'], 0)

def move_sprite(sprite):
    """This function will move a sprite in its current direction.

    It's direction is stored using the aptly named 'direction' key. If moving
    would cause the sprite to move off of the screen, it will instead reverse
    its direction and not move until move_sprite is called again.

    """
    # WARNING: This is a long (and repetitive) function. It could definitely
    # be improved upon, but I wanted to not get too clever so that someone
    # just learning functions doesn't get confused.
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

# All of our functions have been defined - let's use them!

# Here we make one sprite in the middle of the screen. It's called always_on
# because later in the code we make it stay in place which leaves the LED
# turned on.
always_on = make_sprite(2, 2, 7)

# Now we'll use the same make_sprite function to make a few sprites in random
# locations on the screen.
random_sprites = []
for i in range(3):
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    random_sprites.append(make_sprite(x, y, 6))

# Now it's time to bring the sprites to life! We'll continually loop through
# the list of random_sprites and make each one move. We'll spice things up by
# randomly changing their directions some of the time.
while True:
    for sprite in random_sprites:
        move_sprite(sprite)
        if random.random() > 0.80:
            sprite['direction'] = DIRECTIONS[random.randrange(len(DIRECTIONS))]
    show_sprite(always_on)
    sleep(500)

# Here are some ideas if you want to change/improve this code:
# 1. Can you change how fast the sprites move?
# 2. Can you get rid of the boring idle sprite in the middle of the screen?
# 3. Can you change the number of randomly moving sprites?
# 4. Can you make each sprite start with a random direction instead of all
#    moving UP to begin with?
# 5. Can you make the sprites "warp" from one side of the screen to the other
#    instead of "bouncing" off of the edge?
# 6. Can you make the big move_sprite function less repetitive? Hint: try
#    splitting it up into a few other functions.
# 7. Can you add some interactivity (via buttons, shaking, etc.)? Maybe allow
#    for adding new sprites, changing how they move or adding your own sprite
#    that you control.