from pygame_particles import Shape


class CustomShape(Shape):
    def __init__(self, center, radius, speed):
        super().__init__(center, [(-10, 0), (0, -10), (10, 0), (0, 10)], speed)
