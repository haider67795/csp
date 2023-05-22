import pygame
from pygame.locals import *
import random

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
white = (255, 255, 255)
blue = (0, 0, 255)
main_rect_width = 50
main_rect_height = 50

target_rect_width = 50
target_rect_height = 50
main_rect = pygame.Rect(200, 200, main_rect_width, main_rect_height)
target_rect = pygame.Rect(500, 200, target_rect_width, target_rect_height)


def generate_target_position():
    x = random.randint(0, screen_width - target_rect_width)
    y = random.randint(0, screen_height - target_rect_height)
    return x, y


target_rect.x, target_rect.y = generate_target_position()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update the position of the main rectangle based on user input
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        main_rect.x -= 5
    if keys[K_RIGHT]:
        main_rect.x += 5
    if keys[K_UP]:
        main_rect.y -= 5
    if keys[K_DOWN]:
        main_rect.y += 5

    # Check for collision between the main rectangle and the target rectangle
    if main_rect.colliderect(target_rect):
        target_rect.x, target_rect.y = generate_target_position()

    # Clear the screen
    screen.fill(white)

    # Draw the rectangles on the screen
    pygame.draw.rect(screen, blue, main_rect)
    pygame.draw.rect(screen, blue, target_rect)

    # Update the screen
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
