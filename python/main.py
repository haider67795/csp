# imports
import pygame
import random

# varible declaration
WIDTH = 1280
HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
mainRect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 10, 10)

# function declaration


def move(rect):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and rect.y > 0:
        print("w")
        rect.y -= 1
    if keys[pygame.K_a] and rect.x > 0:
        print("a")
        rect.x -= 1
    if keys[pygame.K_s] and rect.y < HEIGHT - rect.height:
        print("s")
        rect.y += 1
    if keys[pygame.K_d] and rect.x < WIDTH - rect.width:
        print("d")
        rect.x += 1
    return rect


# I Don't even know tbh
pygame.init()

running = True


# main game loop

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(
        screen,
        (
            random.randrange(0, 256, 255),
            random.randrange(0, 256, 255),
            random.randrange(0, 256, 255),
        ),
        move(mainRect),
    )
    pygame.display.flip()


pygame.quit()
