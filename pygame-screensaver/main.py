#imports
import pygame 
import random 

#constants
SCREEN_SIZE = (1280, 720)
DVD_WIDTH = 300
RECT_SIZE =(DVD_WIDTH, int(DVD_WIDTH*822/1914))
FPS = 22
BACKGROUND = "blue"

#game state
run = True
pause = False
position = [0, 0]
velocity = [5, 9]
color = "black"       
dvd = pygame.image.load("ViKuT.png")
dvd = pygame.transform.scale(dvd, (DVD_WIDTH, int(DVD_WIDTH*822/1914)))

#functions:-

#drawing:   
def draw(screen , color, position ):
    """
    fill the bg and draw the rectangle
    """
    
    screen.fill(BACKGROUND)
    
    rect = dvd.get_rect(topleft=(position))
    
    screen.blit(dvd, rect) 
        
        
#event handler    
def events():
    
    global run
    global pause

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pause = not pause


#game logic:
               
def movements(position, velocity):
    """change position by adding velocity 
    """
    
    position[0] += velocity[0]
    position[1] += velocity[1]
    
    return position             


def collision(position, velocity, SCREEN_SIZE, RECT_SIZE):
    """
    check for collision:
        move the rectangle back to edge 
        change direction of velocity 
    """
    
    if position[0] <= 0:
        position[0] = 0
        velocity[0] *= -1
        
    elif position[0] + RECT_SIZE[0] >= SCREEN_SIZE[0]:
        position[0] = SCREEN_SIZE[0] - RECT_SIZE[0]
        velocity[0] *= -1
        
    if position[1] <= 0:
        position[1] = 0
        velocity[1] *= -1
        
    elif position[1] + RECT_SIZE[1] >= SCREEN_SIZE[1]:
        position[1] = SCREEN_SIZE[1] - RECT_SIZE[1]
        velocity[1] *= -1
        
    return velocity 

#Initialise Pygame
pygame.init()

#set title
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Pygame Screensaver")

#fps clock
clock = pygame.time.Clock()


#main loop
while run:
    
    events() 
    
    if pause != True:
        position = movements(position, velocity)
    
    draw(screen , color, position)
    
    pygame.display.update() #update display 
    
    velocity = collision(position, velocity, SCREEN_SIZE, RECT_SIZE) #tuple unpacking 
    
    clock.tick(FPS) 


#cleaning     
pygame.quit()    
    
   