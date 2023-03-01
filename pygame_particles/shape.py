from __future__ import annotations

import random
from math import cos, pi, radians as to_radians, sin

import pygame


class Point:
    """
    A class representing point in coordinates
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, move: Point) -> None:
        """
        Move point

        :param move: Move vector
        """
        self.x += move.x
        self.y += move.y

    def rotate(self, center: Point, radians: float) -> None:
        """
        Rotate point

        :param center: Center point
        :param radians: Rotate angle in radians
        """
        self.x, self.y = (self.x - center.x) * cos(radians) - (self.y - center.y) * sin(radians) + center.x, (self.x - center.x) * sin(
            radians) + (self.y - center.y) * cos(radians) + center.y

    def __getitem__(self, item: int) -> float:
        """
        :returns point's x, y
        """
        return [self.x, self.y][item]

    def __repr__(self):
        return f"Point({self.x:.2f}, {self.y:.2f})"


class Shape:
    """
    A class representing Shape base object. Used to generate, rotate and move groups of points
    """

    def __init__(self, center: Point, points: list[tuple[int, int]], speed: int):
        self.center = center
        self.points = [
            Point(center.x + move_x, center.y + move_y)
            for move_x, move_y in points
        ]
        destination_angle = random.randint(0, 360)
        self.move_vector = Point(cos(to_radians(destination_angle)) * speed, sin(to_radians(destination_angle)) * speed)

    def rotate(self, angle: int = 0) -> None:
        """
        Rotates the shape around the center by the specified number of degrees

        :param angle: angle to rotate point in degrees
        """
        if angle == 0:
            return
        radians = to_radians(angle)
        for point in self.points:
            point.rotate(self.center, radians)

    def move(self) -> None:
        """
        Move shape with it's speed and destination
        """
        self.center.move(self.move_vector)
        for point in self.points:
            point.move(self.move_vector)

    def draw(self, screen: pygame.Surface, color: pygame.Color, width: int) -> None:
        """
        Draw shape's points on the screen

        :param screen: Surface, where the particles will be drawn
        :param color: Fill color
        """
        pygame.draw.polygon(screen, color, [(x, y) for x, y in self.points], width)


class RegularPolygon(Shape):
    """
    Represents a generated shape, which has equal angles and sides
    """

    def __init__(self, center: Point, radius: float, speed: float, vertices_count: int):
        super().__init__(center, [Point(radius * cos(2 * pi * i / vertices_count), radius * sin(2 * pi * i / vertices_count)) for i in
                                  range(vertices_count)], speed)

class Pentagon(RegularPolygon):
    """
    Pentagon shape
    """

    def __init__(self, center: Point, radius: float, speed: float):
        super().__init__(center, radius, speed, 5)

class Square(RegularPolygon):
    """
    Square shape
    """

    def __init__(self, center: Point, radius: float, speed: float):
        super().__init__(center, radius, speed, 4)
        self.rotate(45)


class Triangle(RegularPolygon):
    """
    Triangle shape
    """

    def __init__(self, center: Point, radius: float, speed: float):
        super().__init__(center, radius, speed, 3)

class Line(RegularPolygon):
    """
    Line shape
    """

    def __init__(self, center: Point, radius: float, speed: float):
        super().__init__(center, radius, speed, 2)

    def draw(self, screen: pygame.Surface, color: pygame.Color, width: int) -> None:
        pygame.draw.line(screen, color, (self.points[0].x, self.points[0].y), (self.points[1].x, self.points[1].y), width)

class Circle(Shape):
    """
    Circle shape
    """

    def __init__(self, center: Point, radius: float, speed: float):
        super().__init__(center, [], speed)
        self.radius = radius

    def rotate(self, angle: int = 0) -> None:
        """
        Does nothing, because rotated circle is the same circle
        """

    def draw(self, screen: pygame.Surface, color: pygame.Color, width: int) -> None:
        pygame.draw.circle(screen, color, (self.center.x, self.center.y), self.radius, width)
