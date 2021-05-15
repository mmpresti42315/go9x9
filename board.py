import pygame
import time
import json
import numpy as np 
import os
import copy 

class Board():

    def __init__(self, screen, image):
        self.screen = screen
        self.image = image
        self.board = np.zeros((9, 9), dtype=int)
        self.blackboard = np.zeros((9, 9, 3, 2), dtype=int)
        self.whiteboard = np.zeros((9, 9, 3, 2), dtype=int)
        self.boardhist = [[]]
        self.boardhistpast = [[]]
        
        self.boardsurfs = {}
        for self.i in range(9):
            for self.j in range(9):
                self.boardsurfs[(self.i, self.j)] = pygame.Surface((image.get_width()/15,image.get_height()/15))
        
        self.whcoords = [32.1, 7.1, 4.2, 2.8, 2.1, 1.7, 1.46, 1.26, 1.1]
        self.boardrects = {}
        for self.i in range(9):
            for self.j in range(9):
                self.boardrects[(self.i, self.j)] = screen.blit(self.boardsurfs[(self.i, self.j)], (image.get_width()/self.whcoords[self.j],image.get_height()/self.whcoords[self.i]))
        
        screen.blit(image, (0, 0))
        
        self.coords = [[15.52, 15.52], [5.77, 15.52], [3.54, 15.52], [2.556, 15.52], [2, 15.52], [1.64, 15.52], [1.4, 15.52], [1.21, 15.52],  [1.07, 15.52]], \
                      [[15.52, 5.77],  [5.77, 5.77],  [3.54, 5.77],  [2.556, 5.77],  [2, 5.77],  [1.64, 5.77],  [1.4, 5.77],  [1.21, 5.77],   [1.07, 5.77]], \
                      [[15.52, 3.54],  [5.77, 3.54],  [3.54, 3.54],  [2.556, 3.54],  [2, 3.54],  [1.64, 3.54],  [1.4, 3.54],  [1.21, 3.54],   [1.07, 3.54]], \
                      [[15.52, 2.556], [5.77, 2.556], [3.54, 2.556], [2.556, 2.556], [2, 2.556], [1.64, 2.556], [1.4, 2.556], [1.21, 2.556],  [1.07, 2.556]], \
                      [[15.52, 2],     [5.77, 2],     [3.54, 2],     [2.556, 2],     [2, 2],     [1.64, 2],     [1.4, 2],     [1.21, 2],      [1.07, 2]], \
                      [[15.52, 1.64],  [5.77, 1.64],  [3.54, 1.64],  [2.556, 1.64],  [2, 1.64],  [1.64, 1.64],  [1.4, 1.64],  [1.21, 1.64],   [1.07, 1.64]], \
                      [[15.52, 1.4],   [5.77, 1.4],   [3.54, 1.4],   [2.556, 1.4],   [2, 1.4],   [1.64, 1.4],   [1.4, 1.4],   [1.21, 1.4],    [1.07, 1.4]], \
                      [[15.52, 1.21],  [5.77, 1.21],  [3.54, 1.21],  [2.556, 1.21],  [2, 1.21],  [1.64, 1.21],  [1.4, 1.21],  [1.21, 1.21],   [1.07, 1.21]], \
                      [[15.52, 1.07],  [5.77, 1.07],  [3.54, 1.07],  [2.556, 1.07],  [2, 1.07],  [1.64, 1.07],  [1.4, 1.07],  [1.21, 1.07],   [1.07, 1.07]], 
    
    def updateboard(self, x, y, btn):
        self.board[x][y] = btn.turn

        self.defineterritory()
        self.suicide = self.capture(x, y, btn)
        self.repeat = self.checkrepetition(x, y, btn)

        if self.suicide or self.repeat:
            return True
        else:
            return False
    
    def updatehistboards(self):
        self.boardhist.append(np.zeros((9, 9), dtype = int))
        self.boardhistpast.append(np.zeros((9, 9), dtype = int))

    def defineterritory(self):
        for self.i in range (0, 9):
            for self.j in range (0, 9):
                self.blackboard[self.i][self.j][1][0] = 0
                self.whiteboard[self.i][self.j][1][0] = 0
                self.blackboard[self.i][self.j][2][0] = self.i
                self.blackboard[self.i][self.j][2][1] = self.j
                self.whiteboard[self.i][self.j][2][0] = self.i
                self.whiteboard[self.i][self.j][2][1] = self.j


        #Populate Black/White Boards
        for self.i in range(0, 9):
            for self.j in range(0, 9):
                if self.board[self.i][self.j] % 2 == 1:
                    self.blackboard[self.i][self.j][0][0] = self.board[self.i][self.j]
                if self.board[self.i][self.j] % 2 == 0 and self.board[self.i][self.j] > 1:
                    self.whiteboard[self.i][self.j][0][0] = self.board[self.i][self.j]
        
        self.bbname = 1
        self.bwname = 2

        #Calculate Territories on Both Boards
        for self.i in range(0, 9):
            for self.j in range(0, 9):
                if self.blackboard[self.i][self.j][0][0] == 0:
                    self.nameblackboundterritory(self.bbname, self.i, self.j)
                    self.bbname += 2
        for self.i in range(0, 9):
            for self.j in range(0, 9):
                if self.whiteboard[self.i][self.j][0][0] == 0:
                    self.namewhiteboundterritory(self.bwname, self.i, self.j)
                    self.bwname += 2
        
        #Create Lists of Black Territories and White Stones in Black Territories
        self.blackterr = []
        for self.i in range(0, 9):
            for self.j in range(0, 9):
                if self.blackboard[self.i][self.j][0][0] == 0:
                    self.blackterr.append(self.blackboard[self.i][self.j][1][0])
        self.blackterrset = set(self.blackterr)
        self.blackterrlist = list(self.blackterrset)
        self.blackterrgroups = []
        self.wstonesinbterr = []
        for self.k in range(len(self.blackterrlist)):
            self.blackterrgroups.append([])
            self.wstonesinbterr.append([])
            for self.i in range(0, 9):
                for self.j in range(0, 9):
                    if self.blackboard[self.i][self.j][0][0] == 0 and self.blackboard[self.i][self.j][1][0] == self.blackterrlist[self.k]:
                        self.blackterrgroups[self.k].append(self.blackboard[self.i][self.j])
                        if self.whiteboard[self.i][self.j][0][0] % 2 == 0 and self.whiteboard[self.i][self.j][0][0] > 1:
                            self.wstonesinbterr[self.k].append(self.blackboard[self.i][self.j])
        
        #Create Lists of White Territories and Black Stones in White Territories
        self.whiteterr = []
        for self.i in range(0, 9):
            for self.j in range(0, 9):
                if self.whiteboard[self.i][self.j][0][0] == 0:
                    self.whiteterr.append(self.whiteboard[self.i][self.j][1][0])
        self.whiteterrset = set(self.whiteterr)
        self.whiteterrlist = list(self.whiteterrset)
        self.whiteterrgroups = []
        self.bstonesinwterr = []
        for self.k in range(len(self.whiteterrlist)):
            self.whiteterrgroups.append([])
            self.bstonesinwterr.append([])
            for self.i in range(0, 9):
                for self.j in range(0, 9):
                    if self.whiteboard[self.i][self.j][0][0] == 0 and self.whiteboard[self.i][self.j][1][0] == self.whiteterrlist[self.k]:
                        self.whiteterrgroups[self.k].append(self.whiteboard[self.i][self.j])
                        if self.blackboard[self.i][self.j][0][0] % 2 == 1:
                            self.bstonesinwterr[self.k].append(self.whiteboard[self.i][self.j])
    
    def capture(self, x, y, btn):
        #Capture White Groups
        if btn.turn % 2 == 1:
            for self.i in range(len(self.blackterrgroups)):
                if len(self.wstonesinbterr[self.i]) == len(self.blackterrgroups[self.i]):
                    for self.k in self.wstonesinbterr[self.i]:
                        self.x = self.k[2][0]
                        self.y = self.k[2][1]
                        self.board[self.x][self.y] = 0
                        self.whiteboard[self.x][self.y][0][0] = 0
                        self.whiteboard[self.x][self.y][1][0] = 0
            #Suicide? 
            self.defineterritory()
            for self.i in range(len(self.whiteterrgroups)):
                if len(self.bstonesinwterr[self.i]) == len(self.whiteterrgroups[self.i]):
                    self.board[x][y] = 0
                    self.blackboard[x][y][0][0] = 0
                    self.blackboard[x][y][1][0] = 0
                    return True
        #Capture Black Groups
        if btn.turn % 2 == 0:
            for self.i in range(len(self.whiteterrgroups)):
                if len(self.bstonesinwterr[self.i]) == len(self.whiteterrgroups[self.i]):
                    for self.k in self.bstonesinwterr[self.i]:
                        self.x = self.k[2][0]
                        self.y = self.k[2][1]
                        self.board[self.x][self.y] = 0
                        self.blackboard[self.x][self.y][0][0] = 0
                        self.blackboard[self.x][self.y][1][0] = 0
            #Suicide?
            self.defineterritory()
            for self.i in range(len(self.blackterrgroups)):
                if len(self.wstonesinbterr[self.i]) == len(self.blackterrgroups[self.i]):
                    self.board[x][y] = 0
                    self.whiteboard[x][y][0][0] = 0
                    self.whiteboard[x][y][1][0] = 0
                    return True
        return False
    
    def checkrepetition(self, x, y, btn):
        #Repetition?
        if btn.turn > 3:
            self.boardhistpres = np.zeros((9, 9), dtype = int)
            for self.i in range(9):
                for self.j in range(9):
                    if self.board[self.i][self.j] % 2 == 1:
                        self.boardhistpres[self.i][self.j] = 1
                    if self.board[self.i][self.j] >= 1 and self.board[self.i][self.j] % 2 == 0:
                        self.boardhistpres[self.i][self.j] = 2
                    if self.board[self.i][self.j] == 0:
                        self.boardhistpres[self.i][self.j] = 0
            self.repetition = 0
            for self.i in range(9):
                for self.j in range(9):
                    if self.boardhistpres[self.i][self.j] != self.boardhistpast[len(self.boardhistpast)-2][self.i][self.j]:
                        self.repetition += 1
    
            if self.repetition == 0: 
                np.copyto(self.board, self.boardhist[len(self.boardhist)-1])
                self.blackboard[x][y][0][0] = 0
                self.blackboard[x][y][1][0] = 0
                self.whiteboard[x][y][0][0] = 0
                self.whiteboard[x][y][1][0] = 0
                return True
        return False
    
    def saveboard(self, btn):
        if btn.turn >= 1:
            for self.i in range (9):
                for self.j in range (9):
                    self.boardhist[btn.turn][self.i][self.j] = self.board[self.i][self.j]
                    if self.board[self.i][self.j] % 2 == 1:
                        self.boardhistpast[btn.turn][self.i][self.j] = 1
                    if self.board[self.i][self.j] >= 1 and self.board[self.i][self.j] % 2 == 0:
                        self.boardhistpast[btn.turn][self.i][self.j] = 2
                    if self.board[self.i][self.j] == 0:
                        self.boardhistpast[btn.turn][self.i][self.j] = 0
                for i in range(len(self.boardhist) - 1):
                    with open("board/"+str(i+1)+".txt", 'w+') as file:
                        json.dump(self.boardhist[i+1].tolist(), file)
        else:
            return


    def nameblackboundterritory(self, bbname, i, j):
        if self.blackboard[i][j][0][0] == 0 and self.blackboard[i][j][1][0] == 0:
            self.blackboard[i][j][1][0] = bbname

        if j < 8 and self.blackboard[i][j + 1][0][0] == 0 and self.blackboard[i][j + 1][1][0] == 0 :
            self.nameblackboundterritory(bbname, i, j + 1)

        if j >= 1 and self.blackboard[i][j - 1][0][0] == 0 and self.blackboard[i][j - 1][1][0] == 0 :
            self.nameblackboundterritory(bbname, i, j - 1)

        if i < 8 and self.blackboard[i + 1][j][0][0] == 0 and self.blackboard[i + 1][j][1][0] == 0 :
            self.nameblackboundterritory(bbname, i + 1, j)

        if i >= 1 and self.blackboard[i - 1][j][0][0] == 0 and self.blackboard[i - 1][j][1][0] == 0 :
            self.nameblackboundterritory(bbname, i - 1, j)
            
        return
    
    def namewhiteboundterritory(self, bwname, i, j):
        if self.whiteboard[i][j][0][0] == 0 and self.whiteboard[i][j][1][0] == 0:
            self.whiteboard[i][j][1][0] = bwname

        if j < 8 and self.whiteboard[i][j + 1][0][0] == 0 and self.whiteboard[i][j + 1][1][0] == 0 :
            self.namewhiteboundterritory(bwname, i, j + 1)

        if j >= 1 and self.whiteboard[i][j - 1][0][0] == 0 and self.whiteboard[i][j - 1][1][0] == 0 :
            self.namewhiteboundterritory(bwname, i, j - 1)

        if i < 8 and self.whiteboard[i + 1][j][0][0] == 0 and self.whiteboard[i + 1][j][1][0] == 0 :
            self.namewhiteboundterritory(bwname, i + 1, j)

        if i >= 1 and self.whiteboard[i - 1][j][0][0] == 0 and self.whiteboard[i - 1][j][1][0] == 0 :
            self.namewhiteboundterritory(bwname, i - 1, j)
            
        return
    
    def showmovenumber(self, screen, image):
        self.FONT = pygame.font.Font(None, image.get_width()//28)
        self.terrs = []
        for self.i in range(0, 9):
            self.terrs.append([])
            for self.j in range(0, 9):
                self.terrs[self.i].append([])
                if self.board[self.i][self.j] % 2 == 1 and self.board[self.i][self.j] >= 1: 
                    self.number = self.FONT.render(str(self.board[self.i][self.j]), True, (255,255,255))
                    self.number_rect = self.number.get_rect(center=(image.get_width()/self.coords[self.i][self.j][0],image.get_height()/self.coords[self.i][self.j][1]))
                    screen.blit(self.number, self.number_rect)
                if self.board[self.i][self.j] % 2 == 0 and self.board[self.i][self.j] > 0: 
                    self.number = self.FONT.render(str(self.board[self.i][self.j]), True, (0,0,0))
                    self.number_rect = self.number.get_rect(center=(image.get_width()/self.coords[self.i][self.j][0],image.get_height()/self.coords[self.i][self.j][1]))
                    screen.blit(self.number, self.number_rect)
                if self.board[self.i][self.j] == 0: 
                    self.terrs[self.i][self.j].append([self.blackboard[self.i][self.j][1][0], self.whiteboard[self.i][self.j][1][0]])
                    self.trs = self.FONT.render(str(self.terrs[self.i][self.j]).strip('[]'), True, (0,0,255))
                    self.terrs_rect = self.trs.get_rect(center=(image.get_width()/self.coords[self.i][self.j][0],image.get_height()/self.coords[self.i][self.j][1])) 
                    screen.blit(self.trs, self.terrs_rect)
                    pygame.display.flip()
        pygame.display.flip()
                
    def backonemove(self, btn):
        #if repetition not descending (write expression) for super-ko rule
        if btn.turn >= 2:
            for self.i in range(9):
                for self.j in range(9):
                    self.board[self.i][self.j] = self.boardhist[btn.turn-1][self.i][self.j]
                    if self.blackboard[self.i][self.j][0][0] == btn.turn:
                        self.blackboard[self.i][self.j][0][0] = 0
                    if self.whiteboard[self.i][self.j][0][0] == btn.turn:
                        self.whiteboard[self.i][self.j][0][0] = 0
            os.remove(os.path.join('board', str(len(self.boardhist) - 1)+'.txt'))
            btn.turn -= 1
            del self.boardhist[-1]
            del self.boardhistpast[-1]
            for self.i in range(9):
                for self.j in range(9):
                    if self.board[self.i][self.j] == btn.turn:
                        self.updateboard(self.i, self.j, btn)
                        return
        if btn.turn == 1:
            for self.i in range(9):
                for self.j in range(9):
                    if self.blackboard[self.i][self.j][0][0] == btn.turn:
                        self.blackboard[self.i][self.j][0][0] = 0
                    if self.whiteboard[self.i][self.j][0][0] == btn.turn:
                        self.whiteboard[self.i][self.j][0][0] = 0
            os.remove(os.path.join('board', str(len(self.boardhist) - 1)+'.txt'))
            btn.turn -= 1
            del self.boardhist[-1]
            del self.boardhistpast[-1]
            self.board = np.zeros((9, 9), dtype = int)
            self.defineterritory()
            return
        if btn.turn == 0:
            return
            
    
    def passturn(self, screen, imagerect, btn):
        self.boardhist.append(copy.deepcopy(self.boardhist[len(self.boardhist)-1]))
        self.boardhistpast.append(copy.deepcopy(self.boardhistpast[len(self.boardhistpast)-1]))
        self.font = pygame.font.SysFont(None, 96)
        self.rect = pygame.Rect(0, 0, 400, 100)
        self.rect.center = imagerect.center
        self.pass_image = self.font.render("Pass", True, (255,255,255), (128, 128, 128))
        self.pass_image_rect = self.pass_image.get_rect()
        self.pass_image_rect.center = self.rect.center
        screen.blit(self.pass_image, self.pass_image_rect)
        pygame.display.flip()
        time.sleep(2)
        btn.turn += 1
    
    def drawboard(self, screen, image):
        screen.blit(image, (0, 0))
        for self.i in range(0, 9):
            for self.j in range(0, 9):
                if self.board[self.i][self.j] % 2 == 1 and self.board[self.i][self.j] >= 1: 
                    pygame.draw.circle(screen,(0,0,0),(image.get_width()/self.coords[self.i][self.j][0],image.get_height()/self.coords[self.i][self.j][1]), image.get_width()/20)
                if self.board[self.i][self.j] % 2 == 0 and self.board[self.i][self.j] > 0: 
                    pygame.draw.circle(screen,(255,255,255),(image.get_width()/self.coords[self.i][self.j][0],image.get_height()/self.coords[self.i][self.j][1]), image.get_width()/20)
        pygame.display.flip()



            

