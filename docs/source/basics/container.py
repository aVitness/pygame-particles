from pygame_particles import ParticleContainer

screen = ...  # pygame.Surface
particle = ...  # Particle

# Creating container. It will store copies of particles. You can make it empty at the beginning
container = ParticleContainer(particle, particle, particle)
# Add particle to the container (also copies)
container.add(particle)
# Updates all particles, draw them and deletes dead particles, so they don't take your memory
container.draw(screen)