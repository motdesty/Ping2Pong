import pygame, sys
import pygame.freetype
import time
import sys
import itertools
from pygame.locals import *
import threading

from math import pi


pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Ping 2 Pong")
Clock = pygame.time.Clock()

objects = []

done = False

# light shade of the button when it's hovered
color_light = (173,216,230) 
  
# dark shade of the button 
color_dark = (135,206,250) 

BG = (65,105,225)  #(106, 159, 181)
WHITE = (255,255,255)
BLACK = (0, 0, 0)
L_GRAY = (200, 200, 200)
ORANGE = (255, 195, 90)


screenFont = pygame.font.SysFont("arial", 15, True, True)
loadingFont = pygame.font.SysFont("arial", 100, True, True)
readyFont = pygame.font.SysFont("arial", 40, True, True)

chattingText = screenFont.render("Chatting Screen", True, WHITE)
userText = screenFont.render("User Screen", True, WHITE)

P2PText = loadingFont.render("P 2 P", True, BG)
p2pText = screenFont.render("PING                  to                PONG", True, BG)
waitText = screenFont.render("Waiting for opponent user . . .", True, BG)
player1Text = screenFont.render("USER 1", True, WHITE)
player2Text = screenFont.render("USER 2", True, WHITE)


readyText = readyFont.render("READY!", True, ORANGE)



inputText = "Please write here"

WriteHere = screenFont.render(inputText, True, WHITE)
writeBox = WriteHere.get_rect()
writeBox.topleft = (35, 545)
writeCursor = pygame.Rect(writeBox.topright,(3, writeBox.height))
print(writeCursor)





class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = screenFont.render(buttonText, True, WHITE)
        self.alreadyPressed = False


        objects.append(self)



    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(BG)
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(ORANGE)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False


        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2])
        screen.blit(self.buttonSurface, self.buttonRect)


def readyFunction1():
    
    screen.blit(readyText, (618, 100))




'''if player 2 is ready, show the text'''

def readyFunction2():
    
    screen.blit(readyText, (618, 370))






screen.fill(WHITE)

''' loading screen '''
pygame.draw.rect(screen, BG, [15, 15, 550, 350], 2)
    

pygame.draw.rect(screen, BG, [580, 15, 205, 570])
pygame.draw.rect(screen, WHITE, [590, 25, 185, 550], 2)
pygame.draw.rect(screen, BG, [610, 25, 100, 30])
    

''' user1 '''
pygame.draw.rect(screen, WHITE, [605, 50, 155, 155])
pygame.draw.circle(screen, BG, [682, 110], 30, 7)
pygame.draw.arc(screen, BG, [616, 150, 130, 200], 0, pi/2, 7)
pygame.draw.arc(screen, BG, [616, 150, 130, 200], pi/2, pi, 7)
screen.blit(player1Text, (660, 215))


''' user2 '''
pygame.draw.rect(screen, WHITE, [605, 315, 155, 155])
pygame.draw.circle(screen, BG, [682, 375], 30, 7)
pygame.draw.arc(screen, BG, [616, 415, 130, 200], 0, pi/2, 7)
pygame.draw.arc(screen, BG, [616, 415, 130, 200], pi/2, pi, 7)
screen.blit(player2Text, (660, 485))
    
    
''' chatting screen '''
pygame.draw.rect(screen, BG, [15, 380, 550, 205], 2)
pygame.draw.rect(screen, BG, [15, 380, 200, 30])
    
    
''' text line '''
pygame.draw.rect(screen, L_GRAY, [30, 540, 520, 30])




screen.blit(P2PText, (100, 100))
screen.blit(p2pText, (115, 97))
screen.blit(waitText, (50, 320))
    
screen.blit(chattingText, (25, 385))
screen.blit(userText, (625, 20))





readyBtn1 = Button(645, 240, 70, 40, 'READY',readyFunction1)









carryOn = True

while not done:

    Clock.tick(60)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(inputText)> 0:
                    inputText = inputText[:-1]
                    print("x")

            else:
                inputText += event.unicode
                print("o")
            WriteHere = screenFont.render(inputText,True,WHITE)
            writeBox.size = WriteHere.get_size()
            writeCursor.topleft = writeBox.topright
        



    for object in objects:
        object.process()

        



    pygame.draw.rect(screen, L_GRAY, [30, 540, 520, 30])
    screen.blit(WriteHere, writeBox)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, WHITE, writeCursor)

    pygame.display.update()









    
    









    pygame.display.flip()




pygame.quit()
