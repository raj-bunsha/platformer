import pygame
import sys
import os
import time
import random
import math
from pygame.locals import *
import time

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def options():
    running = True
    while running:
        win.fill((0,0,0))

        draw_text('options', font, (255, 255, 255), win, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        clock.tick(60)

def animate(itext):
    text = ''
    string=itext.split(" ")
    for i in range(len(string)):
        win.fill((255,255,255))
        text += string[i]+" "
        text_surface = font.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (W/2, H/2)
        win.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(1000)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False


def gameopening():
    running = True
    animate("Get ready")
    animate("Game starts in 3 2 1")
    animate("Fight")
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        clock.tick(60)
    
def redrawWin():
        win.blit(bg,(bgX,0))
        win.blit(bg,(bgX2,0))
        pygame.draw.rect(win, (255, 0, 0), button_1)
        pygame.draw.rect(win, (255, 0, 0), button_2)
        win.blit(font.render("Adventure To Jungle", 0, (0, 176, 80)), (10, 60))
        pygame.display.update() 

pygame.init()
run=True
W,H = 900, 260
win = pygame.display.set_mode((W,H))
bg =pygame.image.load(os.path.join('game assets','background.jpg')).convert()
H=bg.get_height()
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('escape of adventurous girl')
button_1 = pygame.Rect(W/2-100, 300, 200, 50)
button_2 = pygame.Rect(W/2-100, 400, 200, 50)
font=pygame.font.Font("Soul_Calibur.ttf",144)
bgX = 0
bgX2 = bg.get_width()

bgs=5
clock=pygame.time.Clock()
click = False
while run:
        redrawWin()
        bgX-=bgs
        bgX2-=bgs

        mx, my = pygame.mouse.get_pos()

        if button_1.collidepoint((mx, my)):
                if click:
                        gameopening()
        if button_2.collidepoint((mx, my)):
                if click:
                        options()
        

        if bgX < bg.get_width() * -1: 
                bgX = bg.get_width()
        
        if bgX2 < bg.get_width() * -1:
                bgX2 = bg.get_width()
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True
        clock.tick(20)
