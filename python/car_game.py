import pygame
from pygame.locals import *
import random

pygame.init()
carPic = pygame.image.load("media/mainCar.png")  # 1000x700
car = pygame.transform.scale(carPic, (140, 220))

oppPic = pygame.image.load("media/oppCar.png")
oppCar = pygame.transform.scale(oppPic, (140, 220))

oppPic2 = pygame.image.load("media/oppCar2.png")
oppCar2 = pygame.transform.scale(oppPic2, (140, 220))

lanePic = pygame.image.load("media/lane.png")
lane = pygame.Rect(490, 0, 5, 120)

lane2Pic = pygame.image.load("media/lane.png")
lane2 = pygame.Rect(785, 0, 5, 120)

heartLoad = pygame.image.load("media/heart.png")
heart = pygame.transform.scale(heartLoad, (50, 50))

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

carRect = pygame.Rect(
    screen_width // 2 - car.get_width() // 2,
    720 - car.get_height(),
    140,
    220,
)


def road():
    road1 = pygame.Rect(200, 0, 880, 720)

    pygame.draw.rect(screen, (80, 80, 80), road1)


def move(rect):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and rect.x > 200:
        rect.x -= 10

    if keys[pygame.K_d] and rect.x < 1080 - car.get_width():
        rect.x += 10


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


def checkCol():
    if carRect.colliderect(oppRect) or carRect.colliderect(oppRect2):
        return 1
    else:
        return 0


def moveOpp(opp):
    if opp.y < 720:
        opp.y += 10
        return opp
    else:
        opp.x = xchoices[random.randint(0, 2)]
        opp.y = 0 - opp.height
        return opp


def buildLanes():
    lane.y += 10
    if lane.y > 720:
        lane.y = 0 - screen_height
    lane2.y += 10
    if lane2.y > 720:
        lane2.y = 0 - screen_height
    screen.blit(lanePic, (lane.x, lane.y - screen_height))
    screen.blit(lanePic, (lane.x, lane.y))
    screen.blit(lanePic, (lane.x, lane.y + screen_height))
    screen.blit(lane2Pic, (lane2.x, lane2.y - screen_height))
    screen.blit(lane2Pic, (lane2.x, lane2.y))
    screen.blit(lane2Pic, (lane2.x, lane2.y + screen_height))


def health(lives):
    for x in range(lives):
        screen.blit(heart, (50 * x, 0))


def antiAFK():
    carRect.x += random.randint(100, 105)


count = 0
font = pygame.font.SysFont("Arial", 20)
lives = 3
running = True
while running:
    screen.fill("darkgreen")
    road()

    buildLanes()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    if checkCol() == 1:
        carRect = pygame.Rect(
            screen_width // 2 - car.get_width() // 2,
            720 - car.get_height(),
            140,
            220,
        )
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
        lives -= 1
    if lives == 0:
        running = False
    health(lives)
    move(carRect)
    moveOpp(oppRect)
    moveOpp(oppRect2)
    if oppRect.colliderect(oppRect2):
        while oppRect2.x == oppRect.x:
            oppRect2.x = xchoices[random.randint(0, 2)]
        oppRect.y = 0 - oppCar2.get_height() - random.randint(140, 200)
        oppRect2.y = 0 - oppCar2.get_height() - random.randint(140, 200)
    screen.blit(car, (carRect.x, carRect.y))
    screen.blit(oppCar, (oppRect.x, oppRect.y))
    screen.blit(oppCar2, (oppRect2.x, oppRect2.y))
    text = pygame.font.Font.render(font, "Score: " + str(count), 1, "white")
    screen.blit(text, (screen_width // 2 - text.get_width(), 20))
    pygame.display.flip()
    count += 1
    clock.tick(60)
print("Your Highest Score Was " + str(count))
pygame.quit()
