#imports
import pygame 
import random 

#constants
SCREEN_SIZE = (1280, 720)
RECT_SIZE =(200, 100)
FPS = 60
BACKGROUND = 'blue'
COLORS = ("black", "white", "red", "green", "yellow", "cyan", "magenta", "pink", "hotpink", "deeppink", "crimson", "maroon", "salmon", "coral", "navy", "skyblue", "deepskyblue", "dodgerblue", "royalblue", "steelblue", "turquoise", "lime", "limegreen", "forestgreen", "seagreen", "springgreen", "olive", "purple", "violet", "indigo", "orchid", "plum", "lavender")

#game state
run = True
position = [0, 0]
velocity = [5, 9]
color = "black"       

#functions:-

#helper func:
def random_color():
    """
    returns a color form tuple using random module 
    """
    return random.choice(COLORS)
    
#drawing:   
def draw(screen , color, position , RECT_SIZE):
    """
    fill the bg and draw the rectangle
    """
    screen.fill(BACKGROUND)
    pygame.draw.rect(screen , color, (position , RECT_SIZE)) 
        
#event handler    
def events():
    """
    handle events and change the global variable
    """
    global run
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#game logic:
                
def movements(position, velocity):
    """change position by adding velocity 
    """
    position[0] += velocity[0]
    position[1] += velocity[1]
    return position             

def bounce_color(position, velocity, color, SCREEN_SIZE, RECT_SIZE):
    """
    check for collision:
        move the rectangle back to edge 
        change direction of velocity 
        change color
    """
    if position[0] <= 0:
        position[0] = 0
        velocity[0] *= -1
        color = random_color()
        
    elif position[0] + RECT_SIZE[0] >= SCREEN_SIZE[0]:
        position[0] = SCREEN_SIZE[0] - RECT_SIZE[0]
        velocity[0] *= -1
        color = random_color()

    if position[1] <= 0:
        position[1] = 0
        velocity[1] *= -1
        color = random_color()

    elif position[1] + RECT_SIZE[1] >= SCREEN_SIZE[1]:
        position[1] = SCREEN_SIZE[1] - RECT_SIZE[1]
        velocity[1] *= -1
        color = random_color()

    return velocity, color        

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
    
    position = movements(position, velocity)
    
    draw(screen , color, position , RECT_SIZE)
    
    pygame.display.update() #update display 
    
    velocity, color = bounce_color(position, velocity, color, SCREEN_SIZE, RECT_SIZE) #tuple unpacking 
    
    clock.tick(FPS) 


#cleaning     
pygame.quit()    
    
   