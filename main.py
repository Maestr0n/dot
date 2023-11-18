import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('DoT')
pygame.display.set_icon(pygame.image.load('images/ket.png'))
#dot = pygame.image.load('images/dot.png')
dot_x = 150
dot_y = 150
screen.fill((10, 152, 14))

running = True

while running:

    pygame.display.update()

    for event in pygame.event.get():
        # screen.blit(, (dot_x, dot_y))

        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dot_y += 5
            elif event.type == pygame.K_DOWN:
                dot_y -= 5
            elif event.type == pygame.K_LEFT:
                dot_x += 5
            elif event.type == pygame.K_RIGHT:
                dot_x -= 5

