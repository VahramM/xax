import pygame
import time
pygame.init()

screen_width = 1920
screen_height = 1080
win = pygame.display.set_mode((1920,1080))
pygame.mixer_music.load("song/bg_song.mp3")
pygame.mixer.music.play(-1)
player = pygame.image.load("picture/player/Woodcutter1.png")
bg = pygame.image.load("picture/8.png")
kill_pl = [pygame.image.load("picture/Sprite-1.png")]
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

pygame.mixer.music.load("song/5.mp3")
pygame.mixer.music.play(-1)


tile_size = 60





def draw_grid():
    for line in range(0, 60):
       pass

class World():
    def __init__(self, data):
        self.tile_list = []

        #load images
        dirt_img = pygame.image.load('Tiles/Tile_12.png')
        grass_img = pygame.image.load('Tiles/Tile_02.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            win.blit(tile[0], tile[1])

world_data = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0], 
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

world = World(world_data)



half = [pygame.image.load("picture/kyanqer1.png"),
        pygame.image.load("picture/kyanqer2.png"),
        pygame.image.load("picture/kyanqer3.png"),
        pygame.image.load("picture/kyanqer4.png"),
        pygame.image.load("picture/kyanqer5.png"),
        pygame.image.load("picture/kyanqer6.png"),
        pygame.image.load("picture/kyanqer7.png"),
        pygame.image.load("picture/kyanqer8.png")]




p = 700
o = 520 
x = 50
y = 520
speed = 10
isJump = False
jumpCount = 10
anim_left = [pygame.image.load("picture/player/Woodcutter_run_left_1.png"),
              pygame.image.load("picture/player/Woodcutter_run_left_2.png"),
              pygame.image.load("picture/player/Woodcutter_run_left_3.png"),
              pygame.image.load("picture/player/Woodcutter_run_left_4.png"),
              pygame.image.load("picture/player/Woodcutter_run_left_5.png"),
              pygame.image.load("picture/player/Woodcutter_run_left_6.png")]


anim_right = [
              pygame.image.load("picture/player/Woodcutter_run11.png"),
              pygame.image.load("picture/player/Woodcutter_run22.png"),
              pygame.image.load("picture/player/Woodcutter_run33.png"),
              pygame.image.load("picture/player/Woodcutter_run44.png"),
              pygame.image.load("picture/player/Woodcutter_run55.png"),
              pygame.image.load("picture/player/Woodcutter_run66.png"),
              ]

anim_attack1 = [pygame.image.load("picture/player/Woodcutter_death-11.png"),
              pygame.image.load("picture/player/Woodcutter_death-22.png"),
              pygame.image.load("picture/player/Woodcutter_death-33.png"),
              pygame.image.load("picture/player/Woodcutter_death-44.png"),
              pygame.image.load("picture/player/Woodcutter_death-55.png"),
              pygame.image.load("picture/player/Woodcutter_death-66.png"),]
left = False
right = False
attack = False
death = False
animdeath = 0
animCount = 0
animhalf = 0

clock = pygame.time.Clock()      
run = True
textX = 10
textY = 10
def show_score(x,y):
    score = font.render("Score: "+str(score_value),True,(255,255,255))
    win.blit(score,(x,y))

while(run):

    

    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT]:
        x += speed
        right = True
        left = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            attack = True
    elif animhalf == 7:
        death = True
    else:
        left = False
        right = False
        attack = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            score_value += 1
     
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    win.blit(bg, (0,0))

    world.draw()

    draw_grid()
    
    win.blit(half[0], (50, 50))
    a = 0
    if animCount + 1 >=30:
        animCount = 0
    elif right:
        win.blit(anim_right[animCount // 5], (x, y))
        animCount += 1
    elif left:
        win.blit(anim_left[animCount // 5], (x, y))
        animCount += 1
    
    elif attack:
        if keys[pygame.K_SPACE]:
            win.blit(anim_attack1[a // 5], (x, y))
            a += 1
    else:
        win.blit(player, (x, y))
    
    if x == p:
        if y == o:
            win.blit(kill_pl[0],(p,o))
            half[0] = half[1 + animhalf]
            animhalf += 1
            if animhalf == 7:
                pygame.quit()
    else:
        win.blit(kill_pl[0],(p,o))
        show_score(x,y)


            
    
    pygame.display.update() 
    



pygame.quit()
