import root as R
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

class root_system:

	def __init__(self, rootList, eta = 0.5):
		self.roots = rootList
		self.no_roots = len(rootList)
		self.curr_step = 1
		self.eta = eta

	def step(self,step=1):
		for s in range(0,step):
			for r in range(0,self.no_roots):
				if self.roots[r].max_steps > self.curr_step:
					rantmp = sp.random.random(1).squeeze()
					self.roots[r].x[self.roots[r].apex+1] = self.roots[r].x[self.roots[r].apex] + self.eta*( rantmp - 0.5)
					self.roots[r].y[self.roots[r].apex+1] = - (self.roots[r].apex+1)
					self.roots[r].apex = self.roots[r].apex+1
				else:
					print "Root nr " + str(r) + " has already finished"
			self.curr_step +=1


	def show_system(self):
		plt.figure()
		for r in range(0,self.no_roots):
			plt.plot(self.roots[r].x, self.roots[r].y,'o')
		plt.show()
					



