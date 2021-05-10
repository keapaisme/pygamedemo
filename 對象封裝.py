# -*- codeing = utf-8 -*-
# @Time :2021/4/26 11:41
# @Author: Kas Huang
# @File:對象封裝.py
# @Software:PyCharm

import pygame
import sys

pygame.init()

gameIcon = pygame.image.load("misc\\hanger80.png")
gameBall = pygame.image.load("misc\\kasicon.jpg")
pygame.display.set_icon(gameIcon)
pygame.display.set_caption('新遊戲')

size = width, height = 500, 600
screen = pygame.display.set_mode(size)
WHITE = pygame.color.Color(255, 255, 255)

# 設置圖象的幀數率
FPS = 60
clock = pygame.time.Clock()


class Player:
    def __init__(self):
        x, y = (width/2, height/2)
        self.image = pygame.image.load("misc\\player.png")
        #  self.rect = self.image.get_rect(top = 480, left = 80)
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        # self.rect.y -= 1
        # self.rect = self.rect.move(0,-1)
        self.rect.move_ip(0, -2)


background = pygame.image.load("misc/background.png")
player = Player()

while True:
    screen.blit(background, (0, 0))
    screen.blit(player.image, player.rect)
    #  y -= 1
    player.move()

    for event in pygame.event.get():  # 事件偵測
        if event.type == pygame.QUIT:  # QUIT是常量,按+CTRL可看常數設定
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(FPS)
