import pygame
import time 
import numpy as np
import copy
import os
import json
from board import Board
from player import HumanPlayer
from compplayer import AIPlayer
from buttons import Buttons

pygame.init()

screen = pygame.display.set_mode((800, 900)) 
screen_rect = screen.fill((210,180,140))
pygame.display.set_caption("Go")

image = pygame.image.load('go9x9.png')
image = pygame.transform.scale(image, (800, 800))
imagerect = image.get_rect()

btn = Buttons(screen, imagerect)
hpl = HumanPlayer(btn)
aipl = AIPlayer(btn)
bd = Board(screen,image)


z = len([name for name in os.listdir('board') if os.path.isfile(os.path.join('board', name))])
#Load Board 
if z:
    for i in range(z):
        with open("board/"+str(i+1)+".txt", "r") as file:
            bd.boardhist.append(copy.deepcopy(np.array(json.load(file))))
            bd.boardhistpast.append(copy.deepcopy(bd.boardhist[i+1]))
            for j in range (9):
                for k in range (9):
                    if bd.boardhistpast[i+1][j][k] % 2 == 1:
                        bd.boardhistpast[i+1][j][k] = 1
                    if bd.boardhistpast[i+1][j][k] >= 1 and bd.boardhistpast[i+1][j][k] % 2 == 0:
                        bd.boardhistpast[i+1][j][k] = 2
                    if bd.boardhistpast[i+1][j][k] == 0:
                        bd.boardhistpast[i+1][j][k] = 0
    btn.turn = z
    for j in range(9):
        for k in range(9):
            bd.board[j][k] = bd.boardhist[btn.turn][j][k]
            if bd.board[j][k] == btn.turn:
                bd.updateboard(j, k, btn)
bd.defineterritory()
bd.drawboard(screen, image)
pygame.display.flip()

while True:
    #time.sleep(1)
    if btn.turn == 0 and os.path.exists('board/1.txt'):
        os.remove('board/1.txt')
    if aipl.white and btn.turn:
        start = time.time()
        while True:
            btn.turn += 1
            x = aipl.compwhiteplayermove(bd, btn, screen, image, imagerect, start)
            if x:
                btn.turn -=1
                continue
            if not x:
                bd.updatehistboards()
                bd.saveboard(btn)
                bd.drawboard(screen, image)
                hpl.black = 1
                if btn.movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
                break
    while hpl.black: 
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn.move_rect.collidepoint(pos):
                    btn.movebutton += 1
                    if btn.movebutton % 2 == 1:
                        bd.showmovenumber(screen,image)
                    if btn.movebutton % 2 == 0:
                        bd.drawboard(screen,image)
                if imagerect.collidepoint(pos):
                    for i in range(9):
                        for j in range(9):
                            if bd.boardrects[(i, j)].collidepoint(pos) and (bd.board[i][j] == 0):
                                btn.turn += 1
                                x = bd.updateboard(i, j, btn)
                                if x:
                                    btn.turn -= 1
                                    continue
                                bd.updatehistboards()
                                bd.saveboard(btn)
                                bd.drawboard(screen, image)
                                if btn.movebutton % 2 == 1:
                                    bd.showmovenumber(screen,image)
                                if aipl.white:
                                    hpl.black = 0
                                break
                if btn.back_rect.collidepoint(pos):
                    bd.backonemove(btn)
                    bd.saveboard(btn)
                    bd.drawboard(screen,image)
                    if btn.movebutton % 2 == 1:
                        bd.showmovenumber(screen,image)
                if btn.passturn_rect.collidepoint(pos):
                    bd.passturn(screen, imagerect, btn)
                    bd.saveboard(btn)
                    bd.drawboard(screen, image)
                    if btn.movebutton % 2 == 1:
                        bd.showmovenumber(screen,image)
                    if aipl.white:
                        hpl.black = 0
            if event.type == pygame.QUIT: 
                pygame.quit() 
                quit() 
            
    pygame.display.flip()

    

        
