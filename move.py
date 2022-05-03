import pygame
from main import menu
import cv2
def intro():
    pygame.mixer.music.load('song/desert_2.mp3')
    pygame.mixer.music.play(0)
    video = cv2.VideoCapture("2.mp4")
    success, video_image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)

    window = pygame.display.set_mode(video_image.shape[1::-1])
    clock = pygame.time.Clock()

    run = success
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        success, video_image = video.read()
        if success:
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")

        else:
            run = False
            menu()
        window.blit(video_surf, (0, 0))
        pygame.display.flip()

    pygame.quit()
    exit()
intro()
