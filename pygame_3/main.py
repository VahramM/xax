import pygame
pygame.init()
sc = pygame.display.set_mode((1930,1080))
fon_image = pygame.image.load("picture/14.png")
txt = pygame.image.load('picture/txt011.png')
start = pygame.image.load('picture/k01.png')
start_2 = pygame.image.load('picture/start_2.png')
exit_1 = pygame.image.load('picture/k00010.png')
exit_2 = pygame.image.load('picture/quit_2.png')
option_1 = pygame.image.load('picture/k0012.png')
option_2 = pygame.image.load('picture/option_1.png')

beep = pygame.mixer.music.load("song/songs.wav")
pygame.mixer.music.play(-1)
speed = 10
isJump = False
jumpCount = 10
clock = pygame.time.Clock()     
run = True
while run:
    sc.blit(fon_image,(0,0))
    sc.blit(txt,(500,30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    mouse = pygame.mouse.get_pos()
    if 830+200 > mouse[0] > 830 and 420+60 > mouse[1] > 420:
        sc.blit(start_2,(830,280))
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.stop()
            if event.button == 1:
                from run import*
    else:
        sc.blit(start,(830,280))
    if 820+280 > mouse[0] > 810 and 500+60 > mouse[1] > 500:
        sc.blit(option_2,(850,390))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                from option import*
    else:
        sc.blit(option_1,(850,390))
    if 880+180 > mouse[0] > 880 and 585+60 > mouse[1] > 585:
        sc.blit(exit_2,(880,525))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.quit()
    else:  
        sc.blit(exit_1,(880,525))
    pygame.time.delay(20)
    pygame.display.update()
