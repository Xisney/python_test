"""
python慕课
嵩天
pygame
version: 0.2
author: Jason
date: 2019-09-13
"""
import pygame
import sys

# 初始化窗体
pygame.init()
info = pygame.display.Info()
# size = width, height = info.current_w, info.current_h
size = width, height = 800, 500
speed = [1, 1]
BLACK = (0, 0, 0)
# screen = pygame.display.set_mode(size, flags=pygame.FULLSCREEN)
screen = pygame.display.set_mode(size, flags=pygame.RESIZABLE)
icon = pygame.image.load("./图片文件/ball.gif")
pygame.display.set_icon(icon)
pygame.display.set_caption("碰撞与反弹")
ball = pygame.image.load("./图片文件/ball.gif")
ball_rect = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()

# 循环以响应事件
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else \
                    (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
            if event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] >= 0 else speed[0] - 1
            if event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] >= 0 else speed[1] - 1
            if event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else \
                    (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        if event.type == pygame.VIDEORESIZE:
            size = width, height = event.w, event.h
            screen = pygame.display.set_mode(size, flags=pygame.RESIZABLE)
    if pygame.display.get_active():
        ball_rect = ball_rect.move(speed[0], speed[1])
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    # 窗口刷新
    fclock.tick(fps)
    screen.fill(BLACK)
    screen.blit(ball, ball_rect)
    pygame.display.update()
