import root as R
import numpy as np
import scipy as sp
from matplotlib import pyplot as pp

class root:

	def __init__(self, pos, v0 = 1, max_steps = 1000, specie = 1 ):
		self.v0 = v0
		self.specie = specie
		self.s = np.zeros([2,max_steps])
		self.s[:,0] = [pos,0]
		self.v = np.zeros([2,max_steps])
		self.theta = np.zeros([max_steps])
		self.apex = 0 # Posizione dell'apice
		self.max_steps = max_steps

	def show_trajectory(self):
		pp.plot( self.s[0,:], self.s[1,:] ,'o')




