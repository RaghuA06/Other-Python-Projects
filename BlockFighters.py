import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHTYELLOW = (255, 255, 150)
GREEN = (0, 255, 0)
LIGHTBLUE = (0, 205, 205)
DARKORANGE = (255,127,0)

groundImg = pygame.image.load("Blockfightersbackground.png")

sw = 800
sh = 600

s = pygame.display.set_mode([sw, sh])
pygame.display.set_caption("Block Fighters")
clock = pygame.time.Clock()

FPS = 75

def player(px, py):
    pygame.draw.rect(s, RED, [px, py, 100, 100])

def bullet(bx, py):
    pygame.draw.rect(s, YELLOW, [bx, py, 50, 20])

def opponent(ox, oy):
    pygame.draw.rect(s, LIGHTBLUE, [ox, oy, 100, 100])

def oppBullet(bbx, oy):
    pygame.draw.rect(s, GREEN, [bbx, oy, 50, 20])

def gameEnd(pscr, opscr, lsr):

    ended = True

    while ended:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    mainLoop()

        s.fill(LIGHTYELLOW)

        if lsr == "Red Block":
            lsr_color = RED
        elif lsr == "Blue Block":
            lsr_color = LIGHTBLUE

        myFont = pygame.font.SysFont("Arial", 72)
        TextSurf = myFont.render("Game Over: " + lsr + " LOST", False, lsr_color)
        s.blit(TextSurf, [0, 0])

        again = pygame.font.SysFont("Arial", 48)
        textsurf = again.render("Press R to play again", False, RED)
        s.blit(textsurf, [0, (sh / 2) - 48])

        pygame.display.update()

def scoresFighters(pscr, opscr):
    #Player Score
    scrfont = pygame.font.SysFont("Arial", 32)
    TextSurf = scrfont.render("Score: " + str(pscr), True, RED)
    s.blit(TextSurf, [0, 0])

    #Opponent Score
    opscrfont = pygame.font.SysFont("Arial", 32)
    textsurf = opscrfont.render("Score: " + str(opscr), True, BLACK)
    s.blit(textsurf, [800 - 120, 0])

def playerSheild(psw, psh, pscol):
    pygame.draw.rect(s, pscol, [250, 100, psw, psh])

def opponentShield(osw, osh, oscol):
    pygame.draw.rect(s, oscol, [450, 400, osw, osh])

def mainLoop():

    playerx = (sh / 2) - 250
    playery = (sh / 2) - 50
    cy = 0

    bulx = playerx + 50
    buly = playery + 50
    bullet_change = 0
    bullet_state = True

    ox = (sh / 2) + 350
    oy = (sh / 2) - 50
    oyc = 0

    bbx = ox
    opbullet_change = 0
    opbullet_state = True

    playerscore = 0
    opponentscore = 0

    pswidth = 100
    psheight = 100
    pscolor = DARKORANGE

    oswidth = 100
    osheight = 100
    oscolor = DARKORANGE

    finish = False

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    oyc = -20
                if event.key == pygame.K_DOWN:
                    oyc = 20
                if event.key == pygame.K_w:
                    cy = -20
                if event.key == pygame.K_s:
                    cy = 20
                if event.key == pygame.K_SPACE:
                    if bullet_state == True:
                        bulx = playerx
                        bullet_change = 50
                if event.key == pygame.K_o:
                    if opbullet_state == True:
                        bbx = ox
                        opbullet_change = -50
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    cy = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    oyc = 0

        playery += cy
        oy += oyc
        bulx += bullet_change
        bbx += opbullet_change

        s.blit(groundImg, [0, 0])
        pygame.draw.line(s, BLACK, [sw / 2, 0], [sw / 2, sh], 2)

        bullet(bulx, playery + 50)
        oppBullet(bbx, oy + 50)

        player(playerx, playery)
        opponent(ox, oy)

        playerSheild(pswidth, psheight, pscolor)
        opponentShield(oswidth, osheight, oscolor)

        scoresFighters(playerscore, opponentscore)

        #Logic Code for player bullet
        if playerx + 50 < bulx < sw:
            bullet_state = False
        elif bulx == playerx + 50:
            bullet_state = True
        elif bulx > sw:
            bullet_state = True

        #Logic Code for opponent bullet
        if 0 < bbx < ox:
            opbullet_state = False
        elif bbx == ox:
            opbullet_state = True
        elif bbx < 0:
            opbullet_state = True

        #Player bullet collision with opponent
        if playery + 50 > oy and playery + 50 < oy + 100:
            if bulx > ox and bulx < ox + 100 or bulx + 50 > ox and bulx + 50 < ox + 100:
                bulx = playerx + 50
                bullet_change = 0
                playerscore += 1

        #Opponent bullet collision with player
        if oy + 50 > playery and oy + 50 < playery + 100:
            if bbx > playerx and bbx < playerx + 100 or bbx + 50 > playerx and bbx + 50 < playerx + 100:
                bbx = ox
                opbullet_change = 0
                opponentscore += 1

        #Player bullet collision with playersheild
        if playery + 50 > 100 and playery + 50 < 100 + 100:
            if bulx > 250 and bulx < 250 + 100 or bulx + 50 > 250 and bulx + 50 < 250 + 100:
                bulx = playerx + 50
                bullet_change = 0

        #Player bullet collision with opponent sheild
        if playery + 50 > 400 and playery + 50 < 400 + 100:
            if bulx > 450 and bulx < 450 + 100 or bulx + 50 > 450 and bulx + 50 < 450 + 100:
                bulx = playerx + 50
                bullet_change = 0

        #Opponent bullet collision with playershield
        if oy + 50 > 100 and oy + 50 < 100 + 100:
            if bbx > 250 and bbx < 250 + 100 or bbx + 50 > 250 and bbx + 50 < 250 + 100:
                bbx = ox
                opbullet_change = 0

        #Opponent bullet collision with opponentsheild
        if oy + 50 > 400 and oy + 50 < 400 + 100:
            if bbx > 450 and bbx < 450 + 100 or bbx + 50 > 450 and bbx + 50 < 450 + 100:
                bbx = ox
                opbullet_change = 0

        if playery < 0 or playery > sh - 100:
            cy = 0
        if oy < 0 or oy > sh - 100:
            oyc = 0

        if playerscore == 50:
            loser = "Blue Block"
            gameEnd(playerscore, opponentscore, loser)
        if opponentscore == 50:
            loser = "Red Block"
            gameEnd(playerscore, opponentscore, loser)

        pygame.display.update()
        clock.tick(FPS)

mainLoop()
pygame.quit()
quit()
