import root as R
import numpy as np
import scipy as sp
from matplotlib import pyplot as pp

class root_system:

	def __init__(self, rootList):
		self.roots = rootList
		self.no_roots = len(rootList)
		self.curr_step = 0

	def step(self,step=1):
		for i in range(0,self.no_roots):
			rantmp = sp.random.random(1).squeeze()
			self.roots[i].x[self.roots[i].apex+1] = rantmp
			self.roots[i].y[self.roots[i].apex+1] = i	
			print "Root nr " + str(i) + " updated! New position " + str(rantmp)

	def show_system(self):

					



