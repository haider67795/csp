# imports
import pygame
import random

pygame.init()
# varibles
WIDTH = 1280
HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
mainRect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 10, 10)
ivanPic = pygame.image.load("media/ivanCropped.png")
fordPic = pygame.image.load("media/fordCropped.png")
ivanChar = pygame.transform.scale(ivanPic, (60, 60))
ivanChar = pygame.transform.flip(ivanChar, True, False)
fordChar = pygame.transform.scale(fordPic, (60, 60))

ivanRect = pygame.Rect(
    20,
    HEIGHT // 2 - ivanChar.get_height() // 2,
    ivanChar.get_width(),
    ivanChar.get_height(),
)
fordRect = pygame.Rect(
    WIDTH // 2 - fordChar.get_width(),
    HEIGHT // 2 - fordChar.get_height() // 2,
    fordChar.get_width(),
    fordChar.get_height(),
)

font_game = pygame.font.SysFont("Arial", 20)


def move(rect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and rect.y > 0:
        rect.y -= 1
    if keys[pygame.K_a] and rect.x > 0:
        rect.x -= 1
    if keys[pygame.K_s] and rect.y < HEIGHT - rect.height:
        rect.y += 1
    if keys[pygame.K_d] and rect.x < WIDTH - rect.width:
        rect.x += 1


def checkCol():
    if ivanRect.colliderect(fordRect):
        fordRect.x, fordRect.y = random.randint(
            0, WIDTH - fordRect.width
        ), random.randint(0, HEIGHT - fordRect.height)
        return 1
    else:
        return 0


running = True


# main game loop

score = 0
while running:
    screen.fill(BLACK)
    move(ivanRect)

    if checkCol() == 1:
        score += 1

    text = pygame.font.Font.render(font_game, "Score: " + str(score), 1, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width(), 20))
    screen.blit(fordChar, (fordRect.x, fordRect.y))
    screen.blit(ivanChar, (ivanRect.x, ivanRect.y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()


pygame.quit()
