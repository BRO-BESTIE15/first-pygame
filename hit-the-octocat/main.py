import pygame
import random
pygame.init()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1280
FPS = 60
RECT_WIDTH = 200
RECT_HEIGHT = 100
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
x= 0
y = 200
run = True
start_time = None
speed = 5
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 50)
while run:
    screen.fill("blue")
    if score < 5:
        rect =pygame.draw.rect(screen, 'red' , (x ,y, RECT_WIDTH, RECT_HEIGHT))
    
    score_text = font.render(f"Score: {score}", True, 'black')
    last_text = font.render("GAME OVER", True, "white")
    screen.blit(score_text, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if score < 5:
                if rect.collidepoint(event.pos):
                    score += 1
                    x = random.randint(0, SCREEN_WIDTH - RECT_WIDTH)
                    y = random.randint(0, SCREEN_HEIGHT - RECT_HEIGHT)
                
    
            
         
    if score == 5:
    	screen.blit(last_text, (SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.05))
    	
    	if start_time is None:
    		start_time = pygame.time.get_ticks()
    		
    	if pygame.time.get_ticks() - start_time >= 5000:
    	    run = False
    	    
    pygame.display.update()

    clock.tick(FPS)   

pygame.quit()

