import pygame

class Buttons():
    def __init__(self, screen, imagerect):
        self.screen = screen
        self.imagerect = imagerect
        self.font = pygame.font.Font(None, 25)
        self.turn = 0
        self.movebutton = 0
    
        #Get Move Numbers Button
        self.move = pygame.Surface((screen.get_width()/5,screen.get_height()/14))
        self.move_rect = self.move.fill((210,210,210))
        self.move_rect.topleft = imagerect.bottomleft
        self.move_rect = self.move_rect.move(10, 20)
        self.move_rect = screen.blit(self.move, self.move_rect)
        self.text = self.font.render('Show Move #s', True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.move_rect.center
        screen.blit(self.text, self.text_rect)

        #Go Back One Move Button

        self.back = pygame.Surface((screen.get_width()/5,screen.get_height()/14))
        self.back_rect = self.back.fill((210,210,210))
        self.back_rect.topleft = self.move_rect.topright
        self.back_rect = self.back_rect.move(20, 0)
        self.back_rect = screen.blit(self.back, self.back_rect)
        self.text = self.font.render('Back', True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.back_rect.center
        screen.blit(self.text, self.text_rect)
        

        #Pass Button

        self.passturn = pygame.Surface((screen.get_width()/5,screen.get_height()/14))
        self.passturn_rect = self.passturn.fill((210,210,210))
        self.passturn_rect.topleft = self.back_rect.topright
        self.passturn_rect = self.passturn_rect.move(20, 0)
        self.passturn_rect = screen.blit(self.passturn, self.passturn_rect)
        self.text = self.font.render('Pass', True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.passturn_rect.center
        screen.blit(self.text, self.text_rect)