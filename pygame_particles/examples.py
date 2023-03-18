import random
import pygame
from .shape import *
from .particle import Particle
from .container import ParticleContainer

def white_cubes_color(particle: Particle, shape: Shape) -> pygame.Color:
    if particle.state == 0:
        return "white"
    return tuple([255 * (100 - particle.percent_completed) / 100] * 3)


white_cubes = Particle(
    center_x=1280 / 6,
    center_y=720 / 4,
    life_seconds=0.6,
    fade_seconds=1,
    speed=(1, 2),
    shape_cls=Square,
    size=(5, 25),
    color=white_cubes_color
)


def sunflowers_color(particle: Particle, shape: Shape) -> pygame.Color:
    return random.choice(
        [(250, 250, 110), (250, 247, 106), (251, 244, 102), (251, 241, 99), (251, 238, 95), (251, 236, 91), (252, 233, 88), (252, 230, 84),
         (252, 227, 81), (253, 224, 77), (253, 221, 74), (253, 218, 70), (253, 215, 67), (254, 212, 64), (254, 209, 60), (254, 206, 57),
         (254, 203, 54), (254, 200, 50), (255, 196, 47), (255, 193, 44), (255, 190, 41), (255, 187, 38), (255, 184, 35), (255, 181, 32),
         (255, 177, 29), (255, 174, 26), (255, 171, 23), (255, 168, 20), (255, 164, 17), (255, 161, 14), (255, 158, 11), (255, 154, 8),
         (255, 151, 6), (255, 147, 4), (255, 144, 2), (255, 140, 1), (255, 137, 0), (255, 133, 0), (255, 130, 0), (255, 126, 0)])


sunflowers = Particle(
    center_x=1280 / 6 * 3,
    center_y=720 / 4,
    life_seconds=0.8,
    speed=(1, 2),
    shape_cls=Circle,
    size=(1, 5),
    color=sunflowers_color
)


def smoke_color(particle: Particle, shape: Shape) -> pygame.Color:
    return random.choice(
        [(139, 139, 139), (137, 137, 137), (135, 134, 135), (133, 132, 134), (131, 129, 132), (128, 127, 130), (126, 124, 128),
         (124, 122, 127), (122, 119, 125), (120, 117, 123)])


smoke = Particle(
    center_x=1280 / 6 * 5,
    center_y=720 / 4,
    life_seconds=0.7,
    speed=(1, 3),
    shape_cls=Circle,
    size=(10, 60),
    objects_count=40,
    color=smoke_color
)


def triangles_color(particle: Particle, shape: Shape) -> pygame.Color:
    return random.choice(
        [(0, 234, 255), (0, 230, 255), (0, 226, 255), (0, 222, 255), (0, 217, 255), (0, 213, 255), (0, 209, 255), (0, 204, 255),
         (0, 200, 255), (0, 195, 255), (0, 190, 255), (0, 186, 255), (0, 181, 255), (0, 176, 255), (0, 171, 255), (0, 166, 255),
         (0, 161, 255), (0, 156, 252), (0, 150, 250), (0, 145, 247)])


triangles = Particle(
    center_x=1280 / 6 * 3,
    center_y=720 / 4 * 3,
    life_seconds=0.8,
    speed=(2, 2),
    shape_cls=Triangle,
    size=(5, 10),
    color=triangles_color
)


def bubbles_color(particle: Particle, shape: Shape) -> pygame.Color:
    return random.choice(
        [(0, 234, 255), (0, 231, 248), (0, 227, 240), (0, 224, 232), (0, 221, 224), (0, 217, 216), (0, 214, 207), (0, 210, 198),
         (0, 206, 189), (0, 203, 180), (0, 199, 171), (0, 195, 162), (0, 191, 152), (0, 187, 143), (0, 183, 133), (0, 179, 123),
         (0, 175, 114), (0, 171, 104), (0, 167, 94), (0, 163, 84)])


bubbles = Particle(
    center_x=1280 / 6 * 5,
    center_y=720 / 4 * 3,
    life_seconds=0.9,
    speed=(1, 2),
    shape_cls=Circle,
    size=(10, 30),
    width=2,
    objects_count=20,
    color=bubbles_color
)