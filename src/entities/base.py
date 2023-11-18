import pygame


class Entity:
    x: float
    y: float
    move: int = 5
    image_path: str

    def __init__(self, image_path: str, x: float, y: float):
        self._image_path = image_path
        self.image = pygame.image.load(self._image_path)
        self.x = x
        self.y = y

    def go_left(self):
        self.x -= self.move

    def go_right(self):
        self.x += self.move

    def go_up(self):
        self.y += self.move

    def go_down(self):
        self.y -= self.move
