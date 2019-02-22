from microbit import display
from microbit import sleep
from microbit import button_a, button_b


effects = 1


while True:
    display.clear()
    effects -= button_a.get_presses()
    effects += button_b.get_presses()
    if effects > 0:
        for i in range(10):
            display.set_pixel(2, 2, i)
            sleep(10)
    if effects > 1:
        for i in range(4,10):
            display.set_pixel(2, 1, i)
            display.set_pixel(2, 3, i)
            display.set_pixel(1, 2, i)
            display.set_pixel(3, 2, i)
            sleep(20)
    if effects > 2: 
        for i in range(2,10):
            display.set_pixel(1, 1, i)
            display.set_pixel(3, 1, i)
            display.set_pixel(1, 3, i)
            display.set_pixel(3, 3, i)
            display.set_pixel(2, 2, 9-i)
            sleep(20)
    if effects > 3:
        for i in range(9,-1, -1):
            display.set_pixel(0, 0, i)
            display.set_pixel(2, 0, i)
            display.set_pixel(0, 2, i)
            display.set_pixel(2, 4, i)
            display.set_pixel(4, 2, i)
            display.set_pixel(4, 0, i)
            display.set_pixel(0, 4, i)
            display.set_pixel(4, 4, i)
            sleep(40)
    if effects > 4:
        for i in range(2, 10):
            display.set_pixel(2, 1, 9-i)
            display.set_pixel(2, 3, 9-i)
            display.set_pixel(1, 2, 9-i)
            display.set_pixel(3, 2, 9-i)
            sleep(40)