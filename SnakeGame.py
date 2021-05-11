#Raghu Alluri
#April 10th, 2018
#Progam is a game of classic snake found on mobiles (made using pygame)

import pygame
import random

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 220, 0)

sw = 800
sh = 600

s = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

appleImg = pygame.image.load("Apple.png")
snakeWall = pygame.image.load("ThisSnake.png")
grassWall = pygame.image.load("grass.png")

def snake(snake_list):
    for snk in snake_list:
        pygame.draw.rect(s, ORANGE, [snk[0], snk[1], 20, 20])

def food(fx, fy):
    s.blit(appleImg, [fx, fy])

def scoreGame(scr):
    scoreFont = pygame.font.SysFont("Arial", 24)
    ScrSurf = scoreFont.render("Score: " + str(scr), True, BLUE)
    s.blit(ScrSurf, [0, 0])

def crashed(snk_scr):

    playAgain = True

    while playAgain:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mainLoop()

        s.fill(WHITE)

        over = pygame.font.SysFont("Comic Sans MS", 72)
        TextSurf = over.render('Game Over', False, BLACK)
        s.blit(TextSurf, [(sw / 2) - 72 * 2, (sh / 2) - 72])

        again = pygame.font.SysFont("Comic Sans MS", 48)
        TS = again.render("Press R To Play Again", False, GREEN)
        s.blit(TS, [(sw / 2) - 240, (sh / 2) + 100])

        finalScore = pygame.font.SysFont("Comic Sans MS", 48)
        ScoreSurf = finalScore.render("Score: " + str(snk_scr), False, RED)
        s.blit(ScoreSurf, [(sw / 2) - 96, (sh / 2) - 200])

        pygame.display.update()

def mnScreen():

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    mainLoop()

        s.blit(snakeWall, [0, 0])

        myfont = pygame.font.SysFont("Comic Sans MS", 72)
        textsurf = myfont.render("Snake Game", False, ORANGE)
        s.blit(textsurf, [(sw / 2) - 72 * 2 - 50, (sh / 2) - 72])

        playfont = pygame.font.SysFont("Comic Sans MS", 32)
        playsurf = playfont.render("Press SPACE to play", False, WHITE)
        s.blit(playsurf, [(sw / 2) - 32 * 4, (sh / 2) + 100])

        pygame.display.update()


def mainLoop():

    finish = False

    headx = sw / 2
    heady = sh / 2
    xchange = 0
    ychange = 0

    foodx = round(random.randint(0, sw) / 20.0) * 20.0
    foody = round(random.randint(0, sh) / 20.0) * 20.0

    snakeList = []
    snkLength = 1

    score = 0

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xchange = -20
                    ychange = 0
                if event.key == pygame.K_RIGHT:
                    xchange = 20
                    ychange = 0
                if event.key == pygame.K_DOWN:
                    ychange = 20
                    xchange = 0
                if event.key == pygame.K_UP:
                    ychange = -20
                    xchange = 0


        headx += xchange
        heady += ychange

        s.blit(grassWall, [0, 0])

        snakeHead = []
        snakeHead.append(headx)
        snakeHead.append(heady)
        snakeList.append(snakeHead)

        if len(snakeList) > snkLength:
            del snakeList[0]

        snake(snakeList)

        food(foodx, foody)

        scoreGame(score)

        #Boundaries
        if headx > sw - 40 or headx < 0 + 20:
            crashed(score)
        if heady > sh - 40 or heady < 0 + 20:
            crashed(score)

        if headx == foodx and heady == foody:
            snkLength += 1
            foodx = round(random.randint(0 + 20, sw - 20) / 20.0) * 20.0
            foody = round(random.randint(0 + 20, sh - 20) / 20.0) * 20.0
            score += 1

        pygame.display.update()
        clock.tick(15)

mnScreen()
mainLoop()
