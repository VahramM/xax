import pygame, sys
from run import run
from option import option
from info import inf

pygame.init()
def menu():
    h = 1920
    w = 1080
    sc = pygame.display.set_mode((h,w))
    fon_image = pygame.image.load("1.png")
    txt = pygame.image.load('picture/txt011.png')
    start = pygame.image.load('picture/k01.png')
    start_2 = pygame.image.load('picture/start_2.png')
    exit_1 = pygame.image.load('picture/k00010.png')
    exit_2 = pygame.image.load('picture/quit_2.png')
    option_1 = pygame.image.load('picture/k0012.png')
    option_2 = pygame.image.load('picture/option_1.png')
    info = pygame.image.load('picture/info.png')
    info2 = pygame.image.load('picture/info2.png')

    beep = pygame.mixer.music.load("song/menu_song.mp3")
    pygame.mixer.music.play(-1)
    speed = 10
    isJump = False
    jumpCount = 10
    clock = pygame.time.Clock()     
    quitt = False
    while True:
        
        sc.blit(fon_image,(0,0))
        sc.blit(txt,(500,30))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
        
            if 820+280 > mouse[0] > 810 and 500+60 > mouse[1] > 500:
                sc.blit(option_2,(850,390))
                if event.type == pygame.MOUSEBUTTONDOWN:
                        option()
            else:
                sc.blit(option_1,(850,390))
            if 830+200 > mouse[0] > 830 and 420+60 > mouse[1] > 420:
                sc.blit(start_2,(830,280))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        run()
                        pygame.mixer.music.pause()
            else:
                sc.blit(start,(830,280))
        
            if 880+180 > mouse[0] > 880 and 660+60 > mouse[1] > 660:
                sc.blit(exit_2,(875,595))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pygame.quit()
                        sys.exit()
            else:  
                sc.blit(exit_1,(875,595))

            if 875+180 > mouse[0] > 875 and 585+60 > mouse[1] > 585:
                sc.blit(info2,(875,470))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        inf()
            else:  
                sc.blit(info,(875,470))
                
            pygame.time.delay(20)
            pygame.display.update()
            

