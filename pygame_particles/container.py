import pygame
from .particle import Particle


class ParticleContainer:
    """
    Object that stores a list of particles and has a couple of features to make easier working with particles
    """

    def __init__(self, *particles):
        self.particles = [self.copy_particle(particle) for particle in particles]

    def add(self, particle: Particle):
        """
        Add particle in the container
        :param particle: particle object
        """
        self.particles.append(self.copy_particle(particle))

    def copy_particle(self, particle: Particle):
        """
        Creates a copy of particle, so you can use the same particle and it won't affect them
        """
        return Particle(
            shape_cls=particle.shape_cls,
            center_x=particle.center.x,
            center_y=particle.center.y,
            objects_count=particle.objects_count,
            life_seconds=particle.life_seconds,
            fade_seconds=particle.fade_seconds,
            life_iterations=particle.life_iterations,
            fade_iterations=particle.fade_iterations,
            color=particle.color,
            size_range=particle.size_range,
            speed_range=particle.speed_range,
            rotate_angle_range=particle.rotate_angle_range,
            width=particle.width
        )

    def draw(self, screen: pygame.Surface) -> None:
        """
        Updates, draws and deletes dead particles
        """
        for particle in self.particles:
            particle.update()
            particle.draw(screen)
        self.particles = [particle for particle in self.particles if not particle.is_dead()]
