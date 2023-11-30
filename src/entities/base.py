import pygame


class Entity:
    x: float
    y: float
    move: int = 0.5
    image_path: str
#    cord_list = []

    def __init__(self, image_path: str, x: float, y: float, win_size: tuple):
        self._image_path = image_path
        self.image = pygame.image.load(self._image_path)
        self.x = x
        self.y = y
        self.win_size = win_size

    def go_left(self):
        if self.x > - 126:
            self.x -= self.move
#            self.cord_list.append(self.cord)
            if self.x < -125:
                self.x = self.win_size[0]

    def go_right(self):

        if self.x < self.win_size[0] + 1:
            self.x += self.move
#            self.cord_list.append(self.cord)
            if self.x == self.win_size[0] :
                self.x = - 125

    def go_down(self):

        if self.y < self.win_size[1] + 1:
            self.y += self.move
#            self.cord_list.append(self.cord)
            if self.y == self.win_size[1]:
                self.y = -125

    def go_up(self):

        if self.y > -126:
            self.y -= self.move
#            self.cord_list.append(self.cord)
            if self.y == -125:
                self.y = self.win_size[1]

    @property
    def cord(self) -> tuple:
        return self.x, self.y

#    @cord.setter
#   def cord(self, new_cord):
#        self.x = new_cord[0]
#        self.y = new_cord[1]

#    @property
#    def cords(self):
#        return self.cord_list

#    def new_list(self):
#        self.cord_list = []

 #   def del_end_point(self):
 #       if len(self.cord_list) > 0:
 #           self.cord_list.pop(-1)
 #       else:
 #           pass

    def update_images(self, new_path):
        if new_path != self._image_path:
            self._image_path = new_path
            self.__init__(self._image_path, self.x, self.y, self.win_size)

