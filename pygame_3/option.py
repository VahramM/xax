import pygame
pygame.init()
sc = pygame.display.set_mode((1930,1080))
fon_image = pygame.image.load("picture/14.png")
text_image = pygame.image.load("picture/txt02.png")
nosound = pygame.image.load("picture/nosound.png")
sound1 = pygame.image.load("picture/sound1.png")
sound2 = pygame.image.load("picture/sound2.png")
sound3 = pygame.image.load("picture/sound3.png")
back_button = pygame.image.load("picture/back.png")
nosound1 = pygame.image.load("picture/nosound1.png")
sound11 = pygame.image.load("picture/sound11.png")
sound22 = pygame.image.load("picture/sound22.png")
sound33 = pygame.image.load("picture/sound33.png")
clock = pygame.time.Clock()
vol = 1.0
flpause = False
run = True
while run:
    sc.blit(fon_image,(0,0))
    sc.blit(text_image,(340,50))
    sc.blit(nosound,(740,400))
    sc.blit(sound1,(840,400))
    sc.blit(sound2,(940,400))
    sc.blit(sound3, (1040,405))
    sc.blit(back_button,(1120,600))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        sc.blit(back_button,(1120,600))
        if event.button==1:
            from main import *
    mouse = pygame.mouse.get_pos()  
    if 740+200 > mouse[0] > 740 and 420+60 > mouse[1] > 420:
        sc.blit(nosound1,(740,400))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                flpause = not flpause
                if flpause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
    else:
        sc.blit(nosound,(740,400))
    if 840+280 > mouse[0] > 810 and 500+60 > mouse[1] > 500:
        sc.blit(sound11,(840,400))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                vol+=0.5
    else:
        sc.blit(sound1,(840,400))
    if 940+180 > mouse[0] > 880 and 585+60 > mouse[1] > 585:
        sc.blit(sound22,(940,400))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                vol+=1
    else:
        sc.blit(sound2,(940,400))
    if 1040+180 > mouse[0] > 880 and 585+60 > mouse[1] > 585:
        sc.blit(sound33,(1040,400))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                vol+=2
    else:
        sc.blit(sound3,(1040,400))
    
        
        
    pygame.display.update()
