import pygame
import random
import time

class AIPlayer():
    def __init__(self, btn):
        self.black = 0
        self.white = 0
        self.btn = btn
        self.passturn = 0

    def compblackplayermove(self, bd, btn, screen, image, imagerect, start):
        self.start = time.time()
        if btn.turn % 2 == 1:
            self.rmove = random.randint(0, 80)
            if bd.board[self.rmove//9][self.rmove%9] == 0:
                self.start = time.time()
                self.bool = bd.updateboard(self.rmove//9, self.rmove%9, btn)
                if self.bool:
                    self.end = time.time()
                    if self.end - start < 2:
                        return True
                    else: 
                        self.passmove(bd, screen, image, imagerect, btn)
                        return False
                else:
                    return False
            else:
                return self.compblackplayermove(bd, btn, screen, image, imagerect, start)

    def compwhiteplayermove(self, bd, btn, screen, image, imagerect, start):
        if btn.turn % 2 == 0 and btn.turn > 1:
            self.rmove = random.randint(0, 80)
            if bd.board[self.rmove//9][self.rmove%9] == 0:
                self.bool = bd.updateboard(self.rmove//9, self.rmove%9, btn)
                if self.bool:
                    self.end = time.time()
                    if self.end - start < 2:
                        return True
                    else: 
                        self.passmove(bd, screen, image, imagerect, btn)
                        return False
                else:
                    return False
            else:
                return self.compwhiteplayermove(bd, btn, screen, image, imagerect, start)
    
    def passmove(self, bd, screen, image, imagerect, btn):
        bd.passturn(screen, imagerect, btn)
        bd.saveboard(btn)
        bd.drawboard(screen, image)
        


    
    
