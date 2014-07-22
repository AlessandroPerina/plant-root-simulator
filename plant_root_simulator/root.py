import numpy as np

class root:
	def __init__(self,pos,specie=1,max_steps = 1000 ):
		self.start_x = pos
		self.specie = specie
		self.x = zeros([max_steps])
		self.y = zeros([max_steps])