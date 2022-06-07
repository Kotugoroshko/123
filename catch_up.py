import pygame
import os

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Catch up")

back = os.path.join(os.path.abspath(__file__ + "/.."), "background1.png")
back = pygame.transform.scale(pygame.image.load(back), (800,600))

FPS = pygame.time.Clock()

x1=150
y1=150
x2 = 600
y2 = 300
speed = 10

sprite1 = os.path.join(os.path.abspath(__file__ + "/.."), "sprite1.png")
sprite1 = pygame.transform.scale(pygame.image.load(sprite1), (100,100))
sprite2 = os.path.join(os.path.abspath(__file__ + "/.."), "sprite2.png")
sprite2 = pygame.transform.scale(pygame.image.load(sprite2), (100,100))
#основний цикл гри
game = True
while game :
    window.blit(back, (0,0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y1>5:
        y1-=speed
    if keys[pygame.K_s] and y1<500:
        y1 +=speed
    if keys[pygame.K_a] and x1>5:
        x1 -=speed
    if keys[pygame.K_d] and x1<700:
        x1 +=speed
    
    if keys[pygame.K_UP] and y2>5:
        y2-=speed
    #DOWN
    #LEFT
    #RIGHT
    pygame.display.flip()
    FPS.tick(60)
    
