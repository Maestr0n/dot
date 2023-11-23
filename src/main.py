import sys
import pygame
import random

from src.entities.base import Entity

window_size = (300, 300)
screen_color = (10, 152, 14)


def init():
    pygame.init()
    icon_path = '/home/aleksanyan/PycharmProjects/dot/src/images/icon.png'

    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('DoT')
    pygame.display.set_icon(pygame.image.load(icon_path))
    screen.fill(screen_color)

    return screen


def random_color_cord(win_color) -> tuple:

    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if win_color == random_color:
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    random_cord = (random.randint(0, window_size[0] - 3), random.randint(0, window_size[1] - 3))

    return random_cord, random_color


def run(screen: pygame.Surface, window_color=screen_color):
    dot_x = window_size[0] // 2
    dot_y = window_size[1] // 2
    entity_image_path = '/home/aleksanyan/PycharmProjects/dot/src/images/dot.png'
    entity = Entity(entity_image_path, dot_x, dot_y)
    point = random_color_cord(window_color)

    while True:
        pygame.draw.circle(screen, point[1], point[0], 5)
        pygame.display.update()
        screen.fill(window_color)
        screen.blit(entity.image, (entity.x, entity.y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            entity.go_up()
        elif keys[pygame.K_DOWN]:
            entity.go_down()
        elif keys[pygame.K_LEFT]:
            entity.go_left()
        elif keys[pygame.K_RIGHT]:
            entity.go_right()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    entity.go_down()
                elif event.key == pygame.K_DOWN:
                    entity.go_up()
                elif event.key == pygame.K_LEFT:
                    entity.go_left()
                elif event.key == pygame.K_RIGHT:
                    entity.go_right()

            dot_cord = entity.cord[0] + 24, entity.cord[1] + 24
            point_cord = point[0]
            if abs(dot_cord[0] - point_cord[0]) + abs(dot_cord[1] - point_cord[1]) <= 30:
                window_color = point[1]
                point = random_color_cord(window_color)


if __name__ == '__main__':
    run(init())
