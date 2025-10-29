import pygame
pygame.init()
window=pygame.display.set_mode((400,400))
window.fill((255,255,255))
green=(0,255,0)
pygame.draw.circle(window,green,(300,300),50)
pygame.draw.circle(window,green,(100,100),50,3)
pygame.display.update()
running=True
while running:
    for evetn in pygame.event.get():
        if events.type==pygame.QUIT:
            running=False
pygame.quit()