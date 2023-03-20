import pygame
import random

pg = pygame
pg.init()
win = pg.display.set_mode((1000, 800))
win.fill((255, 255, 255))
c = (0, 0, 0)
speed_x = 1
speed_y = random.randint(-1, 1)
#print(f'speed_x: {speed_x}, speed_y: {speed_y}')
# help(pg.Rect)

class Toy(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)

    def move(self, x, y, w, h):
        #print(f'In move x: {x}, y: {y}, w: {w}, h: {h}')
        if x > 1000 or x < 0:
            x = 1000
        if y > 1000 or y < 0:
            y = 1000
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        # self.rect = pg.Rect((x, y), (w, h))
        # self.rect = pg.Rect(pg.rect.Rect(x, y, w, h))
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)


player_rect = pg.Rect(0, 300, 50, 200)
player = Toy(0, 300, 50, 200)

player2_rect = pg.Rect(950, 300, 50, 200)
player2 = Toy(950, 300, 200, 100)

ball_rect = pg.Rect(450, 300, 100, 100)
ball = Toy(450, 300, 100, 100)
ball.move(450 + speed_x, 350 + speed_y, 100, 100)
playing = True

cnt = 0
while playing:
    cnt += 1
#    print(f'\ncnt: {cnt}')
    win.fill((255, 255, 255))
    print(f"player2.x: {player2.x}, player2.y: {player2.y}")
    print(f"ball.x: {ball.x}, ball.y: {ball.y}")
    for e in pg.event.get():
        if e.type == pg.QUIT:
            playing = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        player2_rect.y -= 1
        player2.y -= 1
        pg.time.wait(2)

    if key[pygame.K_DOWN]:
        player2_rect.y += 1
        player2.y += 1
        pg.time.wait(2)

    if key[pygame.K_w]:
        player_rect.y -= 1
        player.y -= 1
        pg.time.wait(2)

    if key[pygame.K_s]:
        player_rect.y += 1
        player.y += 1
        pg.time.wait(2)

    if player_rect.y >= 600 and player.y >= 600:
        player_rect.y = 600
        player.y = 600

    if player_rect.y <= 0 and player.y <= 0:
        player_rect.y = 0
        player.y = 0

    if player2_rect.y >= 600 and player2.y >= 600:
        player2_rect.y = 600
        player2.y = 600

    if player2_rect.y <= 0 and player2.y <= 0:
        player2_rect.y = 0
        player2.y = 0

    if pg.sprite.collide_rect(player, ball) or pg.sprite.collide_rect(player2, ball):
        print("hit")
    pg.draw.rect(win, c, player_rect)
    pg.draw.rect(win, c, player2_rect)
    pg.draw.ellipse(win, c, ball_rect)

    #print(f'cnt: {cnt} -- speed_x: {speed_x}, speed_y: {speed_y}')
    #print(f'cnt: {cnt} -- 450 + speed_x: {450 + speed_x}, 350 + speed_y: {350 + speed_y}')
    ball.move(450 + speed_x, 350 + speed_y, 100, 100)
    #print(ball_rect.x)
    ball_rect.x += speed_x
    ball_rect.y += speed_y
    pg.display.flip()


