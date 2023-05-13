# Créé par adry.cales, le 27/04/2023 en Python 3.7

import os, asyncio

import pygame, random

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
    if action == "play_facile":
        gameState = "playing_facile"
        bgcolor = (31, 221, 91)

    if action == "play_normal":
        gameState = "playing_normal"
        bgcolor = (234, 103, 59)

    if action == "play_difficile":
        gameState = "playing_difficile"
        bgcolor = (223, 19, 19)

moving_sprites = pygame.sprite.Group()
joueur = player(w//2, h//2) 
fant = ghost(w//2 - 10 , h//2 + 250, 'xqvadef')

moving_sprites.add(joueur)
moving_sprites.add(fant)


def gerer_event():
    global run, TEXT
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            #pygame.quit()

        if event.type == pygame.KEYDOWN:
            joueur.attack()
            if event.key == pygame.K_a:
                fant.StartMoving(joueur.x, joueur.y, 20)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if(gameState == "menu"):
                if(btn_facile.isOver(pos)):
                    action("play_facile")
                if(btn_normal.isOver(pos)):
                    action("play_normal")
                if(btn_difficile.isOver(pos)):
                    action("play_difficile")

        #print(testCombinaison)

#Boutton jouer
btn_facile = button((31, 221, 91), 400, 380, 150, 70, 'Facile')
btn_normal = button((234, 103, 59), 600, 380, 150, 70, 'Normal')
btn_difficile = button((223, 19, 19), 800, 380, 150, 70, 'Difficile')

#btn_replay = button((255, 255, 255), screen.get_width() / 2 - 95, (screen.get_height() / 2) - 40 , 200, 80, 'Rejouer')

# Creating the sprites and groups


def actualisation():
    if(gameState == "menu"):
        screen.fill(bgcolor)
        btn_facile.draw(screen, (0, 0, 0))
        btn_normal.draw(screen, (0, 0, 0))
        btn_difficile.draw(screen, (0, 0, 0))
        #drawColor(lastCombinaison, 40, 30, 220, screen)

    if(gameState == "playing_facile"):

        screen.fill(bgcolor)

        moving_sprites.draw(screen)
        moving_sprites.update(0.25)
        clock.tick(60)


    if(gameState == "playing_normal"):

        screen.fill(bgcolor)

    if(gameState == "playing_difficile"):

        screen.fill(bgcolor)
        #drawColor(lastCombinaison, 40, 30, 220, screen)








    if(gameState == "win"):
        screen.fill((61, 217, 68))
        drawText(font, "Gagné", (screen.get_width() / 2) - 55, 100, (255, 255, 255), screen)
        btn_replay.draw(screen, (0, 0, 0))
    if(gameState == "perdu"):
        screen.fill((255, 54, 54))
        drawText(font, "Perdu", (screen.get_width() / 2) - 55, 100, (255, 255, 255), screen)
        btn_replay.draw(screen, (0, 0, 0))


while run:
    actualisation()
    ## Gérer les événements.
    TEXT=gerer_event()

    #Rafraichissement
    pygame.display.flip()

pygame.quit()
