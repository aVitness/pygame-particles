import random
import time
from typing import Callable, Union

import pygame

from .shape import Point, Shape, Square


def rand_number(nrange: Union[Union[int, float], tuple[Union[int, float], Union[int, float]]]) -> Union[int, float]:
    if isinstance(nrange, (int, float)):
        return nrange
    a, b = nrange
    if isinstance(a, int) and isinstance(b, int):
        return random.randint(a, b)
    return random.random() * (b - a) + a


class State:
    """
    Particle's states
    :param alive: 0
    :param fading: 1
    :param dead: 2
    """
    alive = 0
    fading = 1
    dead = 2


class Particle:
    """
    A class representing Particle group object.

    :param shape_cls: Particle's shape class
    :param center_x: X center coordinate position
    :param center_y: Y center coordinate position
    :param objects_count: Count of particle parts
    :param life_seconds: After that amount of seconds particle will turn into fading
    :param fade_seconds: After that amount of seconds particle will turn into dead
    :param life_iterations: After that amount of iterations particle will turn into fading
    :param fade_iterations: After that amount of iterations particle will turn into dead
    :param color: Default pygame color or a function, that takes particle and shape object and returns color
    :param size: Object size range
    :param speed: Move speed range
    :param rotate_angle: Rotate angle range
    :param width: Pygame drawing width, 0 = filled
    """

    def __init__(self,
                 center_x: int,
                 center_y: int,
                 objects_count: int = 10,
                 life_seconds: float = None,
                 fade_seconds: float = None,
                 life_iterations: int = None,
                 fade_iterations: int = None,
                 color: pygame.Color | Callable = "white",
                 size: Union[Union[int, float], tuple[Union[int, float], Union[int, float]]] = 3,
                 speed: Union[Union[int, float], tuple[Union[int, float], Union[int, float]]] = 1,
                 rotate_angle: Union[Union[int, float], tuple[Union[int, float], Union[int, float]]] = 0,
                 width: int = 0,
                 shape_cls: type = Square,
                 ):
        self.objects_count = objects_count
        self.size_range = size
        self.speed_range = speed
        self.center = Point(center_x, center_y)
        self.life_seconds = life_seconds
        self.fade_seconds = fade_seconds
        self.life_iterations = life_iterations
        self.fade_iterations = fade_iterations
        self.color = color
        self.rotate_angle_range = rotate_angle
        self.shape_cls = shape_cls
        self.objects: list[Shape] = [
            shape_cls(
                Point(center_x, center_y),
                rand_number(size),
                rand_number(speed)
            )
            for _ in range(objects_count)
        ]
        self.width = width
        self.start_time = time.time()
        self.iterations = 0
        self.state = State.alive

    @property
    def percent_completed(self):
        """
        Returns current complete percent [0; 100]
        """
        percents = []
        if self.state == State.alive and self.life_seconds:
            percents.append((time.time() - self.start_time) / self.life_seconds * 100)
        if self.state == State.alive and self.life_iterations:
            percents.append(self.iterations / self.life_iterations * 100)
        if self.state == State.fading and self.fade_seconds:
            percents.append((time.time() - self.start_time) / self.fade_seconds * 100)
        if self.state == State.fading and self.fade_iterations:
            percents.append(self.iterations / self.fade_iterations * 100)
        return min(100, max(0, max(percents, default=100)))

    def is_dead(self):
        """
        Check if particle is dead
        """
        return self.state == State.dead

    def update(self):
        """
        One particle update iteration
        """
        if self.is_dead():
            return
        self.iterations += 1
        for obj in self.objects:
            if self.rotate_angle_range:
                obj.rotate(rand_number(self.rotate_angle_range))
            obj.move()
        if self.percent_completed >= 100:
            self.state += 1
            self.iterations = 0
            self.start_time = time.time()

    def draw(self, screen):
        """
        Draw particle on the screen
        """
        if self.is_dead():
            return
        for obj in self.objects:
            color = self.color
            if callable(self.color):
                color = self.color(self, obj)
            obj.draw(screen, color, self.width)

    def __getitem__(self, item):
        return self.objects[item]

    def __iter__(self):
        return iter(self.objects)
