import pygame
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 20)
pygame.init()
info = pygame.display.Info()
SIZE = (info.current_w, info.current_h)
HEIGHT = SIZE[1]

RED = [250, 65, 65]
TURQUOISE = [65, 234, 250]
GOLD = [209, 207, 98]
GREEN = [98, 209, 98]
SILVER = [196, 202, 206]
x = 250
y = 250
w = 100
h = 100

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("CS Club Game")

def draw():
    screen.fill(GOLD)
    pygame.draw.rect(screen, SILVER, (x-50, y-50, w, h))

def drawtext():
    font = pygame.font.SysFont('Arial', 96)
    text = font.render("Hello World", True, RED)
    screen.blit(text, (0, int(HEIGHT/2)), None, 0)
    
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()
    drawtext()
    pygame.display.flip()
    
    curs = pygame.mouse.get_pos()
    (x, y) = curs

pygame.quit()