import pygame

def inf():
    pygame.init()    
    sc = pygame.display.set_mode((1930,1080))
    fon_image = pygame.image.load("picture/14.png")
    text_image = pygame.image.load("picture/infotext.png")
    back_button = pygame.image.load("picture/back.png")
    back_button1 = pygame.image.load("picture/back1.png")
    clock = pygame.time.Clock()
    run = True
    while run:
        sc.blit(fon_image,(0,0))
        sc.blit(text_image,(340,50))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if 1168 > mouse[0] > 1120 and 720 > mouse[1]  > 650:
            sc.blit(back_button1,(1120,650))
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    run = False
        else:
            sc.blit(back_button,(1120,650))

        pygame.display.update()



        
