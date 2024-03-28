import pygame

pygame.init()
songs=["Never Gonna Give You Up.mp3","Алла Пугачева - Арлекино.mp3", "Personal Jesus.mp3"]
pics=["NGGYU.jpg", "Арлекино.jpg", "PJ.jpg"]
x=0
W=500
H=500
screen = pygame.display.set_mode((W, H))
screen.fill((0,0,0))
pygame.display.set_caption("Music player")
pygame.display.set_icon(pygame.image.load("MusPlayer.png"))
# pygame.display.update()

pygame.mixer.music.load(songs[x])
start=False
stop= True
running = True
while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                if event.type== pygame.KEYDOWN:
                        pressed = pygame.key.get_pressed()
                        if pressed[pygame.K_SPACE]:
                                if stop==True:
                                        if start==False:
                                                pygame.mixer.music.play()
                                                start=True
                                                cov=pygame.image.load(pics[x]).convert()
                                                cover=pygame.transform.scale(cov, (300, 300))
                                                coverr=cover.get_rect(center=(W/2, H/3))
                                                screen.blit(cover, coverr)
                                        else:
                                                pygame.mixer.music.unpause()
                                        stop=False
                                else:
                                        pygame.mixer.music.pause()
                                        stop=True
                        if pressed[pygame.K_LEFT]:
                                if x!=0:
                                        x-=1
                                else:
                                        x=len(songs)-1        
                                cov=pygame.image.load(pics[x]).convert()
                                cover=pygame.transform.scale(cov, (300, 300))
                                coverr=cover.get_rect(center=(W/2, H/3))
                                screen.blit(cover, coverr)
                                pygame.mixer.music.load(songs[x])
                                pygame.mixer.music.play()
                        if pressed[pygame.K_RIGHT]:
                                if x!=len(songs)-1:
                                        x+=1
                                else:
                                        x=0        
                                cov=pygame.image.load(pics[x]).convert()
                                cover=pygame.transform.scale(cov, (300, 300))
                                coverr=cover.get_rect(center=(W/2, H/3))
                                screen.blit(cover, coverr)
                                pygame.mixer.music.load(songs[x])
                                pygame.mixer.music.play()
                pygame.display.update()
pygame.quit()