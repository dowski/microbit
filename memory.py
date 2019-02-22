"""A memory/matching game.

Use A and B to move around the screen. Press A+B together to see a card. Try and find
matches.

The code purposely only uses lists and dictionaries as its most advanced data structures.

It's also incomplete in a number of ways - feel free to make changes and see if you can
improve it!
"""
import random
from microbit import *


# Feel free to change the images used in the game. You should have 12 here, and you can
# see after the end ] below the list is "doubled" which makes a copy of each image.
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
# This line helps ensure that we have the right number of cards and didn't make a mistake. If
# there are more or less than 24 the program will crash and we'll know there's a problem.
assert len(cards) == 24

# This code populates the board. It loops over the rows and columns of LEDs on the screen
# and places a card at each X and Y position (excluding the very middle since we need an
# even number of cards).
board = []
for row in range(5):
    for column in range(5):
        if row == 2 and column == 2:
            # We have an even number of cards - skip the middle LED
            board.append(None)
            continue
        image = cards.pop(random.randrange(0, len(cards)))
        # A dictionary is useful for representing a card. We can keep all of the data about
        # it together and reference it by useful names (kind of like variables).
        card = {
            'image': image,
            'x': column,
            'y': row,
        }
        board.append(card)

# This will represent the controller that we move around on the display.
controller = {
    'x': 2,
    'y': 2,
}

# Now that the board is setup, here's where the game actually runs!

# We keep a variable with the last guess that the player made. To start with we assign it
# the special value of None which means ... nothing.
last_guess = None

# This list will keep the matching cards that the player has found. We'll use that to
# know which LEDs to turn off when showing the board on the display.
matches = []
while True:
    # Button presses control the game! The game is constantly looping and checking if there
    # were button presses. When it finds them, it does different things.
    a_press = button_a.was_pressed()
    b_press = button_b.was_pressed()

    # First we handle if A and B were both pressed. It's important to do this first because
    # checking if either button was pressed individually would hide the fact that both were
    # pressed together.
    if a_press and b_press:
        # Here we do a bit of math to find the card that matches the (x,y) position of the
        # controller. Can you figure out why it works?
        card = board[controller['y'] * 5 + controller['x']]
        # We check and make sure a card was found. When might that be false?
        if card:
            # Now we show the image for the card so the player can remember it.
            display.show(card['image'])
            sleep(1000)
            # If the player had already made a guess, now we compare it with the card
            # that they just chose. Otherwise we assign the card they just chose to last_guess.
            if last_guess:
                # We check that they aren't guessing the same card in the same spot and then
                # check and see if the images match.
                if last_guess != card and last_guess['image'] == card['image']:
                    # Hooray, a match - flash the display in excitement and add it to the
                    # matches list.
                    for i in range(10):
                        display.clear()
                        sleep(50)
                        display.show(card['image'])
                        sleep(50)
                    matches.append(card['image'])
                # Whether they were right or not, reset the last guess and controller positions
                # so they can try to find another pair of matches.
                last_guess = None
                controller['x'] = 2
                controller['y'] = 2
            else:
                last_guess = card
    # The A and B button handling below are similar. They handle moving progressively through
    # all of the cards on the board. Can you figure out how it works?
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

    # All of the button handling is done. Maybe some new matches were found, maybe the
    # controller was moved. We update all of the LEDs based on the state of the board and
    # the matches that have been found so far.
    for card in board:
        if not card:
            # This is the no-card position - unless the controller is here it should be turned
            # off (brightness == 0).
            if controller['x'] != 2 or controller['y'] != 2:
                display.set_pixel(2, 2, 0)
        elif card['x'] != controller['x'] or card['y'] != controller['y']:
            # Now we light up the positions of the cards, so long as the controller doesn't
            # have the same (x,y) coordinates. If a card has been matched already, it's LED
            # is turned off.
            if card['image'] not in matches:
                brightness = 1
            else:
                brightness = 0
            display.set_pixel(card['x'], card['y'], brightness)
    # Finally we light up the controller nice and bright and sleep briefly to allow time to
    # capture button presses.
    display.set_pixel(controller['x'], controller['y'], 9)
    sleep(100)