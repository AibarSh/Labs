import pygame

pygame.init()
W=800
H=600
x=400
y=300
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
running = True

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False 
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y>=25: y -= 10
        if pressed[pygame.K_DOWN] and y<=H-25: y += 10
        if pressed[pygame.K_LEFT] and x>=25: x -= 10
        if pressed[pygame.K_RIGHT] and x<=W-25: x += 10
        
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, "green", (x, y), 25)
        
        pygame.display.flip()   
        clock.tick(60)