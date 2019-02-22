from microbit import sleep
from microbit import display


LEFT = 0
RIGHT = 1


def swish(direction):
    ostart = 0 if direction == RIGHT else 5
    oend = 9 if direction == RIGHT else -5
    step = 1 if direction == RIGHT else -1
    istart = 1 if direction == RIGHT else 3
    iend = 4 if direction == RIGHT else -1
    for i in range(ostart, oend, step):
        display.clear()
        if -1 < i < 5:
            display.set_pixel(i, 2, 9)
        for j in range(istart, iend, step):
            k = i - j * step
            brightness = 9 - (2 * j)
            if 5 > k >= 0:
                display.set_pixel(k, 2, brightness)
        sleep(100)


while True:
    swish(RIGHT)
    sleep(200)
    swish(LEFT)
    sleep(200)