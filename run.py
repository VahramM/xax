import pygame
def run():
    pygame.init()

    screen_width = 1920
    screen_height = 1080
    win = pygame.display.set_mode((1920,1080))
    pygame.mixer_music.load("song/bg_song.mp3")
    pygame.mixer.music.play(-1)



    player = pygame.image.load("picture/player/Idle/1.png")
    player_1 = pygame.image.load("picture/player/Idle/1_1.png")
    player_location = [1200, 1590]
    widht = player.get_width()
    height = player.get_height()
    dy = 0
    dx = 0
    player_rect = player.get_rect()


    b = pygame.image.load("b.png")
    bg = pygame.image.load("background/desert.png")
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf',32)

    pygame.mixer.music.load("song/dune_run.mp3")
    pygame.mixer.music.play(-1)
    class Bullet:
        def __init__(self, mx, my, sp):
            self.mx = mx
            self.my = my
            self.sp = sp
            self.vel = 8 * sp

        def mo(self):
            self.mx += self.vel
            if self.mx:
                pygame.draw.circle(win,(255,0,0),(self.mx, self.my),3)
                return True
            else:
                return False
    colldown = 0
    tile_size = 90
    dirt_image = pygame.image.load('desert/d1(7).png')
    grass_image = pygame.image.load('desert/d1(1).png')
    dirt_2_image = pygame.image.load('desert/d1(8).png')
    dirt_3_image = pygame.image.load('desert/d1(10).png')
    dirt_4_image = pygame.image.load('desert/d1(11).png')
    dirt_5_image = pygame.image.load('desert/d1(12).png')
    dirt_6_image = pygame.image.load('desert/d1(13).png')
    dirt_7_image = pygame.image.load('desert/d1(14).png')
    dirt_8_image = pygame.image.load('desert/d1(15).png')
    TILE_SIZE = grass_image.get_width()

    
    

    def load_map(path):
        f = open(path + '.txt','r')
        data = f.read()
        f.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))
        return game_map

    game_map = load_map('map')


    def collision_test(rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(rect, movement, tiles):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types


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
    anim_jump = [pygame.image.load("picture/player/Jump/0.png"),
                 pygame.image.load("picture/player/Jump/1.png")]

    
    anim_right = [pygame.image.load("picture/player/Run/0.png"),
                  pygame.image.load("picture/player/Run/1.png"),
                  pygame.image.load("picture/player/Run/2.png"),
                  pygame.image.load("picture/player/Run/3.png"),
                  pygame.image.load("picture/player/Run/4.png"),
                  pygame.image.load("picture/player/Run/5.png")]

    
    anim_left = [
                  pygame.image.load("picture/player/Run/0_0.png"),
                  pygame.image.load("picture/player/Run/1_1.png"),
                  pygame.image.load("picture/player/Run/2_2.png"),
                  pygame.image.load("picture/player/Run/3_3.png"),
                  pygame.image.load("picture/player/Run/4_4.png"),
                  pygame.image.load("picture/player/Run/5_5.png"),
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
    running = True
    textX = 10
    textY = 10
    def show_score(x,y):
        score = font.render("Score: "+str(score_value),True,(0,0,0))
        win.blit(score,(x,y))
    player_rect = pygame.Rect(1000, 500, player.get_width(), player.get_height())
    test_rect = pygame.Rect(100,100,100,50)
    player_y_momentum = 0
    player_y_jump = 0
    air_timer = 0
    scroll = [0,0]
    all_btn_bullets = []
    plmove = "right"
    tt = dirt_8_image.get_rect()
    while running:
        win.blit(bg, (0,0))
        clock.tick(60)
        scroll[0] += (player_rect.x-scroll[0] - 600)
        scroll[1] += (player_rect.y-scroll[1] - 800)


        
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()

        tile_rects = []
        br = 0
        for row in game_map:
            er = 0
            for tile in row:
                if tile == '1':
                    win.blit(dirt_image, (er * 60 -scroll[0], br * 60 - scroll[1]))
                if tile == '2':
                    win.blit(grass_image, (er * 60 - scroll[0], br * 60 - scroll[1]))
                if tile == '3':
                    win.blit(dirt_2_image, (er * 60 - scroll[0], br * 60 - scroll[1]))
                if tile == '4':
                    win.blit(dirt_3_image, (er * 60 - scroll[0], br * 60 - scroll[1]))
                if tile == '5':
                    win.blit(dirt_4_image, (er * 60 - scroll[0], br * 60 - scroll[1]))
                if tile == '6':
                    win.blit(dirt_5_image, (er * 60 - scroll[0], br * 60 - scroll[1]))
                if tile == '7':
                    win.blit(dirt_6_image, (er * 60 - scroll[0], br * 60 - scroll[1]))
                if tile == '8':
                    win.blit(dirt_7_image, (er * 60 - scroll[0], br * 60 - scroll[1]))
                if tile == '9':
                    win.blit(dirt_8_image, (er * 60 - scroll[0], br * 60 - scroll[1]))
                if tile != '0':
                    tile_rects.append(pygame.Rect(er * 60, br * 60, 60, 60))
                er += 1
            br += 1
        
        player_movement = [0, 0]
        if right:
            player_movement[0] += 10
        if left:
            player_movement[0] -= 10
        player_movement[1] += player_y_momentum
        player_y_momentum += 0.3
        
        if player_y_momentum > 100:
            player_y_momentum = 100
            
        
        player_rect, collisions = move(player_rect, player_movement, tile_rects)
        if collisions['bottom']:
            player_y_momentum = 0
            air_timer = 0
        else:
            air_timer += 10

        keys = pygame.key.get_pressed()
        if not colldown:
            if keys[pygame.K_x]:
                if plmove == "right":
                    sp = 1
                else:
                    sp = -1
                all_btn_bullets.append(Bullet(player_rect[1]+250,player_rect[2]+765, sp))
                colldown = 30
        else:
            colldown -= 1
        for bullet in all_btn_bullets:
            if not bullet.mo():
                all_btn_bullets.remove(bullet)
        if keys[pygame.K_q]:
            running = False
            pygame.mixer.music.pause()
        if keys[pygame.K_LEFT]:
            left = True
            right = False
            plmove = "left"
        elif keys[pygame.K_RIGHT]:
            right = True
            left = False
            plmove = "right"
        elif animhalf == 7:
            death = True
        else:
            left = False
            right = False
            animCount = 0
        if keys[pygame.K_UP]:
            if air_timer < 30:
                player_y_momentum = -8
     
        win.blit(half[0], (50, 50))
        a = 0
        if animCount + 1 >=30:
            animCount = 0
        elif right:
            win.blit(anim_right[animCount // 5], (player_rect.x-scroll[0],player_rect.y-scroll[1]))
            animCount += 1
        elif left:
           
            win.blit(anim_left[animCount // 5], (player_rect.x-scroll[0],player_rect.y-scroll[1]))
            animCount += 1
        elif attack:
            if keys[pygame.K_SPACE]:
                win.blit(anim_attack1[a // 5], (player_rect.x-scroll[0],player_rect.y-scroll[1]))
                a += 1
        else:
            if plmove == "right":
                win.blit(player, (player_rect.x-scroll[0],player_rect.y-scroll[1]))
            else:
                win.blit(player_1, (player_rect.x-scroll[0],player_rect.y-scroll[1]))
                

        if player_rect.y > 1920:
            return run()


        if player_rect[0] >= 4200 and player_rect[0] <= 4400:
            if player_rect[1] <= 360 and player_rect[1] >= 360:
                half[0] = half[1 + animhalf]
                animhalf += 1
                if animhalf == 7:
                    return run()

        pygame.display.update()
