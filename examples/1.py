import pygame
from pygame_particles import Line, Particle, ParticleContainer
# Importing some pre-built particles examples
from pygame_particles.examples import bubbles, smoke, sunflowers, triangles, white_cubes

# Creating one custom particle
# Color
def my_cool_particle_color(particle, shape):
    if particle.state == 0:
        return "red"
    return 255 * (100 - particle.percent_completed) / 100, 0, 0

# Particle
my_cool_particle = Particle(
    center_x=1280 / 6,
    center_y=720 / 4 * 3,
    life_seconds=0.6,
    fade_seconds=1,
    speed=(1, 2),
    shape_cls=Line,
    size=(5, 15),
    color=my_cool_particle_color,
    width=3
)

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
        if event.type == pygame.USEREVENT:
            particles.add(white_cubes)
            particles.add(sunflowers)
            particles.add(smoke)
            particles.add(my_cool_particle)
            particles.add(triangles)
            particles.add(bubbles)
    screen.fill("black")
    particles.draw(screen)
    pygame.display.flip()
    clock.tick(60)