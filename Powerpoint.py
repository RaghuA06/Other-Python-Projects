import pygame

pygame.init()
pygame.font.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
orange = (255, 180, 0)

wn_width = 800
wn_height = 600

wn = pygame.display.set_mode((wn_width, wn_height))
pygame.display.set_caption("Powerpoint In Python")
clock = pygame.time.Clock()

def mainslide():

    main_slide = True

    while main_slide:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    slide2()
            if event.type == pygame.KEYUP:
                continue

        wn.fill(orange)

        myfont = pygame.font.SysFont("Comic Sans MS", 72)
        TextSurf = myfont.render("Welcome To My", False, black)
        wn.blit(TextSurf, ((wn_width / 2) - 250, (wn_height / 2) - 100))

        my_font = pygame.font.SysFont("Comic Sans MS", 72)
        Text_Surf = my_font.render("Powerpoint", False, black)
        wn.blit(Text_Surf, ((wn_width / 2) - 150, (wn_height / 2) - 100 + 72))

        name = pygame.font.SysFont("Comic Sans Ms", 48)
        TextSurface = name.render("By: Raghu Alluri", False, black)
        wn.blit(TextSurface, (400, 500))

        pygame.display.update()
        clock.tick(30)

def slide2():

    slide_2 = True

    while slide_2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mainslide()
            if event.type == pygame.KEYUP:
                continue

        wn.fill(white)

        text = pygame.font.SysFont("Calibri", 24)
        TextSurf = text.render("This is a sample sentence for testing of this slide", False, black)
        wn.blit(TextSurf, (0, 0))

        pygame.display.update()
        clock.tick(30)

def slide3():

    slide_3 = True

mainslide()
pygame.quit()
quit()
