import pygame


def option():
    sc = pygame.display.set_mode((1930,1080))
    fon_image = pygame.image.load("picture/14.png")
    text_image = pygame.image.load("picture/txt02.png")
    nosound = pygame.image.load("picture/nosound.png")
    sound1 = pygame.image.load("picture/sound1.png")
    sound2 = pygame.image.load("picture/sound2.png")
    sound3 = pygame.image.load("picture/sound3.png")
    nosound1 = pygame.image.load("picture/nosound1.png")
    sound11 = pygame.image.load("picture/sound11.png")
    sound22 = pygame.image.load("picture/sound22.png")
    sound33 = pygame.image.load("picture/sound33.png")
    WASD = pygame.image.load("picture/WASD.png")
    WASD1 = pygame.image.load("picture/WASD1.png")
    arrow = pygame.image.load("picture/arrow.png")
    arrow1 = pygame.image.load("picture/arrow1.png")
    back_button = pygame.image.load("picture/back.png")
    back_button1 = pygame.image.load("picture/back1.png")
    clock = pygame.time.Clock()
    vol = 1.0
    flpause = False
    run = True
    op = False
    while run:
        sc.blit(fon_image,(0,0))
        sc.blit(text_image,(340,50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        mouse = pygame.mouse.get_pos()
        if 700+77 > mouse[0] > 700  and 400+68 > mouse[1] > 400:
            sc.blit(nosound1,(700,400))
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    flpause = not flpause
                    if flpause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
        else:
            sc.blit(nosound,(700,400))
        if 800+68 > mouse[0] > 800 and 405+60 > mouse[1] > 405:
            sc.blit(sound11,(800,405))
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    vol+=0.5
        else:
            sc.blit(sound1,(800,405))
        if 900+79 > mouse[0] > 900 and 400+70 > mouse[1] > 400:
            sc.blit(sound22,(900,400))
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    vol+=1
        else:
            sc.blit(sound2,(900,400))
        if 1000+68 > mouse[0] > 1000 and 410+60 > mouse[1]  > 410:
            sc.blit(sound33,(1000,410))
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    vol+=2
        else:
            sc.blit(sound3,(1000,410))
        if 1120+68 > mouse[0] > 1120 and 600+80 > mouse[1]  > 600:
            sc.blit(back_button1,(1120,600))
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    run = False
        else:
            sc.blit(back_button,(1120,600))
        
        sc.blit(WASD,(650,500))
        sc.blit(arrow,(890,490))
        pygame.display.update()
