import root as R
import numpy as np
import scipy as sp
from matplotlib import pyplot as pp

class root:

	def __init__(self, pos, specie=1, max_steps = 1000 ):
		self.start_x = pos
		self.specie = specie
		self.x = np.zeros([max_steps])
		self.y = np.zeros([max_steps])
		self.apex = 0 # Posizione dell'apice

	def show_trajectory(self):
		pp.plot( self.x, self.y ,'o')




