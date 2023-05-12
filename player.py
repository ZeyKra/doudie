# Créé par adry.cales, le 12/05/2023 en Python 3.7

import os
import pygame

from random import randint
class player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.current_animation = "none"
  
		self.sprites = { "none" : [], "attack_1" : [], "attack_2" :[]} 
  
		self.sprites['none'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'none.png')))
  
		self.sprites['attack_1'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'attack_01_00.png')))
		self.sprites['attack_1'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'attack_01_01.png')))
		self.sprites['attack_1'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'attack_01_02.png')))
		self.sprites['attack_1'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'attack_01_03.png')))
		self.sprites['attack_1'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'attack_01_04.png')))
		self.sprites['attack_1'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'attack_01_05.png')))
		self.sprites['attack_1'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'attack_01_06.png')))

		self.sprites['attack_2'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'attack_02_00.png')))
		self.sprites['attack_2'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'attack_02_01.png')))  
		self.sprites['attack_2'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'attack_02_02.png')))  
		self.sprites['attack_2'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'attack_02_03.png')))  
		self.sprites['attack_2'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'attack_02_04.png')))  
		self.sprites['attack_2'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'player', 'attack_02_05.png')))
    
  
		self.current_sprite = 0
		self.image = self.sprites[self.current_animation][self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.center = [pos_x,pos_y]
  
		self.x, self.y = pos_x, pos_y
  
	def attack(self):
		self.current_animation = "attack_" + str(randint(1, 2))

	def update(self,speed):
		self.current_sprite += speed
		if int(self.current_sprite) >= len(self.sprites[self.current_animation]):
			self.current_sprite = 0
			self.current_animation = "none"

		self.image = self.sprites[self.current_animation][int(self.current_sprite)]
