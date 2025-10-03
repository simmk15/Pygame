import pygame
pygame.init()
screen_width,screen_height=500,500
display_surface=pygame.display.set_mode((screen_width,screen_height))
color = (58,58,58)
display_surface.fill(color)
pygame.display.set_caption('My first game screen')
coding_image=pygame.transform.scale(
    pygame.image.load('code.png').convert_alpha(),(300,300))
coding_rect=coding_image.get_rect(center=(screen_width//2,screen_height//2-30))
def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
          if event.type==pygame.QUIT:
            running=False
        display_surface.blit(coding_image,coding_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__=='__main__':
   game_loop()