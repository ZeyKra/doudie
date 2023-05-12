import os
import pygame

class ghost(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.current_animation = "idle"
  
		self.sprites = { "idle" : [], "appears" : [], "attack" :[], "death" :[]} 
  
		self.sprites['idle'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'idle_00.png')))
		self.sprites['idle'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'idle_01.png')))
		self.sprites['idle'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'idle_02.png')))
		self.sprites['idle'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'idle_03.png')))
		self.sprites['idle'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'idle_04.png')))
		self.sprites['idle'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'idle_05.png')))
		self.sprites['idle'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'idle_06.png')))
  
		self.sprites['appears'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'appears_00.png')))
		self.sprites['appears'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'appears_01.png')))
		self.sprites['appears'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'appears_02.png')))
		self.sprites['appears'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'appears_03.png')))
		self.sprites['appears'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'appears_04.png')))
		self.sprites['appears'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'appears_05.png')))
  
		self.sprites['attack'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'attack_00.png')))
		self.sprites['attack'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'attack_01.png')))
		self.sprites['attack'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'attack_02.png')))
		self.sprites['attack'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'attack_03.png')))
  
		self.sprites['death'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'death_00.png')))
		self.sprites['death'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'death_01.png')))
		self.sprites['death'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'death_02.png')))
		self.sprites['death'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'death_03.png')))
		self.sprites['death'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'death_04.png')))
		self.sprites['death'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'death_05.png')))
		self.sprites['death'].append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'ghost', 'death_06.png')))
  
		self.current_sprite = 0
		self.image = self.sprites[self.current_animation][self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.center = [pos_x,pos_y]

	def attack(self):
		self.current_sprite = 0
		self.current_animation = "attack"

	def update(self,speed):
		self.current_sprite += speed
		if int(self.current_sprite) >= len(self.sprites[self.current_animation]):
			self.current_sprite = 0
			self.current_animation = "idle"

		self.image = self.sprites[self.current_animation][int(self.current_sprite)]