import pygame
import math
import time

pygame.init()
window_size = (730, 730)
screen = pygame.display.set_mode(window_size)
center = window_size[0]/2, window_size[1]/2
clock = pygame.image.load('Clock2.png')
clock = pygame.transform.scale(clock, (730,730))
Icon = pygame.image.load('Clock.jpg')
pygame.display.set_icon(Icon)
pygame.display.set_caption("Clock")
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    screen.blit(clock, (0, 0))

    current_time = time.localtime()
    hours = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    hours_angle = (hours % 12 + minute / 60) * 360 / 12
    minute_angle = (minute + second / 60) * 360 / 60
    second_angle = second * 360 / 60

    hours_hand_length = 360 * 0.5
    hours_hand_end = (center[0] + hours_hand_length * math.sin(math.radians(hours_angle)),
                       center[1] - hours_hand_length * math.cos(math.radians(hours_angle)))
    pygame.draw.line(screen, "green", center, hours_hand_end, 8)

    minute_hand_length = 360 * 0.7
    minute_hand_end = (center[0] + minute_hand_length * math.sin(math.radians(minute_angle)),
                       center[1] - minute_hand_length * math.cos(math.radians(minute_angle)))
    pygame.draw.line(screen, "white", center, minute_hand_end, 5)

    second_hand_length = 360 * 0.8
    second_hand_end = (center[0] + second_hand_length * math.sin(math.radians(second_angle)),
                       center[1] - second_hand_length * math.cos(math.radians(second_angle)))
    pygame.draw.line(screen, "yellow", center, second_hand_end, 3)
    

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
