# Créé par adry.cales, le 27/04/2023 en Python 3.7
import os

import pygame
from random import randint

from button import *
from player import *
from ghost import *

bgcolor = (19, 19, 19)

pygame.init()
pygame.font.init()

#Ouverture de la fenêtre Pygame
screen = pygame.display.set_mode((1280, 720))
w,h = screen.get_width(), screen.get_height()

## Chargement du SysFont
font = pygame.font.SysFont('c', 50)

#Nommer la page
pygame.display.set_caption("Doudie")

run = True
gameState = "menu"

clock = pygame.time.Clock()

def changeGameState(text):
    global gameState
    gameState = text

def action(action):
    global gameState, bgcolor
    if action == "play":
        gameState = "playing"
        bgcolor = (31, 221, 91)

moving_sprites = pygame.sprite.Group()
joueur = player(w//2, h//2)

moving_sprites.add(joueur)

ghosts = []
ghosts_group = pygame.sprite.Group()

def gerer_event():
    global run, TEXT
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            exit()

        if event.type == pygame.KEYDOWN:
            
            attack(pygame.key.name(event.key))
            joueur.attack()
            
            
            if event.key == pygame.K_g:

                generateGhost()

            if event.key == pygame.K_m:

                for gh in ghosts:
                    if gh.moveData['can_move'] == False:
                        #ghost(gh).moveData['can_move'] = True
                        gh.StartMoving(joueur.x, joueur.y, 20)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if(gameState == "menu"):
                if(btn_play.isOver(pos)):
                    action("play")

#Boutton jouer
btn_play = button((31, 221, 91), w/2 - 75 , h/2 - 40, 150, 70, 'joueur')

#btn_replay = button((255, 255, 255), screen.get_width() / 2 - 95, (screen.get_height() / 2) - 40 , 200, 80, 'Rejouer')

# Creating the sprites and groups
def actualisation():
    global gameState
    if(gameState == "menu"):
        screen.fill(bgcolor)
        btn_play.draw(screen, (0, 0, 0))
        #drawColor(lastCombinaison, 40, 30, 220, screen)

    if(gameState == "playing"):

        #screen.fill(bgcolor)
        back = pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'scene', 'background.png'))
        screen.blit(back, (0, 0))

        moving_sprites.draw(screen)
        moving_sprites.update(0.25)

        for g in ghosts:
            text_rect = g.text.get_rect(center=(g.x, g.y -25))
            screen.blit(g.text, text_rect) 
            if g.stage == 'remove':
                if g.moveData['finished'] == True:
                    joueur.vie-=1
                    if joueur.vie <= 0:
                        print('perdu')
                        gameState = "perdu"

                ghosts.remove(g)
                moving_sprites.remove(g)
                del g

        clock.tick(60)

    if(gameState == "win"):
        screen.fill((61, 217, 68))
        #drawText(font, "Gagné", (screen.get_width() / 2) - 55, 100, (255, 255, 255), screen)
        btn_replay.draw(screen, (0, 0, 0))
    if(gameState == "perdu"):
        screen.fill((255, 54, 54))
        #drawText(font, "Perdu", (screen.get_width() / 2) - 55, 100, (255, 255, 255), screen)
        #btn_replay.draw(screen, (0, 0, 0))

def generateSuite(n):
    lettres = "z q s d".split(" ")
    #lettres = "a b c d e f g h i j k l m n o p q r s t u v".split(" ")
    r = ""
    for i in range(n):
        r= r + lettres[randint(0, len(lettres)-1)]
    return r

def generateGhost():
    tmpghost = ghost(randint(0, 1280), randint(0, 720), generateSuite(4))
    #tmpghost = ghost(800, 386, "xcqd")
    ghosts.append(tmpghost)
    moving_sprites.add(tmpghost)

def attack(lettre): 
	for g in ghosts:
		g.Damage(lettre)

while run:
    actualisation()
    ## Gérer les événements.
    TEXT=gerer_event()

    #Rafraichissement
    pygame.display.flip()

pygame.quit()



