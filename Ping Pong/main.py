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

    def moveTo(self, x, y):
        # print(f'In move x: {x}, y: {y}, w: {w}, h: {h}')
        self.x = x
        self.y = y
        if self.y >= 600:
            self.y = 600
        if player.y <= 0:
            player.y = 0
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)

    def moveBy(self, xDelta, yDelta):
        self.moveTo(self.x + xDelta, self.y + yDelta)


# player_rect = pg.Rect(0, 300, 50, 200)
player = Toy(0, 300, 50, 200)

# player2_rect = pg.Rect(950, 300, 50, 200)
player2 = Toy(950, 300, 200, 100)

# ball_rect = pg.Rect(450, 300, 100, 100)
ball = Toy(450, 300, 100, 100)
# ball.moveTo(450 + speed_x, 350 + speed_y)
ball.moveBy(speed_x, speed_y)
playing = True

cnt = 0
while playing:
    cnt += 1
#    print(f'\ncnt: {cnt}')
    win.fill((255, 255, 255))
#    print(f"player2.x: {player2.x}, player2.y: {player2.y}")
#    print(f"ball.x: {ball.x}, ball.y: {ball.y}")
    for e in pg.event.get():
        if e.type == pg.QUIT:
            playing = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        player2.moveBy(0, -1)
        pg.time.wait(2)

    if key[pygame.K_DOWN]:
        player2.moveBy(0, 1)
        pg.time.wait(2)

    if key[pygame.K_w]:
        player.moveBy(0, -1)
        pg.time.wait(2)

    if key[pygame.K_s]:
        player.moveBy(0, 1)
        pg.time.wait(2)

    if pg.sprite.collide_rect(player, ball) or pg.sprite.collide_rect(player2, ball):
        print("hit")
    pg.draw.rect(win, c, player.rect)
    pg.draw.rect(win, c, player2.rect)
    pg.draw.ellipse(win, c, ball.rect)

    #print(f'cnt: {cnt} -- speed_x: {speed_x}, speed_y: {speed_y}')
    #print(f'cnt: {cnt} -- 450 + speed_x: {450 + speed_x}, 350 + speed_y: {350 + speed_y}')
    ball.moveBy(2*speed_x, 2*speed_y)
    pg.display.flip()


