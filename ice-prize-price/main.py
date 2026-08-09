import pygame 
SCREEN_SIZE = (1280, 720)
RECT_SIZE =(200, 100)
FPS = 60
BACKGROUND = 'blue'
run = True
position=[200, 500]
radius=100
width = 10
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
EDGE_X = SCREEN_SIZE[0] * 0.1
EDGE_Y = SCREEN_SIZE[1] * 0.1
clock = pygame.time.Clock()
direction_x = None
direction_y = None
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            if y <= EDGE_Y:
                direction_y = "up"
                
            elif y >= SCREEN_SIZE[1] - EDGE_Y:
                direction_y = "down"
                
            if x <= EDGE_X:
                direction_x = "left"
                
            elif x >= SCREEN_SIZE[0] - EDGE_X:
                direction_x = "right"
                
        elif event.type == pygame.MOUSEBUTTONUP:
            direction_x = None
            direction_y = None
                
                
    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, "white", position, radius, width )
    pygame.display.update()
    

        
    if direction_y == "up":
        position[1] -= 5

    elif direction_y == "down":
        position[1] += 5

    if direction_x == "left":
        position[0] -= 5

    elif direction_x == "right":
        position[0] += 5
        
    if position[0] - radius <= 0:
        position[0] = radius

    elif position[0] + radius >= SCREEN_SIZE[0]:
        position[0] = SCREEN_SIZE[0] - radius

    if position[1] - radius <= 0:
        position[1] = radius

    elif position[1] + radius >= SCREEN_SIZE[1]:
        position[1] = SCREEN_SIZE[1] - radius
    pygame.display.update()        
    clock.tick(FPS)
    
    
pygame.quit()