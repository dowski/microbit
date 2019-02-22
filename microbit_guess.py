import random
from microbit import *

SECRET_SIZE = 5

SECRET = []

for i in range(SECRET_SIZE):
    SECRET.append(random.choice("ab"))

guess = []
tries = 0

display.show(Image.MEH)

while True:
    if button_a.was_pressed():
        guess.append("a")
    if button_b.was_pressed():
        guess.append("b")

    if len(guess) == SECRET_SIZE:
        tries += 1
        correct = []
        for guess_letter, secret_letter in zip(guess, SECRET):
            if guess_letter == secret_letter:
                correct.append(guess_letter)
            else:
                break
        if len(correct) == SECRET_SIZE:
            break
        elif len(correct) == 0:
            display.show(Image.SAD)
        else:
            display.scroll("".join(correct))
        guess = []
display.scroll("YOU WON IN " + str(tries) + " TRIES")
display.show(Image.HAPPY)