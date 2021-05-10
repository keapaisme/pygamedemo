# -*- codeing = utf-8 -*-
# @Time :2021/4/27 17:18
# @Author: Kas Huang
# @File:事件處理_鍵盤.py
# @Software:PyCharm

"""
1.角色不能超出邊界
2.碰撞不真實 
3.難度陏著時間增加
"""  # 加深遊戲體驗

import pygame
import sys
from pygame.locals import *
import time

pygame.init()

gameIcon = pygame.image.load("misc\\hanger80.png")
gameBall = pygame.image.load("misc\\kasicon.jpg")
pygame.display.set_icon(gameIcon)
pygame.display.set_caption('逆行飇車')

size = width, height = 500, 600
screen = pygame.display.set_mode(size)
WHITE = pygame.color.Color(255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # "#FF0000"
SCORE = 0

# 設置圖象的幀數率
FPS = 60
clock = pygame.time.Clock()

# 設置字体和文字
font_big = pygame.font.SysFont("impact.ttf", 60)
font_small = pygame.font.SysFont("trebuc.ttf", 20)
game_over = font_big.render("GAME OVER", True, BLACK)

# 播放背景音樂
# pygame.mixer.Sound("misc\\Alarm08.wav").play(-1)  #背景音樂默認執行1次,參數Loopw默認為0, -1表無限循環


class Enemy(pygame.sprite.Sprite):  # 繼承pygame.sprite類
    def __init__(self):
        super(Enemy, self).__init__()  # 週用父類的init
        self.image = pygame.image.load("misc\\player2.png")
        #  self.rect = self.image.get_rect(top = 480, left = 80)
        self.surf = pygame.Surface((105, 180))
        # self.rect = self.image.get_rect(left=width/1.5 - 22, top=0)
        self.rect = self.surf.get_rect(left=width / 1.5 - 22, top=0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, 5)
        if self.rect.top > height:
            SCORE += 1
            self.rect.top = 0 - self.rect.height


class Player(pygame.sprite.Sprite):  # 繼承pygame.sprite類
    def __init__(self):
        # super(Player, self).__init__()  # 週用父類的init
        super().__init__()
        # x, y = (width/2, height/2)
        self.image = pygame.image.load("misc\\player.png")
        self.surf = pygame.Surface((100, 180))
        #  self.rect = self.image.get_rect(top = 480, left = 80)
        self.rect = self.surf.get_rect(left=178, bottom=height-8)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_DOWN]:  # 往下
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
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))

    for sprite in all_sprites:  # 統一對所有精灵繪圖
        screen.blit(sprite.image, sprite.rect)
        player.move()
        enemy.move()

    for event in pygame.event.get():  # 事件偵測
        # print(event)
        if event.type == pygame.QUIT:  # QUIT是常量,按+CTRL可看常數設定
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()

    """ 
    1.敌人和玩家都存在
        # if pygame.sprite.spritecollide(player, enemies, False):
        # print('colsa')
    2.敌人消失 (金币...道具)
        #if pygame.sprite.spritecollide(player, enemies, True):
        #   print('colsa')
    3.敌人和玩家都消失
        #  if pygame.sprite.spritecollide(player, enemies, True):
          #  player.kill()  # 單獨控制某个精灵對象消失
          #  print('colsa')
    4.玩家消失
    """  # 碰撞發生後會有的四種場景

    if pygame.sprite.spritecollideany(player, enemies):
        # pygame.mixer.Sound("misc\\Windows Recycle.wav").play()
        time.sleep(1)
        screen.fill(RED)
        screen.blit(game_over, (80, 150))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(FPS)
