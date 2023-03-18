import random

import pygame

from pygame_particles import Circle, Particle, ParticleContainer


def sunflowers_color(particle, shape):
    return random.choice(
        [(250, 250, 110), (250, 247, 106), (251, 244, 102), (251, 241, 99), (251, 238, 95), (251, 236, 91), (252, 233, 88), (252, 230, 84),
         (252, 227, 81), (253, 224, 77), (253, 221, 74), (253, 218, 70), (253, 215, 67), (254, 212, 64), (254, 209, 60), (254, 206, 57),
         (254, 203, 54), (254, 200, 50), (255, 196, 47), (255, 193, 44), (255, 190, 41), (255, 187, 38), (255, 184, 35), (255, 181, 32),
         (255, 177, 29), (255, 174, 26), (255, 171, 23), (255, 168, 20), (255, 164, 17), (255, 161, 14), (255, 158, 11), (255, 154, 8),
         (255, 151, 6), (255, 147, 4), (255, 144, 2), (255, 140, 1), (255, 137, 0), (255, 133, 0), (255, 130, 0), (255, 126, 0)])


screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Vitness's particles example")
pygame.init()
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1500)
particles = ParticleContainer()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            particles.add(
                Particle(
                    center_x=event.pos[0],
                    center_y=event.pos[1],
                    life_seconds=0.6,
                    speed=(1, 2),
                    shape_cls=Circle,
                    size=(1, 4),
                    color=sunflowers_color
                )
            )
    screen.fill("black")
    particles.draw(screen)
    pygame.display.flip()
    clock.tick(60)
