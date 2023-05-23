import pygame
from pygame.locals import *
import random

pygame.init()
carPic = pygame.image.load("media/mainCar.png")  # 1000x700
car = pygame.transform.scale(carPic, (140, 240))

oppPic = pygame.image.load("media/oppCar.png")
oppCar = pygame.transform.scale(oppPic, (140, 240))

oppPic2 = pygame.image.load("media/oppCar2.png")
oppCar2 = pygame.transform.scale(oppPic2, (140, 240))

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
carRect = pygame.Rect(
    screen_width // 2 - car.get_width() // 2,
    720 - car.get_height(),
    200,
    140,
)


def road():
    road1 = pygame.Rect(200, 0, 880, 720)

    pygame.draw.rect(screen, (80, 80, 80), road1)


def move(rect):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and rect.x > 200:
        rect.x -= 20

    if keys[pygame.K_d] and rect.x < 1080 - car.get_width():
        rect.x += 20
    if keys[pygame.K_w] and rect.y > 240:
        rect.y -= 20

    if keys[pygame.K_s] and rect.y < 720 - car.get_height():
        rect.y += 20


xchoices = [275, 570, 865]

oppRect = pygame.Rect(
    xchoices[random.randint(0, 2)],
    0 - oppCar.get_height(),
    oppCar.get_width(),
    oppCar.get_height(),
)
oppRect2 = pygame.Rect(
    xchoices[random.randint(0, 2)],
    0 - oppCar.get_height(),
    oppCar.get_width(),
    oppCar.get_height(),
)


def buildLanes():
    lane1 = pygame.Rect(490, 0, 5, 36)
    lane2 = pygame.Rect(785, 0, 5, 36)
    for x in range(0, 11):
        lane1.y = x * 36 * 2
        pygame.draw.rect(screen, (255, 255, 255), lane1)
    for x in range(0, 11):
        lane2.y = x * 36 * 2
        pygame.draw.rect(screen, (255, 255, 255), lane2)


def checkCol():
    if carRect.colliderect(oppRect) or carRect.colliderect(oppRect2):
        return 1
    else:
        return 0


running = True


def moveOpp(opp):
    if opp.y < 720:
        opp.y += random.randint(10, 20)
        return opp
    else:
        opp.x = xchoices[random.randint(0, 2)]
        opp.y = 0 - opp.height
        return opp


while running:
    screen.fill("black")

    road()

    buildLanes()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # if checkCol() == 1:
    #     running = False

    move(carRect)
    # while moveOpp(oppRect).x == moveOpp(oppRect2).x:
    #     if moveOpp(oppRect2).y > 720:
    #         moveOpp(oppRect2).x = xchoices[random.randint(0, 2)]
    #     else:

    moveOpp(oppRect)
    moveOpp(oppRect2)
    if oppRect.colliderect(oppRect2):
        oppRect2.x = xchoices[random.randint(0, 2)]
        oppRect.y = 0 - oppCar2.get_height()
        oppRect2.y = 0 - oppCar2.get_height()

    screen.blit(car, (carRect.x, carRect.y))
    screen.blit(oppCar, (oppRect.x, oppRect.y))
    screen.blit(oppCar2, (oppRect2.x, oppRect2.y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
