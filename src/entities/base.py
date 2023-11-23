import pygame


class Entity:
    x: float
    y: float
    move: int = 1/4
    image_path: str

    def __init__(self, image_path: str, x: float, y: float):
        self._image_path = image_path
        self.image = pygame.image.load(self._image_path)
        self.x = x - 24
        self.y = y - 24

    def go_left(self):
        if self.x > -24:
            self.x -= self.move
            if self.x == -24:
                self.x = 276

    def go_right(self):
        if self.x < 276:
            self.x += self.move
            if self.x == 276:
                self.x = -24

    def go_down(self):
        if self.y < 276:
            self.y += self.move
            if self.y == 276:
                self.y = -24

    def go_up(self):
        if self.y > -24:
            self.y -= self.move
            if self.y == - 24:
                self.y = 276

    @property
    def cord(self) -> tuple:
        return self.x, self.y

    @cord.setter
    def cord(self, new_cord):
        self.x = new_cord[0]
        self.y = new_cord[1]
