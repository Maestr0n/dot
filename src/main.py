import sys
import pygame
import random

from src.entities.base import Entity

window_size = (600, 600)
screen_color = (255, 255, 255)


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


def run(screen,  window_color=screen_color, window=window_size):
    quantity_dot = 0
    dot_x = 405.5
    dot_y = 516
    entity_image_path = '/home/aleksanyan/PycharmProjects/dot/src/images/smile.png'
    entity = Entity(entity_image_path, dot_x, dot_y, window)
    point = random_color_cord(window_color)
    pinocio_image = pygame.image.load('/home/aleksanyan/PycharmProjects/dot/src/images/pinocio.png')
    screen.blit(pinocio_image, (400, 391))
    while True:

        #font = pygame.font.SysFont('tlwgtypo', 30)
        #score = font.render(f'{quantity_dot}', 1, (255, 255, 255), )
        #screen.blit(score, (0, 0))
        #pygame.draw.circle(screen, (0, 0, 0), point[0], 8)
        #pygame.draw.circle(screen, point[1], point[0], 5)
        pygame.display.update()
        screen.fill(window_color)
        #screen.blit(entity.image, (entity.x, entity.y))

        screen.blit(pinocio_image, (400, 391))
        for dot in entity.cords:
            pygame.draw.circle(screen, (234, 174, 126), dot, 5)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            entity.go_up()
        if keys[pygame.K_DOWN]:
            entity.go_down()
        if keys[pygame.K_LEFT]:
            entity.go_left(screen)
        if keys[pygame.K_RIGHT]:
            entity.go_right()
        if keys[pygame.K_DELETE]:
            entity.new_list()
        if keys[pygame.K_SPACE]:
            entity.del_end_point()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            dot_cord = entity.cord[0] + 24, entity.cord[1] + 24
            #point_cord = point[0]
            #if abs(dot_cord[0] - point_cord[0]) + abs(dot_cord[1] - point_cord[1]) <= 30:
            #    window_color = point[1]
            #    point = random_color_cord(window_color)
            #    quantity_dot += 1



if __name__ == '__main__':
    run(init())
