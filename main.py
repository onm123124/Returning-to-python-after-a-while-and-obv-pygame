import pygame
import time

# initialize
pygame.init()

# vars
screen = pygame.display.set_mode((0, 0))  # fullscreen
clock = pygame.time.Clock()
square_pos = pygame.Rect(600, 800, 50, 50)  # Use pygame.Rect() instead of pygame.rect()


while True:
    for event in pygame.event.get(): #fr loop
        if event.type == pygame.QUIT:
            break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_pos.x -= 20
    pygame.display.update()

    if keys[pygame.K_RIGHT]:
        square_pos.x += 20
    pygame.display.update()

    if keys[pygame.K_UP]:
        square_pos.y -= 20
    pygame.display.update()

    if keys[pygame.K_DOWN]:
        square_pos.y += 20
    pygame.display.update()

    screen.fill("white")  # Because i like being flashbanged
    pygame.draw.rect(screen, "black", square_pos)
    pygame.display.flip()#update display
    clock.tick(60)

pygame.quit()
