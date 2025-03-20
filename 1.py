import pygame
from datetime import datetime
import time

pygame.init()

background = pygame.image.load("images/clock.png")
minute_hand = pygame.image.load("images/rightarm.png")
second_hand = pygame.image.load("images/leftarm.png")
WIDTH, HEIGHT = background.get_size()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

CENTER = (WIDTH // 2, HEIGHT // 2)

def rotate_image(image, angle):

    rotated_image = pygame.transform.rotate(image, -angle)

    rect = rotated_image.get_rect(center=CENTER)

    return rotated_image, rect

running = True

while running:

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    now = datetime.now()
    minute_angle = now.minute * 6
    second_angle = now.second * 6


    rotated_minute, min_rect = rotate_image(minute_hand, minute_angle)
    rotated_second, sec_rect = rotate_image(second_hand, second_angle)

    screen.blit(rotated_minute, min_rect.topleft)
    screen.blit(rotated_second, sec_rect.topleft)

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    time.sleep(1)

pygame.quit()