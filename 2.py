import pygame
import os

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")

pygame.mixer.init()
font = pygame.font.Font(None, 36)

audio_folder = "audio"
playlist = [os.path.join(audio_folder, track) for track in os.listdir(audio_folder) if track.endswith(".mp3")]


current_track = 0
is_playing = True

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    return True

is_playing = play_music()

running = True
while running:
    screen.fill((30, 30, 30))
    
    track_name = os.path.basename(playlist[current_track])
    status_text = "Играет" if is_playing else "На паузе"
    
    track_surface = font.render(f"Трек: {track_name}", True, (255, 255, 255))
    status_surface = font.render(f"Статус: {status_text}", True, (255, 255, 255))
    
    screen.blit(track_surface, (20, 100))
    screen.blit(status_surface, (20, 150))
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause()
                    is_playing = True
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                is_playing = False
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(playlist)
                is_playing = play_music()
            elif event.key == pygame.K_p:
                current_track = (current_track - 1) % len(playlist)
                is_playing = play_music()

pygame.quit()
