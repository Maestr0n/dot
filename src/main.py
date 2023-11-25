import sys
import time

import pygame
import random

from src.entities.base import Entity

window_size = (600, 600)
screen_color = (2, 2, 2)


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


def run(screen, window_color=screen_color, window=window_size):
    quantity_dot = 0
    dot_x = window[0] // 2
    dot_y = window[1] // 2
    packman_open_path = '/home/aleksanyan/PycharmProjects/dot/src/images/packman/l.png'
    packman_close_path = '/home/aleksanyan/PycharmProjects/dot/src/images/packman/close.png'
    entity = Entity(packman_open_path, dot_x, dot_y, window)
    point = random_color_cord(window_color)
    gosts_path = ('/home/aleksanyan/PycharmProjects/dot/src/images/packman gost/gost_red.png',
                  '/home/aleksanyan/PycharmProjects/dot/src/images/packman gost/gost_blue.png',
                  '/home/aleksanyan/PycharmProjects/dot/src/images/packman gost/gost_pink.png',
                  '/home/aleksanyan/PycharmProjects/dot/src/images/packman gost/gost_orage.png')
    gost = pygame.image.load(random.choice(gosts_path))

    while True:

        font = pygame.font.SysFont('tlwgtypo', 30)
        score = font.render(f'{quantity_dot}', 1, (255, 255, 255), )
        screen.blit(score, (0, 0))
        screen.blit(gost, point[0])
        pygame.display.update()
        screen.fill(window_color)
        screen.blit(entity.image, (entity.x, entity.y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            packman_open_path = '/home/aleksanyan/PycharmProjects/dot/src/images/packman/u.png'
            entity.update_images(packman_open_path)
            screen.blit(entity.image, (entity.x, entity.y))
            entity.go_up()
        if keys[pygame.K_DOWN]:
            packman_open_path = '/home/aleksanyan/PycharmProjects/dot/src/images/packman/d.png'
            entity.update_images(packman_open_path)
            screen.blit(entity.image, (entity.x, entity.y))
            entity.go_down()
        if keys[pygame.K_LEFT]:
            packman_open_path = '/home/aleksanyan/PycharmProjects/dot/src/images/packman/l.png'
            entity.update_images(packman_open_path)
            screen.blit(entity.image, (entity.x, entity.y))
            entity.go_left()
        if keys[pygame.K_RIGHT]:
            packman_open_path = '/home/aleksanyan/PycharmProjects/dot/src/images/packman/r.png'
            entity.update_images(packman_open_path)
            screen.blit(entity.image, (entity.x, entity.y))
            entity.go_right()
#        if keys[pygame.K_DELETE]:
#            entity.new_list()
#        if keys[pygame.K_SPACE]:
#            entity.del_end_point()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            dot_cord = entity.cord[0] + 24, entity.cord[1] + 24
            point_cord = point[0]
            if abs(dot_cord[0] - point_cord[0]) + abs(dot_cord[1] - point_cord[1]) <= 80:
                point = random_color_cord(window_color)
                gost = pygame.image.load(random.choice(gosts_path))
                entity.update_images(packman_close_path)
                screen.blit(entity.image, (entity.x, entity.y))
                pygame.display.update()
                time.sleep(0.13)
                entity.update_images(packman_open_path)
                screen.blit(entity.image, (entity.x, entity.y))
                pygame.display.update()
                quantity_dot += 1

if __name__ == '__main__':
    run(init())
