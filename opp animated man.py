import os

import pygame
import time

pygame.init()

win = pygame.display.set_mode((500, 480)) #created a window for our game of 500*500 size
pygame.display.set_caption("First Game") #Caption(name to be displayed at top) is set

# Character animation work
walk_right = [pygame.image.load('R1.png'), pygame.image.load(os.path.join('R2.png')), pygame.image.load(os.path.join('R3.png')), pygame.image.load(os.path.join('R4.png')), pygame.image.load(os.path.join('R5.png')), pygame.image.load(os.path.join('R6.png')), pygame.image.load(os.path.join('R7.png')), pygame.image.load(os.path.join('R8.png')), pygame.image.load(os.path.join('R9.png'))]
walk_left = [pygame.image.load(os.path.join('L1.png')), pygame.image.load(os.path.join('L2.png')), pygame.image.load(os.path.join('L3.png')), pygame.image.load(os.path.join('L4.png')), pygame.image.load(os.path.join('L5.png')), pygame.image.load(os.path.join('L6.png')), pygame.image.load(os.path.join('L7.png')), pygame.image.load(os.path.join('L8.png')), pygame.image.load(os.path.join('L9.png'))]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load(os.path.join('standing.png'))
crying = pygame.image.load(os.path.join('crying.png'))
won = pygame.image.load(os.path.join('won].png'))

score = 0
is_game = True
font_obj = pygame.font.SysFont('comicsans', 25, True)

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False
        self.left = False
        self.right = False
        self.jump_count = 8
        self.walk_count = 0
        self.is_standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if goblin.hitbox[0] <= self.x <= goblin.hitbox[0] + goblin.hitbox[2] and goblin.hitbox[1] < self.y < goblin.hitbox[1] + goblin.hitbox[3]:
            endgame()
        else:
            if self.walk_count + 1 >= 27:
                self.walk_count = 0
            if not self.is_standing:
                if self.left:
                    win.blit(walk_left[self.walk_count // 3], (self.x, self.y))
                    self.walk_count += 1
                elif self.right:
                    win.blit(walk_right[self.walk_count // 3], (self.x, self.y))
                    self.walk_count += 1
            else:
                if self.right:
                    win.blit(walk_right[0], (self.x, self.y))
                else:
                    win.blit(walk_left[0], (self.x, self.y))


        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


def endgame():
    global is_game
    win.blit(bg, (0, 0))
    if goblin.dec_health > 0:
        win.blit(crying, (100, 100))
        is_game = False
    else:
        win.blit(won, (100, 100))
        is_game = False
    text_obj = font_obj.render(f"SCORE: {int(score)} ", True, (0, 0, 0))
    win.blit(text_obj, (330, 10))




class Enemy(object):
    walk_right = [pygame.image.load(os.path.join('R1E.png')), pygame.image.load(os.path.join('R2E.png')), pygame.image.load(os.path.join('R3E.png')), pygame.image.load(os.path.join('R4E.png')), pygame.image.load(os.path.join('R5E.png')), pygame.image.load(os.path.join('R6E.png')), pygame.image.load(os.path.join('R7E.png')), pygame.image.load(os.path.join('R8E.png')), pygame.image.load(os.path.join('R9E.png')),  pygame.image.load(os.path.join('R10E.png')),  pygame.image.load(os.path.join('R11E.png'))]
    walk_left = [pygame.image.load(os.path.join('L1E.png')), pygame.image.load(os.path.join('L2E.png')), pygame.image.load(os.path.join('L3E.png')), pygame.image.load(os.path.join('L4E.png')), pygame.image.load(os.path.join('L5E.png')), pygame.image.load(os.path.join('L6E.png')), pygame.image.load(os.path.join('L7E.png')), pygame.image.load(os.path.join('L8E.png')), pygame.image.load(os.path.join('L9E.png')),  pygame.image.load(os.path.join('L10E.png')),  pygame.image.load(os.path.join('L11E.png'))]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.vel = 3
        self.health = 20
        self.dec_health = 20
        self.hitbox = (self.x + 20 - self.vel, self.y + 1, 29, 58)
        self.rem_health = (self.x + 10 - self.vel, self.y - 5, int(50 * (self.dec_health / 20)), 10)
        self.total_health = (self.x + 10 - self.vel, self.y - 5, 50, 10)

    def draw(self, win):
        self.move()
        if self.walk_count + 1 >= 33:
            self.walk_count = 0

        if self.vel > 0:
            win.blit(self.walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        else:
            win.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        self.hitbox = (self.x + 20 - self.vel, self.y + 1, 29, 58)
        self.total_health = (self.x + 10 - self.vel, self.y - 5, 50, 10)
        self.rem_health = (self.x + 10 - self.vel, self.y - 5, int(50 * (self.dec_health / 20)), 10)

        if self.dec_health >= 0:
            pygame.draw.rect(win, (255, 0, 0), self.total_health)
            pygame.draw.rect(win, (0, 255, 0), self.rem_health)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        else:
            endgame()






    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel* -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0

    def hit(self):

        print('hit')
        # text_obj = font_obj.render(f"SCORE: {int(score/2)} ", True, (0, 0, 0))
        # bullet_hit_goblin += 1
        # win.blit(text_obj, (330, 10))


def redraw_game_window():
    if goblin.dec_health > 0:

        win.blit(bg, (0, 0))
        text_obj = font_obj.render(f"SCORE: {int(score)} ", True, (0, 0, 0))
        win.blit(text_obj, (330, 10))
        # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
        # '''draw.rect draws a rectangle taking three arguments
        # first surface where we want to draw the rectangle, second the color of rect,
        # and last the position and size of rect.'''
        man.draw(win)
        goblin.draw(win)

        for bullet in bullets:
            bullet.draw(win)

        pygame.display.update()

    else:
        endgame()
# main loop
man = player(50, 400, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
bullet_num = 0
bullets = []
run = True

if is_game:
    while run:
        clock.tick(27)
        if bullet_num > 0:
            bullet_num += 1
        if bullet_num > 3:
            bullet_num = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bullet in bullets:

            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y - bullet.radius > goblin.hitbox[1]:
                if bullet.x - bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    score += 1
                    # goblin.hit()
                    bullets.pop(bullets.index(bullet))
                    goblin.dec_health = goblin.dec_health - 0.1*goblin.health

            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and bullet_num == 0:
            if man.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 5:
                bullets.append(projectile(round(man.x + man.width//2), round(man.y + man.height//2), 6, (0, 0, 0), facing))
            bullet_num += 1
        if keys[pygame.K_LEFT] and man.x >= man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.is_standing = False
        elif keys[pygame.K_RIGHT] and (500 - man.x - man.width) >= man.vel:
            man.x += man.vel
            man.left = False
            man.right = True
            man.is_standing = False
        else:
            man.is_standing = True
            man.walk_count = 0

        if not man.is_jump:
            # if keys[pygame.K_UP] and y > vel:
            #     y -= vel
            #
            # if keys[pygame.K_DOWN] and (500 - y - height) > vel:
            #     y += vel
            if keys[pygame.K_UP]:
                man.is_jump = True
        else:
            neg = 1
            if man.jump_count >= -8:
                if man.jump_count < 0:
                    neg = -1
                man.y -= (man.jump_count ** 2) * neg
                man.jump_count -= 1
            else:
                man.is_jump = False
                man.jump_count = 8
        pygame.display.update()
        redraw_game_window()
else:
    endgame()
