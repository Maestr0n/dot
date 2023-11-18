import sys
import pygame

from src.entities.base import Entity

window_size = (300, 300)
screen_color = (10, 152, 14)

def init():
    pygame.init()
    icon_path = '/home/olgert/projects/dot/src/images/icon.png'

    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('DoT')
    pygame.display.set_icon(pygame.image.load(icon_path))
    screen.fill(screen_color)

    return screen


def run(screen: pygame.Surface):
    dot_x = window_size[0] // 2
    dot_y = window_size[1] // 2
    entity_image_path = '/home/olgert/projects/dot/src/images/dot.png'
    entity = Entity(entity_image_path, dot_x, dot_y)
    while True:
        pygame.display.update()
        screen.fill(screen_color)
        screen.blit(entity.image, (entity.x, entity.y))

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

        pygame.display.flip()


if __name__ == '__main__':
    run(init())
