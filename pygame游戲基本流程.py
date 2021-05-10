# -*- codeing = utf-8 -*-
# @Time :2021/4/18 0:49
# @Author: Kas Huang
# @File:pygame游戲基本流程.py
# @Software:PyCharm

import pygame
import sys

pygame.init()

gameIcon = pygame.image.load("misc\hanger80.png")
gameBall = pygame.image.load('misc\kasicon.jpg')
pygame.display.set_icon(gameIcon)
pygame.display.set_caption('新遊戲')
size = width, height = 500, 600
screen = pygame.display.set_mode(size)
WHITE = pygame.color.Color(255, 255, 255)
gbX, gbY = 125, 500
giX, giY = 375, 500

# 設置圖象的幀數率
FPS = 120
clock = pygame.time.Clock()

while True:

    screen.fill('black')  # draw screen again to make a move sight
    pygame.draw.circle(screen, 'red', [100, 100], 30, 1)
    pygame.draw.rect(screen, 'white', [250, 0, -5, 600], 10)
    pygame.draw.polygon(screen, 'white', [(20, 34), (45, 80), (199, 77)], 1)

    screen.blit(gameBall, (gbX, gbY))
    screen.blit(gameIcon, (giX, giY))
    gbY -= 1
    giY -= 0.85

    for event in pygame.event.get():  # 事件偵測
        if event.type == pygame.QUIT:  # QUIT是常量,按+CTRL可看常數設定
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(FPS)