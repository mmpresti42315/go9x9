import pygame

class Board():

    def __init__(self):

        self.groupcount = 0

        self.board = []
        self.blackboard = []
        self.whiteboard = []
        self.boardhist = [[]]
        for self.i in range (9):
            self.boardrow = [[0, 0] for self.j in range(9)]
            self.board.append(self.boardrow)
        for self.i in range (9):
            self.boardrow = [[0, 0, 0] for self.j in range(9)]
            self.blackboard.append(self.boardrow)
        for self.i in range (9):
            self.boardrow = [[0, 0, 0] for self.j in range(9)]
            self.whiteboard.append(self.boardrow)
        
        self.coords = [[15.52, 15.52], [5.77, 15.52], [3.54, 15.52], [2.556, 15.52], [2, 15.52], [1.64, 15.52], [1.4, 15.52], [1.21, 15.52],  [1.07, 15.52]], \
                      [[15.52, 5.77],  [5.77, 5.77],  [3.54, 5.77],  [2.556, 5.77],  [2, 5.77],  [1.64, 5.77],  [1.4, 5.77],  [1.21, 5.77],   [1.07, 5.77]], \
                      [[15.52, 3.54],  [5.77, 3.54],  [3.54, 3.54],  [2.556, 3.54],  [2, 3.54],  [1.64, 3.54],  [1.4, 3.54],  [1.21, 3.54],   [1.07, 3.54]], \
                      [[15.52, 2.556], [5.77, 2.556], [3.54, 2.556], [2.556, 2.556], [2, 2.556], [1.64, 2.556], [1.4, 2.556], [1.21, 2.556],  [1.07, 2.556]], \
                      [[15.52, 2],     [5.77, 2],     [3.54, 2],     [2.556, 2],     [2, 2],     [1.64, 2],     [1.4, 2],     [1.21, 2],      [1.07, 2]], \
                      [[15.52, 1.64],  [5.77, 1.64],  [3.54, 1.64],  [2.556, 1.64],  [2, 1.64],  [1.64, 1.64],  [1.4, 1.64],  [1.21, 1.64],   [1.07, 1.64]], \
                      [[15.52, 1.4],   [5.77, 1.4],   [3.54, 1.4],   [2.556, 1.4],   [2, 1.4],   [1.64, 1.4],   [1.4, 1.4],   [1.21, 1.4],    [1.07, 1.4]], \
                      [[15.52, 1.21],  [5.77, 1.21],  [3.54, 1.21],  [2.556, 1.21],  [2, 1.21],  [1.64, 1.21],  [1.4, 1.21],  [1.21, 1.21],   [1.07, 1.21]], \
                      [[15.52, 1.07],  [5.77, 1.07],  [3.54, 1.07],  [2.556, 1.07],  [2, 1.07],  [1.64, 1.07],  [1.4, 1.07],  [1.21, 1.07],   [1.07, 1.07]], 
        
        
        self.turn = 0
    
    def updateboard(self, x, y):
        self.board[x][y][0] = self.turn

        for self.i in range (0, 9):
            for self.j in range (0, 9):
                if self.board[self.i][self.j][0] % 2 == 1:
                    self.board[self.i][self.j][1] = 1
                if self.board[self.i][self.j][0] % 2 == 0 and self.board[self.i][self.j][0] > 1:
                    self.board[self.i][self.j][1] = 2
        
        self.checkrepetition(x, y)
        self.defineterritory()
        self.capture(x, y)

    def defineterritory(self):
        for self.i in range (0, 9):
            for self.j in range (0, 9):
                #self.board[self.i][self.j][2] = 0
                self.blackboard[self.i][self.j][1] = 0
                self.whiteboard[self.i][self.j][1] = 0
                self.blackboard[self.i][self.j][2] = [self.i, self.j]
                self.whiteboard[self.i][self.j][2] = [self.i, self.j]

        #Populate Black/White Boards
        for self.i in range(0, 9):
            for self.j in range(0, 9):
                if self.board[self.i][self.j][0] % 2 == 1:
                    self.blackboard[self.i][self.j][0] = self.board[self.i][self.j][0]
                if self.board[self.i][self.j][0] % 2 == 0 and self.board[self.i][self.j][0] > 1:
                    self.whiteboard[self.i][self.j][0] = self.board[self.i][self.j][0]
        
        self.bbname = 1
        self.bwname = 1

        #Calculate Territories on Both Boards
        for self.i in range(0, 9):
            for self.j in range(0, 9):
                if self.blackboard[self.i][self.j][0] == 0:
                    self.nameblackboundterritory(self.bbname, self.i, self.j)
                    self.bbname += 1
        for self.i in range(0, 9):
            for self.j in range(0, 9):
                if self.whiteboard[self.i][self.j][0] == 0:
                    self.namewhiteboundterritory(self.bwname, self.i, self.j)
                    self.bwname += 1
        
        #Create Lists of Black Territories and White Stones in Black Territories
        self.blackterr = []
        for self.i in range(0, 9):
            for self.j in range(0, 9):
                if self.blackboard[self.i][self.j][0] == 0:
                    self.blackterr.append(self.blackboard[self.i][self.j][1])
        self.blackterrset = set(self.blackterr)
        self.blackterrlist = list(self.blackterrset)
        self.blackterrgroups = []
        self.wstonesinbterr = []
        for self.k in range(len(self.blackterrlist)):
            self.blackterrgroups.append([])
            self.wstonesinbterr.append([])
            for self.i in range(0, 9):
                for self.j in range(0, 9):
                    if self.blackboard[self.i][self.j][0] == 0 and self.blackboard[self.i][self.j][1] == self.blackterrlist[self.k]:
                        self.blackterrgroups[self.k].append(self.blackboard[self.i][self.j])
                        if self.whiteboard[self.i][self.j][0] % 2 == 0 and self.whiteboard[self.i][self.j][0] > 1:
                            self.wstonesinbterr[self.k].append(self.blackboard[self.i][self.j])
        
        #Create Lists of White Territories and Black Stones in White Territories
        self.whiteterr = []
        for self.i in range(0, 9):
            for self.j in range(0, 9):
                if self.whiteboard[self.i][self.j][0] == 0:
                    self.whiteterr.append(self.whiteboard[self.i][self.j][1])
        self.whiteterrset = set(self.whiteterr)
        self.whiteterrlist = list(self.whiteterrset)
        self.whiteterrgroups = []
        self.bstonesinwterr = []
        for self.k in range(len(self.whiteterrlist)):
            self.whiteterrgroups.append([])
            self.bstonesinwterr.append([])
            for self.i in range(0, 9):
                for self.j in range(0, 9):
                    if self.whiteboard[self.i][self.j][0] == 0 and self.whiteboard[self.i][self.j][1] == self.whiteterrlist[self.k]:
                        self.whiteterrgroups[self.k].append(self.whiteboard[self.i][self.j])
                        if self.blackboard[self.i][self.j][0] % 2 == 1:
                            self.bstonesinwterr[self.k].append(self.whiteboard[self.i][self.j])
    
    def capture(self, x, y):
        #Capture White Groups
        if self.turn % 2 == 1:
            for self.i in range(len(self.blackterrgroups)):
                if len(self.wstonesinbterr[self.i]) == len(self.blackterrgroups[self.i]):
                    for self.k in self.wstonesinbterr[self.i]:
                        self.x, self.y = self.k[2]
                        self.board[self.x][self.y][0] = 0
                        self.board[self.x][self.y][1] = 0
                        self.whiteboard[self.x][self.y][0] = 0
                        self.whiteboard[self.x][self.y][1] = 0
                        self.whiteboard[self.x][self.y][2] = 0
            #Suicide? 
            self.defineterritory()
            for self.i in range(len(self.whiteterrgroups)):
                if len(self.bstonesinwterr[self.i]) == len(self.whiteterrgroups[self.i]):
                    self.board[x][y][0] = 0
                    self.board[x][y][1] = 0
                    self.blackboard[x][y][0] = 0
                    self.blackboard[x][y][1] = 0
                    self.blackboard[x][y][2] = 0
                    self.turn -= 1
        #Capture Black Groups
        if self.turn % 2 == 0:
            for self.i in range(len(self.whiteterrgroups)):
                if len(self.bstonesinwterr[self.i]) == len(self.whiteterrgroups[self.i]):
                    for self.k in self.bstonesinwterr[self.i]:
                        self.x, self.y = self.k[2]
                        self.board[self.x][self.y][0] = 0
                        self.board[self.x][self.y][1] = 0
                        self.blackboard[self.x][self.y][0] = 0
                        self.blackboard[self.x][self.y][1] = 0
                        self.blackboard[self.x][self.y][2] = 0
            #Suicide?
            self.defineterritory()
            for self.i in range(len(self.blackterrgroups)):
                if len(self.wstonesinbterr[self.i]) == len(self.blackterrgroups[self.i]):
                    self.board[x][y][0] = 0
                    self.board[x][y][1] = 0
                    self.whiteboard[x][y][0] = 0
                    self.whiteboard[x][y][1] = 0
                    self.whiteboard[x][y][2] = 0
                    self.turn -= 1
    
    def nameblackboundterritory(self, bbname, i, j):
        if self.blackboard[i][j][0] == 0 and self.blackboard[i][j][1] == 0:
            self.blackboard[i][j][1] = bbname

        if j < 8 and self.blackboard[i][j + 1][0] == 0 and self.blackboard[i][j + 1][1] == 0 :
            self.nameblackboundterritory(bbname, i, j + 1)

        if j >= 1 and self.blackboard[i][j - 1][0] == 0 and self.blackboard[i][j - 1][1] == 0 :
            self.nameblackboundterritory(bbname, i, j - 1)

        if i < 8 and self.blackboard[i + 1][j][0] == 0 and self.blackboard[i + 1][j][1] == 0 :
            self.nameblackboundterritory(bbname, i + 1, j)

        if i >= 1 and self.blackboard[i - 1][j][0] == 0 and self.blackboard[i - 1][j][1] == 0 :
            self.nameblackboundterritory(bbname, i - 1, j)
            
        return
    
    def namewhiteboundterritory(self, bwname, i, j):
        if self.whiteboard[i][j][0] == 0 and self.whiteboard[i][j][1] == 0:
            self.whiteboard[i][j][1] = bwname

        if j < 8 and self.whiteboard[i][j + 1][0] == 0 and self.whiteboard[i][j + 1][1] == 0 :
            self.namewhiteboundterritory(bwname, i, j + 1)

        if j >= 1 and self.whiteboard[i][j - 1][0] == 0 and self.whiteboard[i][j - 1][1] == 0 :
            self.namewhiteboundterritory(bwname, i, j - 1)

        if i < 8 and self.whiteboard[i + 1][j][0] == 0 and self.whiteboard[i + 1][j][1] == 0 :
            self.namewhiteboundterritory(bwname, i + 1, j)

        if i >= 1 and self.whiteboard[i - 1][j][0] == 0 and self.whiteboard[i - 1][j][1] == 0 :
            self.namewhiteboundterritory(bwname, i - 1, j)
            
        return
    
    def drawboard(self, screen, image):
        screen.blit(image, (0, 0))
        for self.i in range(0, 9):
            for self.j in range(0, 9):
                if self.board[self.i][self.j][0] % 2 == 1 and self.board[self.i][self.j][0] >= 1: 
                    pygame.draw.circle(screen,(0,0,0),(image.get_width()/self.coords[self.i][self.j][0],image.get_height()/self.coords[self.i][self.j][1]), image.get_width()/20)
                if self.board[self.i][self.j][0] % 2 == 0 and self.board[self.i][self.j][0] > 0: 
                    pygame.draw.circle(screen,(255,255,255),(image.get_width()/self.coords[self.i][self.j][0],image.get_height()/self.coords[self.i][self.j][1]), image.get_width()/20)
        pygame.display.flip()
    
    def showmovenumber(self, screen, image):
        self.BLUE = pygame.Color('dodgerblue1')
        self.FONT = pygame.font.Font(None, image.get_width()//18)

        for self.i in range(0, 9):
            for self.j in range(0, 9):
                if self.board[self.i][self.j][0] % 2 == 1 and self.board[self.i][self.j][0] >= 1: 
                    self.number = self.FONT.render(str(self.board[self.i][self.j][0]), True, (255,255,255))
                    self.number_rect = self.number.get_rect(center=(image.get_width()/self.coords[self.i][self.j][0],image.get_height()/self.coords[self.i][self.j][1]))
                    screen.blit(self.number, self.number_rect)
                if self.board[self.i][self.j][0] % 2 == 0 and self.board[self.i][self.j][0] > 0: 
                    self.number = self.FONT.render(str(self.board[self.i][self.j][0]), True, (0,0,0))
                    self.number_rect = self.number.get_rect(center=(image.get_width()/self.coords[self.i][self.j][0],image.get_height()/self.coords[self.i][self.j][1]))
                    screen.blit(self.number, self.number_rect)
        pygame.display.flip()

    
    def checkrepetition(self, x, y):
        self.boardhist.append([])
        for self.i in range(0, 9):
            for self.j in range(0, 9):
                self.boardhist[len(self.boardhist)-1].append(self.board[self.i][self.j][1])
        
        #Repetition?
        if self.turn > 3:
            self.repetition = 0
            for self.i in range(0, 81):
                if self.boardhist[len(self.boardhist)-1][self.i] != self.boardhist[len(self.boardhist)-2][self.i]:
                    self.repetition += 1
    
            if self.repetition == 0: 
                self.board[x][y][0] = 0
                self.board[x][y][1] = 0
                self.blackboard[x][y][0] = 0
                self.blackboard[x][y][1] = 0
                self.blackboard[x][y][2] = 0
                self.whiteboard[x][y][0] = 0
                self.whiteboard[x][y][1] = 0
                self.whiteboard[x][y][2] = 0
                self.turn -= 1
    
    def backonemove(self):
        if self.turn > 0:
            for self.i in range (0, 9):
                for self.j in range (0, 9):
                    if self.board[self.i][self.j][0] == self.turn:
                        self.board[self.i][self.j][0] = 0
                        self.board[self.i][self.j][1] = 0
                        self.blackboard[self.i][self.j][0] = 0
                        self.blackboard[self.i][self.j][1] = 0
                        self.blackboard[self.i][self.j][2] = 0
                        self.whiteboard[self.i][self.j][0] = 0
                        self.whiteboard[self.i][self.j][1] = 0
                        self.whiteboard[self.i][self.j][2] = 0
            self.turn -= 1
            self.boardhist.pop(len(self.boardhist)-1)
    
    def passturn(self):
        self.turn += 1
        self.boardhist.append([])
        for self.i in range(0, 81):
            self.boardhist[len(self.boardhist)-1].append(3)



            

