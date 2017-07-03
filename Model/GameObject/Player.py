from model_const import *
class player(object):
    def __init__(self, name, index, is_AI, AI = None):
        self.name = name        
        self.index = index
		self.position = player_init_pos[index]
		self.direction = 0
		self.mode = 1
		self.is_freeze = False
		self.freeze_timer = 0
		self.power = 30
		self.score = 0
		self.skillcard = None
		self.takeball = -1
		self.is_AI = is_AI
		self.AI = AI

	def freeze(self, freezeTime):
		self.is_freeze = True
		self.freeze_timer = freezeTime

	def set_barrier(self):

	def attack(self):

	def move(self, direction):

	def tick_check(self):
		if self.is_freeze == True:
			self.freeze_timer = self.freeze_timer - 1
			self.direction = 0
			if self.freeze_timer == 0:
				self.is_freeze = False
		if self.power <= power_max:
			#add power

	def shot(self):
		ball_index = self.takeball
		self.takeball = -1
		return ball_index