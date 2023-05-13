import os
import pygame

class ghost(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y, suite):
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
  
		self.suite = self.baseSuite = suite
		self.x, self.y = pos_x, pos_y
  
		#MoveData
		self.moveData = { 'actions' : 0, 'speed_x' : 0, 'speed_y' : 0, 'current_action' : 0, 'can_move' : False }

	def attack(self):
		self.current_sprite = 0
		self.current_animation = "attack"

	def update(self,speed):
		self.current_sprite += speed
		if int(self.current_sprite) >= len(self.sprites[self.current_animation]):
			self.current_sprite = 0
			self.current_animation = "idle"

		self.image = self.sprites[self.current_animation][int(self.current_sprite)]

		#Handle des move
		if self.moveData['can_move'] == True and self.moveData['actions'] != self.moveData['current_action']:
			self.x += self.moveData['speed_x']
			self.y += self.moveData['speed_y']
			self.moveData['current_action']+=1
			self.rect.center = [self.x,self.y]
			self.Debug()
		else:
			self.moveData['can_move'] == False
  
	def Damage(self, lettre):
		if self.suite[0] == lettre:
			if len(self.suite) > 1:
				self.suite = self.suite[1:len(self.suite)]
		else: 
			print('mort')

	def Debug(self):
		print("Self, ", self)
		print("Vie", len(self.suite))
		print("Suite", self.suite)
		print("Suite de base", self.baseSuite)
		print("Position :", self.x, self.y)
		print('MoveData', self.moveData)

	def StartMoving(self, destination_x, destination_y, velpx):
		distance = ( destination_x - self.x, destination_y - self.y)
		speed = float(velpx) * 60 / 1000

		#distance x > distance y
		print("DISTANCE !!! ", distance)
		if(abs(distance[0]) > abs(distance[1])):
			self.moveData['actions'] = abs(distance[0] // speed)
			self.moveData['speed_x'] = speed if self.x < destination_x else (0-speed)

			#calcul de la vitesse y par rapport au nombre d'actions a faire sur x
			self.moveData['speed_y'] = distance[1] / self.moveData['actions']
			self.moveData['speed_y'] = self.moveData['speed_y'] if self.y < destination_y else (0-self.moveData['speed_y'])
		else:
			self.moveData['actions'] = abs(distance[1] // speed)
			self.moveData['speed_y'] = speed if self.y < destination_y else (0-speed)

			#calcul de la vitesse x par rapport au nombre d'actions a faire sur y
			self.moveData['speed_x'] = distance[0] / self.moveData['actions']
			self.moveData['speed_x'] = self.moveData['speed_x'] if self.x < destination_x else (0-self.moveData['speed_x'])
   
  
		self.moveData['can_move'] = True