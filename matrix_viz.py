# An animation sort of like the Matrix from ... the Matrix
# Press A to add more particles, B to remove them

import random
from microbit import display
from microbit import button_a, button_b
from microbit import sleep


MAX_PARTICLES = 15
MAX_NEW_PARTICLES = 3
MAX_Y = 4
MAX_X = 4
MIN_SPEED = 1
MAX_SPEED = 9


class FallingParticle:
    def __init__(self, speed, x):
        self.speed = speed
        self.x = x
        self.y = 0
        self.brightness = speed
        self.age = 0

    def drop(self):
        if self.speed > random.randint(0, MAX_SPEED - 1):
            self.y += 1

class Animator:
    def __init__(self):
        self.particles = []
        self.max_particles = 1

    def generate(self, requested=0):
        particle_count = len(self.particles)
        self.max_particles = max(requested + self.max_particles, 0)
        if self.max_particles > 0:
            new_particle_count = self.max_particles - particle_count
            for i in range(new_particle_count):
                particle = FallingParticle(
                        random.randint(MIN_SPEED, MAX_SPEED),
                        random.randint(0, MAX_X))
                self.particles.append(particle)

    def render(self):
        display.clear()
        for particle in self.particles:
            display.set_pixel(particle.x, particle.y, particle.brightness)

    def advance(self):
        for particle in self.particles[:]:
            particle.drop()
            if particle.y > MAX_Y:
                self.particles.remove(particle)

animator = Animator()
while True:
    animator.generate(requested=button_a.get_presses() - button_b.get_presses())
    animator.render()
    animator.advance()
    sleep(100)