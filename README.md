# Particles for pygame
Installing
-----------

You can get the library directly from PyPI:

On Windows

```bash
py -m pip install pygame-particles
```

On Linux

```bash
python3 -m pip install pygame-particles
```


Basics
------
### Particle
There are a lot of arguments, but required is only center position. So this is the minimal particle example

```python3
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
```
By running this code you won't see something nice and interesting, it is just a showcase of how to use them


### Shape
You can subclass shape object to create your own

```python3
from pygame_particles import Shape

class CustomShape(Shape):
    def __init__(self, center, radius, speed):
        super().__init__(center, [(-10, 0), (0, -10), (10, 0), (0, 10)], speed)
```
Now you can use this `CustomShape` as `shape_cls` argument for particle

### Container
Container is an object which has some methods to make your work easier

```python3
from pygame_particles import ParticleContainer

screen = ... # pygame.Surface
particle = ... # Particle

# Creating container. It will store copies of particles. You can make it empty at the beginning
container = ParticleContainer(particle, particle, particle) 
# Add particle to the container (also copies)
container.add(particle)
# Updates all particles, draw them and deletes dead particles, so they don't take your memory
container.draw(screen)
```

Examples
--------
### Just particles
This is example of full code with particles

```python3
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
    speed_range=(1, 2),
    shape_cls=Line,
    size_range=(5, 15),
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
```

![Result](docs/videos/example1.gif)

### Mouse particles
Particles appearing on mouse position

```python3
import pygame
import random
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
                    speed_range=(1, 2),
                    shape_cls=Circle,
                    size_range=(1, 4),
                    color=sunflowers_color
                )
            )
    screen.fill("black")
    particles.draw(screen)
    pygame.display.flip()
    clock.tick(60)
```
![Result](docs/videos/example2.gif)