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
pygame.display.set_caption('逆行飇車')

size = width, height = 500, 800
screen = pygame.display.set_mode(size)
WHITE = pygame.color.Color(255, 255, 255)

# 設置圖象的幀數率
FPS = 60
clock = pygame.time.Clock()



class Enemy(pygame.sprite.Sprite):  # 繼承pygame.sprite類
    def __init__(self) :
        super(Enemy, self).__init__()  # 週用父類的init
        self.image = pygame.image.load("misc\\player2.png")
        #  self.rect = self.image.get_rect(top = 480, left = 80)
        self.rect = self.image.get_rect(left = width/2 - 22, top = 0)

    def move(self):
       self.rect.move_ip(1, 5)

class Player(pygame.sprite.Sprite):  # 繼承pygame.sprite類
    def __init__(self):
        # super(Player, self).__init__()  # 週用父類的init
        super().__init__()
        x, y = (width/2, height/2)
        self.image = pygame.image.load("misc\\player.png")
        #  self.rect = self.image.get_rect(top = 480, left = 80)
        self.rect = self.image.get_rect(center=(x, y + 200))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[1073741905]:  # 往下
            self.rect.move_ip(0, 5)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

background = pygame.image.load("misc/background.png")
player = Player()
enemy = Enemy()

# 定義精灵組
enemies = pygame.sprite.Group()
enemies.add(enemy)

# 將所有精灵放到一个組中
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)


while True:
    screen.blit(background, (0, 0))

    for sprite in all_sprites:  # 統一對所有精灵繪圖
        screen.blit(sprite.image, sprite.rect)
        sprite.move()
    # screen.blit(player.image, player.rect)
    # screen.blit(enemy.image, enemy.rect)
    #
    # player.move()
    # enemy.move()

    for event in pygame.event.get():  # 事件偵測
        print(event)
        if event.type == pygame.QUIT:  # QUIT是常量,按+CTRL可看常數設定
            pygame.quit()
            sys.exit()

# 碰撞發生後會有的四種場景
    # 1.敌人和玩家都存在
    # if pygame.sprite.spritecollide(player, enemies, False):
       # print('colsa')
    # 2.敌人消失 (金币...道具)
    #if pygame.sprite.spritecollide(player, enemies, True):
     #   print('colsa')
    # 3.敌人和玩家都消失
    #  if pygame.sprite.spritecollide(player, enemies, True):
       #   player.kill()  # 單獨控制某个精灵對象消失
        #  print('colsa')

    # 4.玩家消失
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        print('colsa')

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.KEYDOWN]:
        player.rect.move_ip(0, 5)

    pygame.display.update()
    clock.tick(FPS)