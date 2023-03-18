# Import pygame and particles
import pygame

from pygame_particles import Particle

# Initialize screen
pygame.init()
screen = pygame.display.set_mode((300, 300))

# Creates standart particle on (100, 100) position
my_cool_particle = Particle(150, 150)

# Update it if you want
# my_cool_particle.update()

# Draw it
my_cool_particle.draw(screen)
# Update display
pygame.display.flip()
