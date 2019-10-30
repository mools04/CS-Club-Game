#This works, but it's boring and we need to add to it
import pygame
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 20)
pygame.init()
info = pygame.display.Info()
SIZE = (info.current_w, info.current_h)
LENGTH = SIZE[0]

RED = [250, 65, 65]
TURQUOISE = [65, 234, 250]
GOLD = [209, 207, 98]
GREEN = [98, 209, 98]
SILVER = [196, 202, 206]
BLACK = [0, 0, 0]

x = 250
y = 250
r = 100

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("CS Club Game")

def draw():
    screen.fill(GOLD)
    pygame.draw.circle(screen, SILVER, (x, y), r)

def drawtext():
    font = pygame.font.SysFont('Consolas.ttf', 85)
    text = font.render("Welcome to *Game Title!*", True, BLACK)
    screen.blit(text, [50, 50])
    
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    curs = pygame.mouse.get_pos()
    (x, y) = curs
    
    draw()
    drawtext()
    pygame.display.flip()
    #We should add something here to make it more interesting

pygame.quit()
