import pygame 
from goclasses import Board

pygame.init()

screen = pygame.display.set_mode((600, 700), pygame.RESIZABLE) 
screen_rect = screen.fill((210,180,140))
pygame.display.set_caption("Go")
font = pygame.font.Font(None, 25)

image = pygame.image.load('go9x9.png')
image = pygame.transform.scale(image, (600, 600))
imagerect = image.get_rect()
bd = Board()


AA = pygame.Surface((image.get_width()/15,image.get_height()/15))
AB = pygame.Surface((image.get_width()/15,image.get_height()/15))
AC = pygame.Surface((image.get_width()/15,image.get_height()/15))
AD = pygame.Surface((image.get_width()/15,image.get_height()/15))
AE = pygame.Surface((image.get_width()/15,image.get_height()/15))
AF = pygame.Surface((image.get_width()/15,image.get_height()/15))
AG = pygame.Surface((image.get_width()/15,image.get_height()/15))
AH = pygame.Surface((image.get_width()/15,image.get_height()/15))
AI = pygame.Surface((image.get_width()/15,image.get_height()/15))

BA = pygame.Surface((image.get_width()/15,image.get_height()/15))
BB = pygame.Surface((image.get_width()/15,image.get_height()/15))
BC = pygame.Surface((image.get_width()/15,image.get_height()/15))
BD = pygame.Surface((image.get_width()/15,image.get_height()/15))
BE = pygame.Surface((image.get_width()/15,image.get_height()/15))
BF = pygame.Surface((image.get_width()/15,image.get_height()/15))
BG = pygame.Surface((image.get_width()/15,image.get_height()/15))
BH = pygame.Surface((image.get_width()/15,image.get_height()/15))
BI = pygame.Surface((image.get_width()/15,image.get_height()/15))

CA = pygame.Surface((image.get_width()/15,image.get_height()/15))
CB = pygame.Surface((image.get_width()/15,image.get_height()/15))
CC = pygame.Surface((image.get_width()/15,image.get_height()/15))
CD = pygame.Surface((image.get_width()/15,image.get_height()/15))
CE = pygame.Surface((image.get_width()/15,image.get_height()/15))
CF = pygame.Surface((image.get_width()/15,image.get_height()/15))
CG = pygame.Surface((image.get_width()/15,image.get_height()/15))
CH = pygame.Surface((image.get_width()/15,image.get_height()/15))
CI = pygame.Surface((image.get_width()/15,image.get_height()/15))

DA = pygame.Surface((image.get_width()/15,image.get_height()/15))
DB = pygame.Surface((image.get_width()/15,image.get_height()/15))
DC = pygame.Surface((image.get_width()/15,image.get_height()/15))
DD = pygame.Surface((image.get_width()/15,image.get_height()/15))
DE = pygame.Surface((image.get_width()/15,image.get_height()/15))
DF = pygame.Surface((image.get_width()/15,image.get_height()/15))
DG = pygame.Surface((image.get_width()/15,image.get_height()/15))
DH = pygame.Surface((image.get_width()/15,image.get_height()/15))
DI = pygame.Surface((image.get_width()/15,image.get_height()/15))

EA = pygame.Surface((image.get_width()/15,image.get_height()/15))
EB = pygame.Surface((image.get_width()/15,image.get_height()/15))
EC = pygame.Surface((image.get_width()/15,image.get_height()/15))
ED = pygame.Surface((image.get_width()/15,image.get_height()/15))
EE = pygame.Surface((image.get_width()/15,image.get_height()/15))
EF = pygame.Surface((image.get_width()/15,image.get_height()/15))
EG = pygame.Surface((image.get_width()/15,image.get_height()/15))
EH = pygame.Surface((image.get_width()/15,image.get_height()/15))
EI = pygame.Surface((image.get_width()/15,image.get_height()/15))

FA = pygame.Surface((image.get_width()/15,image.get_height()/15))
FB = pygame.Surface((image.get_width()/15,image.get_height()/15))
FC = pygame.Surface((image.get_width()/15,image.get_height()/15))
FD = pygame.Surface((image.get_width()/15,image.get_height()/15))
FE = pygame.Surface((image.get_width()/15,image.get_height()/15))
FF = pygame.Surface((image.get_width()/15,image.get_height()/15))
FG = pygame.Surface((image.get_width()/15,image.get_height()/15))
FH = pygame.Surface((image.get_width()/15,image.get_height()/15))
FI = pygame.Surface((image.get_width()/15,image.get_height()/15))

GA = pygame.Surface((image.get_width()/15,image.get_height()/15))
GB = pygame.Surface((image.get_width()/15,image.get_height()/15))
GC = pygame.Surface((image.get_width()/15,image.get_height()/15))
GD = pygame.Surface((image.get_width()/15,image.get_height()/15))
GE = pygame.Surface((image.get_width()/15,image.get_height()/15))
GF = pygame.Surface((image.get_width()/15,image.get_height()/15))
GG = pygame.Surface((image.get_width()/15,image.get_height()/15))
GH = pygame.Surface((image.get_width()/15,image.get_height()/15))
GI = pygame.Surface((image.get_width()/15,image.get_height()/15))

HA = pygame.Surface((image.get_width()/15,image.get_height()/15))
HB = pygame.Surface((image.get_width()/15,image.get_height()/15))
HC = pygame.Surface((image.get_width()/15,image.get_height()/15))
HD = pygame.Surface((image.get_width()/15,image.get_height()/15))
HE = pygame.Surface((image.get_width()/15,image.get_height()/15))
HF = pygame.Surface((image.get_width()/15,image.get_height()/15))
HG = pygame.Surface((image.get_width()/15,image.get_height()/15))
HH = pygame.Surface((image.get_width()/15,image.get_height()/15))
HI = pygame.Surface((image.get_width()/15,image.get_height()/15))

IA = pygame.Surface((image.get_width()/15,image.get_height()/15))
IB = pygame.Surface((image.get_width()/15,image.get_height()/15))
IC = pygame.Surface((image.get_width()/15,image.get_height()/15))
ID = pygame.Surface((image.get_width()/15,image.get_height()/15))
IE = pygame.Surface((image.get_width()/15,image.get_height()/15))
IF = pygame.Surface((image.get_width()/15,image.get_height()/15))
IG = pygame.Surface((image.get_width()/15,image.get_height()/15))
IH = pygame.Surface((image.get_width()/15,image.get_height()/15))
II = pygame.Surface((image.get_width()/15,image.get_height()/15))

AA_rect = screen.blit(AA, (image.get_width()/32.1,image.get_height()/32.1))
AB_rect = screen.blit(AB, (image.get_width()/7.1,image.get_height()/32.1))
AC_rect = screen.blit(AC, (image.get_width()/4.2,image.get_height()/32.1))
AD_rect = screen.blit(AD, (image.get_width()/2.8,image.get_height()/32.1))
AE_rect = screen.blit(AE, (image.get_width()/2.1,image.get_height()/32.1))
AF_rect = screen.blit(AF, (image.get_width()/1.7,image.get_height()/32.1))
AG_rect = screen.blit(AG, (image.get_width()/1.46,image.get_height()/32.1))
AH_rect = screen.blit(AH, (image.get_width()/1.26,image.get_height()/32.1))
AI_rect = screen.blit(AI, (image.get_width()/1.1,image.get_height()/32.1))

BA_rect = screen.blit(BA, (image.get_width()/32.1 ,image.get_height()/7.1))
BB_rect = screen.blit(BB, (image.get_width()/7.1,image.get_height()/7.1))
BC_rect = screen.blit(BC, (image.get_width()/4.2,image.get_height()/7.1))
BD_rect = screen.blit(BD, (image.get_width()/2.8,image.get_height()/7.1))
BE_rect = screen.blit(BE, (image.get_width()/2.1,image.get_height()/7.1))
BF_rect = screen.blit(BF, (image.get_width()/1.7,image.get_height()/7.1))
BG_rect = screen.blit(BG, (image.get_width()/1.46,image.get_height()/7.1))
BH_rect = screen.blit(BH, (image.get_width()/1.26,image.get_height()/7.1))
BI_rect = screen.blit(BI, (image.get_width()/1.1,image.get_height()/7.1))

CA_rect = screen.blit(CA, (image.get_width()/32.1 ,image.get_height()/4.2))
CB_rect = screen.blit(CB, (image.get_width()/7.1,image.get_height()/4.2))
CC_rect = screen.blit(CC, (image.get_width()/4.2,image.get_height()/4.2))
CD_rect = screen.blit(CD, (image.get_width()/2.8,image.get_height()/4.2))
CE_rect = screen.blit(CE, (image.get_width()/2.1,image.get_height()/4.2))
CF_rect = screen.blit(CF, (image.get_width()/1.7,image.get_height()/4.2))
CG_rect = screen.blit(CG, (image.get_width()/1.46,image.get_height()/4.2))
CH_rect = screen.blit(CH, (image.get_width()/1.26,image.get_height()/4.2))
CI_rect = screen.blit(CI, (image.get_width()/1.1,image.get_height()/4.2))

DA_rect = screen.blit(DA, (image.get_width()/32.1 ,image.get_height()/2.8))
DB_rect = screen.blit(DB, (image.get_width()/7.1,image.get_height()/2.8))
DC_rect = screen.blit(DC, (image.get_width()/4.2,image.get_height()/2.8))
DD_rect = screen.blit(DD, (image.get_width()/2.8,image.get_height()/2.8))
DE_rect = screen.blit(DE, (image.get_width()/2.1,image.get_height()/2.8))
DF_rect = screen.blit(DF, (image.get_width()/1.7,image.get_height()/2.8))
DG_rect = screen.blit(DG, (image.get_width()/1.46,image.get_height()/2.8))
DH_rect = screen.blit(DH, (image.get_width()/1.26,image.get_height()/2.8))
DI_rect = screen.blit(DI, (image.get_width()/1.1,image.get_height()/2.8))

EA_rect = screen.blit(EA, (image.get_width()/32.1 ,image.get_height()/2.1))
EB_rect = screen.blit(EB, (image.get_width()/7.1,image.get_height()/2.1))
EC_rect = screen.blit(EC, (image.get_width()/4.2,image.get_height()/2.1))
ED_rect = screen.blit(ED, (image.get_width()/2.8,image.get_height()/2.1))
EE_rect = screen.blit(EE, (image.get_width()/2.1,image.get_height()/2.1))
EF_rect = screen.blit(EF, (image.get_width()/1.7,image.get_height()/2.1))
EG_rect = screen.blit(EG, (image.get_width()/1.46,image.get_height()/2.1))
EH_rect = screen.blit(EH, (image.get_width()/1.26,image.get_height()/2.1))
EI_rect = screen.blit(EI, (image.get_width()/1.1,image.get_height()/2.1))

FA_rect = screen.blit(FA, (image.get_width()/32.1 ,image.get_height()/1.7))
FB_rect = screen.blit(FB, (image.get_width()/7.1,image.get_height()/1.7))
FC_rect = screen.blit(FC, (image.get_width()/4.2,image.get_height()/1.7))
FD_rect = screen.blit(FD, (image.get_width()/2.8,image.get_height()/1.7))
FE_rect = screen.blit(FE, (image.get_width()/2.1,image.get_height()/1.7))
FF_rect = screen.blit(FF, (image.get_width()/1.7,image.get_height()/1.7))
FG_rect = screen.blit(FG, (image.get_width()/1.46,image.get_height()/1.7))
FH_rect = screen.blit(FH, (image.get_width()/1.26,image.get_height()/1.7))
FI_rect = screen.blit(FI, (image.get_width()/1.1,image.get_height()/1.7))

GA_rect = screen.blit(GA, (image.get_width()/32.1 ,image.get_height()/1.46))
GB_rect = screen.blit(GB, (image.get_width()/7.1,image.get_height()/1.46))
GC_rect = screen.blit(GC, (image.get_width()/4.2,image.get_height()/1.46))
GD_rect = screen.blit(GD, (image.get_width()/2.8,image.get_height()/1.46))
GE_rect = screen.blit(GE, (image.get_width()/2.1,image.get_height()/1.46))
GF_rect = screen.blit(GF, (image.get_width()/1.7,image.get_height()/1.46))
GG_rect = screen.blit(GG, (image.get_width()/1.46,image.get_height()/1.46))
GH_rect = screen.blit(GH, (image.get_width()/1.26,image.get_height()/1.46))
GI_rect = screen.blit(GI, (image.get_width()/1.1,image.get_height()/1.46))

HA_rect = screen.blit(HA, (image.get_width()/32.1,image.get_height()/1.26))
HB_rect = screen.blit(HB, (image.get_width()/7.1,image.get_height()/1.26))
HC_rect = screen.blit(HC, (image.get_width()/4.2,image.get_height()/1.26))
HD_rect = screen.blit(HD, (image.get_width()/2.8,image.get_height()/1.26))
HE_rect = screen.blit(HE, (image.get_width()/2.1,image.get_height()/1.26))
HF_rect = screen.blit(HF, (image.get_width()/1.7,image.get_height()/1.26))
HG_rect = screen.blit(HG, (image.get_width()/1.46,image.get_height()/1.26))
HH_rect = screen.blit(HH, (image.get_width()/1.26,image.get_height()/1.26))
HI_rect = screen.blit(HI, (image.get_width()/1.1,image.get_height()/1.26))

IA_rect = screen.blit(IA, (image.get_width()/32.1 ,image.get_height()/1.1))
IB_rect = screen.blit(IB, (image.get_width()/7.1,image.get_height()/1.1))
IC_rect = screen.blit(IC, (image.get_width()/4.2,image.get_height()/1.1))
ID_rect = screen.blit(ID, (image.get_width()/2.8,image.get_height()/1.1))
IE_rect = screen.blit(IE, (image.get_width()/2.1,image.get_height()/1.1))
IF_rect = screen.blit(IF, (image.get_width()/1.7,image.get_height()/1.1))
IG_rect = screen.blit(IG, (image.get_width()/1.46,image.get_height()/1.1))
IH_rect = screen.blit(IH, (image.get_width()/1.26,image.get_height()/1.1))
II_rect = screen.blit(II, (image.get_width()/1.1,image.get_height()/1.1))

#Get Move Numbers Button
move = pygame.Surface((image.get_width()/5,image.get_height()/10))
move_rect = move.fill((210,210,210))
move_rect.topleft = imagerect.bottomleft
move_rect = move_rect.move(10, 20)
move_rect = screen.blit(move, move_rect)
text = font.render('Show Move #s', True, (0,0,0))
text_rect = text.get_rect()
text_rect.center = move_rect.center
screen.blit(text, text_rect)
movebutton = 0

#Go Back One Move Button

back = pygame.Surface((image.get_width()/5,image.get_height()/10))
back_rect = back.fill((210,210,210))
back_rect.topleft = move_rect.topright
back_rect = back_rect.move(20, 0)
back_rect = screen.blit(back, back_rect)
text = font.render('Back', True, (0,0,0))
text_rect = text.get_rect()
text_rect.center = back_rect.center
screen.blit(text, text_rect)
backbutton = 0

#Pass Button

passturn = pygame.Surface((image.get_width()/5,image.get_height()/10))
passturn_rect = passturn.fill((210,210,210))
passturn_rect.topleft = back_rect.topright
passturn_rect = passturn_rect.move(20, 0)
passturn_rect = screen.blit(passturn, passturn_rect)
text = font.render('Pass', True, (0,0,0))
text_rect = text.get_rect()
text_rect.center = passturn_rect.center
screen.blit(text, text_rect)
passbutton = 0

screen.blit(image, (0, 0))

pygame.display.flip()

go = True

while True: 
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if move_rect.collidepoint(pos):
                movebutton += 1
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
                if movebutton % 2 == 0:
                    bd.drawboard(screen,image)
            if AA_rect.collidepoint(pos) and (bd.board[0][0][0] == 0):
                bd.turn += 1
                bd.updateboard(0, 0)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if AB_rect.collidepoint(pos) and (bd.board[0][1][0] == 0):
                bd.turn += 1
                bd.updateboard(0, 1)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if AC_rect.collidepoint(pos) and (bd.board[0][2][0] == 0):
                bd.turn += 1
                bd.updateboard(0, 2)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if AD_rect.collidepoint(pos) and (bd.board[0][3][0] == 0):
                bd.turn += 1
                bd.updateboard(0, 3)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if AE_rect.collidepoint(pos) and (bd.board[0][4][0] == 0):
                bd.turn += 1
                bd.updateboard(0, 4)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if AF_rect.collidepoint(pos) and (bd.board[0][5][0] == 0):
                bd.turn += 1
                bd.updateboard(0, 5)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if AG_rect.collidepoint(pos) and (bd.board[0][6][0] == 0):
                bd.turn += 1
                bd.updateboard(0, 6)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if AH_rect.collidepoint(pos) and (bd.board[0][7][0] == 0):
                bd.turn += 1
                bd.updateboard(0, 7)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if AI_rect.collidepoint(pos) and (bd.board[0][8][0] == 0):
                bd.turn += 1
                bd.updateboard(0, 8)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if BA_rect.collidepoint(pos) and (bd.board[1][0][0] == 0):
                bd.turn += 1
                bd.updateboard(1, 0)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if BB_rect.collidepoint(pos) and (bd.board[1][1][0] == 0):
                bd.turn += 1
                bd.updateboard(1, 1) 
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if BC_rect.collidepoint(pos) and (bd.board[1][2][0] == 0):
                bd.turn += 1
                bd.updateboard(1, 2) 
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if BD_rect.collidepoint(pos) and (bd.board[1][3][0] == 0):
                bd.turn += 1
                bd.updateboard(1, 3)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if BE_rect.collidepoint(pos) and (bd.board[1][4][0] == 0):
                bd.turn += 1
                bd.updateboard(1, 4)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if BF_rect.collidepoint(pos) and (bd.board[1][5][0] == 0):
                bd.turn += 1
                bd.updateboard(1, 5)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if BG_rect.collidepoint(pos) and (bd.board[1][6][0] == 0):
                bd.turn += 1
                bd.updateboard(1, 6)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if BH_rect.collidepoint(pos) and (bd.board[1][7][0] == 0):
                bd.turn += 1
                bd.updateboard(1, 7)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if BI_rect.collidepoint(pos) and (bd.board[1][8][0] == 0):
                bd.turn += 1
                bd.updateboard(1, 8)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if CA_rect.collidepoint(pos) and (bd.board[2][0][0] == 0):
                bd.turn += 1
                bd.updateboard(2, 0)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if CB_rect.collidepoint(pos) and (bd.board[2][1][0] == 0):
                bd.turn += 1
                bd.updateboard(2, 1)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if CC_rect.collidepoint(pos) and (bd.board[2][2][0] == 0):
                bd.turn += 1
                bd.updateboard(2, 2)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if CD_rect.collidepoint(pos) and (bd.board[2][3][0] == 0):
                bd.turn += 1
                bd.updateboard(2, 3)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if CE_rect.collidepoint(pos) and (bd.board[2][4][0] == 0):
                bd.turn += 1
                bd.updateboard(2, 4)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if CF_rect.collidepoint(pos) and (bd.board[2][5][0] == 0):
                bd.turn += 1
                bd.updateboard(2, 5)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if CG_rect.collidepoint(pos) and (bd.board[2][6][0] == 0):
                bd.turn += 1
                bd.updateboard(2, 6)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if CH_rect.collidepoint(pos) and (bd.board[2][7][0] == 0):
                bd.turn += 1
                bd.updateboard(2, 7)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if CI_rect.collidepoint(pos) and (bd.board[2][8][0] == 0):
                bd.turn += 1
                bd.updateboard(2, 8)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if DA_rect.collidepoint(pos) and (bd.board[3][0][0] == 0):
                bd.turn += 1
                bd.updateboard(3, 0)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if DB_rect.collidepoint(pos) and (bd.board[3][1][0] == 0):
                bd.turn += 1
                bd.updateboard(3, 1)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if DC_rect.collidepoint(pos) and (bd.board[3][2][0] == 0):
                bd.turn += 1
                bd.updateboard(3, 2)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if DD_rect.collidepoint(pos) and (bd.board[3][3][0] == 0):
                bd.turn += 1
                bd.updateboard(3, 3)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if DE_rect.collidepoint(pos) and (bd.board[3][4][0] == 0):
                bd.turn += 1
                bd.updateboard(3, 4)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if DF_rect.collidepoint(pos) and (bd.board[3][5][0] == 0):
                bd.turn += 1
                bd.updateboard(3, 5)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if DG_rect.collidepoint(pos) and (bd.board[3][6][0] == 0):
                bd.turn += 1
                bd.updateboard(3, 6)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if DH_rect.collidepoint(pos) and (bd.board[3][7][0] == 0):
                bd.turn += 1
                bd.updateboard(3, 7)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if DI_rect.collidepoint(pos) and (bd.board[3][8][0] == 0):
                bd.turn += 1
                bd.updateboard(3, 8)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if EA_rect.collidepoint(pos) and (bd.board[4][0][0] == 0):
                bd.turn += 1
                bd.updateboard(4, 0)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if EB_rect.collidepoint(pos) and (bd.board[4][1][0] == 0):
                bd.turn += 1
                bd.updateboard(4, 1)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if EC_rect.collidepoint(pos) and (bd.board[4][2][0] == 0):
                bd.turn += 1
                bd.updateboard(4, 2)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)     
            if ED_rect.collidepoint(pos) and (bd.board[4][3][0] == 0):
                bd.turn += 1
                bd.updateboard(4, 3)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if EE_rect.collidepoint(pos) and (bd.board[4][4][0] == 0):
                bd.turn += 1
                bd.updateboard(4, 4)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if EF_rect.collidepoint(pos) and (bd.board[4][5][0] == 0):
                bd.turn += 1
                bd.updateboard(4, 5)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if EG_rect.collidepoint(pos) and (bd.board[4][6][0] == 0):
                bd.turn += 1
                bd.updateboard(4, 6)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if EH_rect.collidepoint(pos) and (bd.board[4][7][0] == 0):
                bd.turn += 1
                bd.updateboard(4, 7)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if EI_rect.collidepoint(pos) and (bd.board[4][8][0] == 0):
                bd.turn += 1
                bd.updateboard(4, 8)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if FA_rect.collidepoint(pos) and (bd.board[5][0][0] == 0):
                bd.turn += 1
                bd.updateboard(5, 0)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if FB_rect.collidepoint(pos) and (bd.board[5][1][0] == 0):
                bd.turn += 1
                bd.updateboard(5, 1)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if FC_rect.collidepoint(pos) and (bd.board[5][2][0] == 0):
                bd.turn += 1
                bd.updateboard(5, 2)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if FD_rect.collidepoint(pos) and (bd.board[5][3][0] == 0):
                bd.turn += 1
                bd.updateboard(5, 3)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if FE_rect.collidepoint(pos) and (bd.board[5][4][0] == 0):
                bd.turn += 1
                bd.updateboard(5, 4)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if FF_rect.collidepoint(pos) and (bd.board[5][5][0] == 0):
                bd.turn += 1
                bd.updateboard(5, 5)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if FG_rect.collidepoint(pos) and (bd.board[5][6][0] == 0):
                bd.turn += 1
                bd.updateboard(5, 6)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if FH_rect.collidepoint(pos) and (bd.board[5][7][0] == 0):
                bd.turn += 1
                bd.updateboard(5, 7)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if FI_rect.collidepoint(pos) and (bd.board[5][8][0] == 0):
                bd.turn += 1
                bd.updateboard(5, 8)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if GA_rect.collidepoint(pos) and (bd.board[6][0][0] == 0):
                bd.turn += 1
                bd.updateboard(6, 0)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if GB_rect.collidepoint(pos) and (bd.board[6][1][0] == 0):
                bd.turn += 1
                bd.updateboard(6, 1)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if GC_rect.collidepoint(pos) and (bd.board[6][2][0] == 0):
                bd.turn += 1
                bd.updateboard(6, 2)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if GD_rect.collidepoint(pos) and (bd.board[6][3][0] == 0):
                bd.turn += 1
                bd.updateboard(6, 3)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if GE_rect.collidepoint(pos) and (bd.board[6][4][0] == 0):
                bd.turn += 1
                bd.updateboard(6, 4)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if GF_rect.collidepoint(pos) and (bd.board[6][5][0] == 0):
                bd.turn += 1
                bd.updateboard(6, 5)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if GG_rect.collidepoint(pos) and (bd.board[6][6][0] == 0):
                bd.turn += 1
                bd.updateboard(6, 6)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if GH_rect.collidepoint(pos) and (bd.board[6][7][0] == 0):
                bd.turn += 1
                bd.updateboard(6, 7)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if GI_rect.collidepoint(pos) and (bd.board[6][8][0] == 0):
                bd.turn += 1
                bd.updateboard(6, 8)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if HA_rect.collidepoint(pos) and (bd.board[7][0][0] == 0):
                bd.turn += 1
                bd.updateboard(7, 0)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if HB_rect.collidepoint(pos) and (bd.board[7][1][0] == 0):
                bd.turn += 1
                bd.updateboard(7, 1)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if HC_rect.collidepoint(pos) and (bd.board[7][2][0] == 0):
                bd.turn += 1
                bd.updateboard(7, 2)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if HD_rect.collidepoint(pos) and (bd.board[7][3][0] == 0):
                bd.turn += 1
                bd.updateboard(7, 3)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if HE_rect.collidepoint(pos) and (bd.board[7][4][0] == 0):
                bd.turn += 1
                bd.updateboard(7, 4)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1: 
                    bd.showmovenumber(screen,image)
            if HF_rect.collidepoint(pos) and (bd.board[7][5][0] == 0):
                bd.turn += 1
                bd.updateboard(7, 5)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if HG_rect.collidepoint(pos) and (bd.board[7][6][0] == 0):
                bd.turn += 1
                bd.updateboard(7, 6)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if HH_rect.collidepoint(pos) and (bd.board[7][7][0] == 0):
                bd.turn += 1
                bd.updateboard(7, 7)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if HI_rect.collidepoint(pos) and (bd.board[7][8][0] == 0):
                bd.turn += 1
                bd.updateboard(7, 8)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if IA_rect.collidepoint(pos) and (bd.board[8][0][0] == 0):
                bd.turn += 1
                bd.updateboard(8, 0)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if IB_rect.collidepoint(pos) and (bd.board[8][1][0] == 0):
                bd.turn += 1
                bd.updateboard(8, 1)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if IC_rect.collidepoint(pos) and (bd.board[8][2][0] == 0):
                bd.turn += 1
                bd.updateboard(8, 2)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if ID_rect.collidepoint(pos) and (bd.board[8][3][0] == 0):
                bd.turn += 1
                bd.updateboard(8, 3)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if IE_rect.collidepoint(pos) and (bd.board[8][4][0] == 0):
                bd.turn += 1
                bd.updateboard(8, 4)
                bd.drawboard(screen, image)
            if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if IF_rect.collidepoint(pos) and (bd.board[8][5][0] == 0):
                bd.turn += 1
                bd.updateboard(8, 5)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if IG_rect.collidepoint(pos) and (bd.board[8][6][0] == 0):
                bd.turn += 1
                bd.updateboard(8, 6) 
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if IH_rect.collidepoint(pos) and (bd.board[8][7][0] == 0):
                bd.turn += 1
                bd.updateboard(8, 7)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if II_rect.collidepoint(pos) and (bd.board[8][8][0] == 0):
                bd.turn += 1
                bd.updateboard(8, 8)
                bd.drawboard(screen, image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if back_rect.collidepoint(pos):
                bd.backonemove()
                bd.drawboard(screen,image)
                if movebutton % 2 == 1:
                    bd.showmovenumber(screen,image)
            if passturn_rect.collidepoint(pos):
                bd.passturn()
        if event.type == pygame.QUIT: 
            pygame.quit() 
            quit() 
            
    pygame.display.flip()

    

        
