import pygame
import sys

class Toy(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

pygame.init()
window = pygame.display.set_mode([2000, 1000])
window.fill((255, 0, 247))

Abee_Island = pygame.Rect(250, 800, 300, 500)
Goal_Island = pygame.Rect(1700, 800, 1000, 1000)
Tree_Island = pygame.Rect(975, 800, 300, 500)
goal = pygame.Rect(1775, 200, 600, 600)

SoccerBallImg = pygame.image.load('SoccerBall.png').convert_alpha()
# SoccerBall_x = 400
# SoccerBall_y = 700
SoccerBall_x = 400
SoccerBall_y = 700

AbeeKick = pygame.image.load('AbeeKick.png')
AbeeStand = pygame.image.load('AbeeStand.png')
Abee_x = 275
Abee_y = 550

PinkTreeImg = pygame.image.load('PinkTree.png').convert_alpha()

PinkTree = Toy((975, 800), PinkTreeImg)
SoccerBall = Toy((400, 700), SoccerBallImg)


def arrange_the_trees():
    Tree_x = 1000
    Tree_y = 400
    window.blit(PinkTreeImg, (Tree_x, Tree_y))

def make_goal_net():
    pygame.draw.line(window, (255, 255, 255), (1850, 800), (2000, 647.5), 10)
    pygame.draw.line(window, (255, 255, 255), (1775, 800), (2000, 550), 10)
    pygame.draw.line(window, (255, 255, 255), (1775, 700), (2000, 462.5), 10)
    pygame.draw.line(window, (255, 255, 255), (1775, 600), (2000, 375), 10)
    pygame.draw.line(window, (255, 255, 255), (1775, 500), (2000, 287.5), 10)
    pygame.draw.line(window, (255, 255, 255), (1775, 400), (2000, 200), 10)
    pygame.draw.line(window, (255, 255, 255), (1775, 300), (1900, 195), 10)

    pygame.draw.line(window, (255, 255, 255), (1965, 800), (1800, 200), 10)
    pygame.draw.line(window, (255, 255, 255), (1885, 800), (1775, 450), 10)
    pygame.draw.line(window, (255, 255, 255), (2000, 600), (1900, 200), 10)


BallOffset_x = 0
BallOffset_y = 0
AlienOffset = 0
frames = 0

BallSpeed_x = float(input("Enter the amount of power from 1-50: "))

while BallSpeed_x > 50 or BallSpeed_x < 0:
    BallSpeed_x = float(input("Please enter the amount of power from 1-50: "))

BallSpeed_y = float(input("Enter the amount of height from 1-50: "))

while BallSpeed_y > 50 or BallSpeed_y < 0:
    BallSpeed_y = float(input("Please enter the amount of height from 1-50: "))

while frames <= 100:
    window.fill((255, 0, 247))
    arrange_the_trees()
    pygame.draw.circle(window, (255, 255, 0), (200, 200), 100)
    pygame.draw.rect(window, (154, 0, 255), Abee_Island)
    pygame.draw.rect(window, (154, 0, 255), Goal_Island)
    pygame.draw.rect(window, (154, 0, 255), Tree_Island)

    if 30 >= frames >= 0:
        window.blit(SoccerBallImg, (SoccerBall_x + BallOffset_x, SoccerBall_y + BallOffset_y))

    if 100 >= frames >= 30:
        window.blit(SoccerBallImg, (SoccerBall_x + BallOffset_x, SoccerBall_y + BallOffset_y))
        SoccerBall.rect.x = SoccerBall_x + BallOffset_x
        SoccerBall.rect.y = SoccerBall_y + BallOffset_y
        # SoccerBall.image
        BallOffset_x += BallSpeed_x
        BallOffset_y -= BallSpeed_y
        BallSpeed_y += 1
        BallSpeed_x += 1

    if 30 >= frames >= 0 or 100 >= frames >= 40:
        window.blit(AbeeStand, (Abee_x, Abee_y))

    if 40 > frames > 30:
        window.blit(AbeeKick, (Abee_x, Abee_y))

    if 55 >= frames >= 50:
        BallSpeed_y -= 20

    pygame.draw.rect(window, (255, 255, 255), goal, 10)
    make_goal_net()
    pygame.display.flip()

    if pygame.sprite.collide_rect(PinkTree, SoccerBall):
        print("Oops, you hit a tree!")
        print("Rerun your program to retry")
        sys.exit(0)
    pygame.time.wait(80)
    frames += 1
float(input("How much would you rate my first and probably my easiest game from 1-5 (Decimals can be included): "))
