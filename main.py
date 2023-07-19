import math
import pygame as pg
import random as rn
from sys import exit as exit_game
from settings import *


class Head:
    def __init__(self, x, y, degress):
        self.x = x
        self.y = y
        self.degress = degress

    def movement(self):
        self.x += SPEED * math.cos(self.degress)
        self.y += SPEED * math.sin(self.degress)

    def mirrormovement(self):
        self.x -= SPEED * math.cos(self.degress)
        self.y -= SPEED * math.sin(self.degress)


def new_apple():
    return (rn.randrange(20, 780, SPEED), rn.randrange(20, 380, SPEED))


pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT))
head = Head(60, 60, 0)
body = [(60, 60)
        for i in range(DEFAULT_LENGTH)]

apple = new_apple()

while apple in body:
    apple = new_apple()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit_game()

    pressed_button = pg.key.get_pressed()

    if pressed_button[pg.K_LEFT]:
        if head.degress < 0:
            head.degress = 2*math.pi
        head.degress -= 2 * 0.04
    if pressed_button[pg.K_RIGHT]:
        if head.degress > 2*math.pi:
            head.degress = 0
        head.degress += 2 * 0.04

    body.insert(0, (head.x, head.y))
    body.__delitem__(-1)

    head.movement()

    window.fill((0, 0, 0))

    head_rect = pg.draw.circle(window, (0, 255, 0), (head.x, head.y), SIZE//2)
    body_rect = [pg.draw.circle(window, (0, 255, 0), (element[0], element[1]), SIZE//2)
                 for element in body]

    blocks = [pg.draw.rect(window, (255, 255, 255), (0, 0, 800, 1)),
              pg.draw.rect(window, (255, 255, 255), (0, 0, 20, 400)),
              pg.draw.rect(window, (255, 255, 255), (0, 380, 800, 400)),
              pg.draw.rect(window, (255, 255, 255), (780, 0, 20, 400))]

    if head_rect.collidelist(blocks) > -1:
        head.mirrormovement()

    if head_rect.colliderect(pg.draw.circle(window, (255, 255, 0), apple, SIZE//2)):
        apple = new_apple()
        body.append(None)

    pg.display.update()
    clock.tick(FPS)
