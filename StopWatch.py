import pygame
import time

pygame.init()

WHITE = (255, 255, 255)
GREEN = (0, 185, 0)
LIGHTGREEN = (0, 255, 0)
RED = (185, 0, 0)
LIGHTRED = (255, 0, 0)
BLACK = (0, 0, 0)
ORANGE = (255, 185, 0)
YELLOW = (255,255, 0)

sw = 400
sh = 600

screen = pygame.display.set_mode([sw, sh])
pygame.display.set_caption("Stop Watch")
clock = pygame.time.Clock()

def startButton(bx, by, bw, bh, bcol, nx, ny):
    pygame.draw.rect(screen, bcol, [bx, by, bw, bh])

    thisfont = pygame.font.SysFont("Verdana", 18)
    TextSurf = thisfont.render("START", True, BLACK)
    screen.blit(TextSurf, [bx + nx, by + ny])

def stopButton(sx, sy, sw, sh, scol, nx, ny):
    pygame.draw.rect(screen, scol, [sx, sy, sw, sh])

    thisfont = pygame.font.SysFont("Verdana", 18)
    TextSurf = thisfont.render("STOP", True, BLACK)
    screen.blit(TextSurf, [sx + nx, sy + ny])

def resetButton(rx, ry, rw, rh, rcol, nx, ny):
    pygame.draw.rect(screen, rcol, [rx, ry, rw, rh])

    thisfont = pygame.font.SysFont("Verdana", 18)
    TextSurf = thisfont.render("RESET", True, BLACK)
    screen.blit(TextSurf, [rx + nx, ry + ny])

def showColon(nx, ny):
    thisfont = pygame.font.SysFont("'Verdana", 72)
    TextSurf = thisfont.render(".", True, BLACK)
    screen.blit(TextSurf, [230 - 10, 150])

def milsecTime(milseclist):
    thisfont = pygame.font.SysFont("Verdana", 72)
    TextSurf = thisfont.render(str(milseclist[0]), True, BLACK)
    screen.blit(TextSurf, [240, 150])

def secTime(seclist):
    thisfont = pygame.font.SysFont("Verdana", 72)
    TextSurf = thisfont.render(str(seclist[0]), True, BLACK)
    screen.blit(TextSurf, [140, 150])

def mainloop():

    btncol = GREEN
    btnw = 100
    btnh = 50
    btnx = (sw / 4) - (btnw / 2)
    btny = 400

    stcol = RED
    stw = 100
    sth = 50
    stx = (sw * (3/4)) - (stw / 2)
    sty = 400

    recol = ORANGE
    rew = 100
    reh = 50
    rex = (sw / 2) - (rew / 2)
    rey = 500

    numx = 20
    numy = 10

    milsecList = [0]
    secList = [0]

    timerState = False

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(WHITE)

        cursor = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()

        startButton(btnx, btny, btnw, btnh, btncol, numx, numy)
        stopButton(stx, sty, stw, sth, stcol, numx, numy)
        resetButton(rex, rey, rew, reh, recol, numx, numy)
        showColon(numx, numy)
        milsecTime(milsecList)
        secTime(secList)

        if 50 < cursor[0] < 150 and 400 < cursor[1] < 450:
            btncol = LIGHTGREEN
            if clicked[0] == 1:
                timerState = True
        else:
            btncol = GREEN

        if 250 < cursor[0] < 350 and 400 < cursor[1] < 450:
            stcol = LIGHTRED
            if clicked[0] == 1:
                timerState = False
        else:
            stcol = RED

        #If clicked on the reset button
        if 150 < cursor[0] < 250 and 500 < cursor[1] < 550:
            recol = YELLOW
            if clicked[0] == 1:
                timerState = False
                milsecList[0] = 0
                secList[0] = 0
        else:
            recol = ORANGE

        if timerState == True:
            milsecList[0] += 1
        elif timerState == False:
            milsecList[0] += 0

        if milsecList[0] >= 100:
            milsecList[0] = 0
            secList[0] += 1

        pygame.display.update()
        clock.tick(95)

mainloop()
pygame.quit()
quit()
