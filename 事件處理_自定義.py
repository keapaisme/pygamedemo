# -*- codeing = utf-8 -*-
# @Time :2021/4/27 17:18
# @Author: Kas Huang
# @File:事件處理_鍵盤.py
# @Software:PyCharm

import pygame
import sys
from pygame.locals import *

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

# 定義用户事件類型名稱及編碼
# 定義用户事件觸發條件 35,465
# 定義用户事件處理過程

# 定義用户事件
OUT_OF_RANGE = pygame.USEREVENT + 1

class Player:
    def __init__(self):
        x, y = (width/2, height/2)
        self.image = pygame.image.load("misc\\player.png")
        #  self.rect = self.image.get_rect(top = 480, left = 80)
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        mouseX, mouseY = pygame.mouse.get_pos()

        # 觸發用戶自定義事件
        if self.rect.left < 35 or self.rect.right > 465:
            pygame.event.post(pygame.event.Event(OUT_OF_RANGE))
        # player.rect.x = mouseX
        # player.rect.y = mouseY
        if player.rect.width/2 <= mouseX <= width - player.rect.width/2\
                and player.rect.height/2 <= mouseY <= height - player.rect.height/2:
            player.rect.center = (mouseX, mouseY)
        pass

background = pygame.image.load("misc/background.png")
player = Player()


while True:
    screen.blit(background, (0, 0))
    screen.blit(player.image, player.rect)
    #  y -= 1
    player.move()

    for event in pygame.event.get():  # 事件偵測
        print(event)
        if event.type == pygame.QUIT:  # QUIT是常量,按+CTRL可看常數設定
            pygame.quit()
            sys.exit()

        if event.type == OUT_OF_RANGE:
            if player.rect.x < width/2:
                lineX = player.rect.x
                lineY = player.rect.y
                pygame.draw.line(screen, 'red', [lineX, lineY], [lineX, lineY + player.rect.height/2], 10)
            else:
                lineX = player.rect.x + player.rect.width
                lineY = player.rect.y
                pygame.draw.line(screen, 'red', [lineX, lineY], [lineX, lineY + player.rect.height/2], 10)



            # pygame.draw.rect(screen, 'red', [player.rect.x, player.rect.y, 120, 200] , 10)


    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.KEYDOWN]:
        player.rect.move_ip(0, 5)

    pygame.display.update()
    clock.tick(FPS)