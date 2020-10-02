import os

import pygame
import time

pygame.init()

win = pygame.display.set_mode((500,480)) #created a window for our game of 500*500 size
pygame.display.set_caption("First Game") #Caption(name to be displayed at top) is set

# Character animation work
walk_right = [pygame.image.load(os.path.join('R1.png')), pygame.image.load(os.path.join('R2.png')), pygame.image.load(os.path.join('R3.png')), pygame.image.load(os.path.join('R4.png')), pygame.image.load(os.path.join('R5.png')), pygame.image.load(os.path.join('R6.png')), pygame.image.load(os.path.join('R7.png')), pygame.image.load(os.path.join('R8.png')), pygame.image.load(os.path.join('R9.png'))]
walk_left = [pygame.image.load(os.path.join('L1.png')), pygame.image.load(os.path.join('L2.png')), pygame.image.load(os.path.join('L3.png')), pygame.image.load(os.path.join('L4.png')), pygame.image.load(os.path.join('L5.png')), pygame.image.load(os.path.join('L6.png')), pygame.image.load(os.path.join('L7.png')), pygame.image.load(os.path.join('L8.png')), pygame.image.load(os.path.join('L9.png'))]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load(os.path.join('standing.png'))

clock = pygame.time.Clock()
x = 50
y = 400
width = 64
height = 64
vel = 10
is_jump = False
jump_count = 8
left = False
right = False
walk_count = 0


def redraw_game_window():
    global walk_count

    win.blit(bg, (0, 0))
    # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # '''draw.rect draws a rectangle taking three arguments
    # first surface where we want to draw the rectangle, second the color of rect,
    # and last the position and size of rect.'''

    if walk_count + 1 >= 27:
        walk_count = 0
    if left:
        win.blit(walk_left[walk_count//3], (x, y))
        walk_count += 1
    elif right:
        win.blit(walk_right[walk_count // 3], (x, y))
        walk_count += 1
    else:
        win.blit(char, (x,y))
    pygame.display.update()


# main loop
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and (500 - x - width) >= vel:
        x += vel
        left = False
        right = True
    else:
        right = False
        left = False
        walk_count = 0

    if not is_jump:
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        #
        # if keys[pygame.K_DOWN] and (500 - y - height) > vel:
        #     y += vel
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
            walk_count = 0
    else:
        neg = 1
        if jump_count >= -8:
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * neg
            jump_count -= 1
        else:
            is_jump =  False
            jump_count = 8

    redraw_game_window()
pygame.quit()