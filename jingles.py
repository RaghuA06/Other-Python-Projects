#Raghu Alluri
#6/1/2018
#This program plays a jingle when clicked on a button

import pygame

pygame.init()

WHITE = (255, 255, 255)
COLOR = (0, 255, 100)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

sw = 800
sh = 600

pepsiJingle = pygame.mixer.Sound('PepsiJingle.wav')
colaJingle = pygame.mixer.Sound('ColaJingle.wav')

wn = pygame.display.set_mode([sw, sh])
pygame.display.set_caption("Jingles")

def showText():
    myfont = pygame.font.SysFont("Arial", 100)
    TextSurf = myfont.render("Jingle Player", False, COLOR)
    wn.blit(TextSurf, [(sw / 2) - 200, 200])

def playJingleOne(b1x, b1y, b1w, b1h):
    button1 = pygame.draw.rect(wn, GREEN, [b1x, b1y, b1w, b1h])
    myfont = pygame.font.SysFont("Arial", 32)
    TextSurf = myfont.render("Jingle 1", False, YELLOW)
    wn.blit(TextSurf, [b1x + 10, b1y + 5])

def playJingleTwo(b2x, b2y, b2w, b2h):
    button1 = pygame.draw.rect(wn, GREEN, [b2x, b2y, b2w, b2h])
    myfont = pygame.font.SysFont("Arial", 32)
    TextSurf = myfont.render("Jingle 2", False, YELLOW)
    wn.blit(TextSurf, [b2x + 10, b2y + 5])

def mainLoop():

    j1x = 100
    j1y = 400
    j1w = 100
    j1h = 50

    j2x = 600
    j2y = 400
    j2w = 100
    j2h = 50

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

        wn.fill(WHITE)

        cursor = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()

        if 100 < cursor[0] < 200 and 400 < cursor[1] < 450:
            if clicked[0] == 1:
                colaJingle.stop()
                pepsiJingle.play()
        elif 600 < cursor[0] < 700 and 400 < cursor[1] < 450:
            if clicked[0] == 1:
                pepsiJingle.stop()
                colaJingle.play()

        showText()
        playJingleOne(j1x, j1y, j1w, j1h)
        playJingleTwo(j2x, j2y, j2w, j2h)

        pygame.display.update()

mainLoop()
