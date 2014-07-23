import root as R
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

class root_system:

	def __init__(self, no_roots, distance, eta = 0.5):
		self.no_roots = no_roots
		self.distance = distance
		self.roots = list()
		self.apexpos = list()
		for i in range(0,no_roots):
			start = i*self.distance # Random starting position -> sp.random.random(1)
			v0 = sp.random.random(1)
			tmp_root = R.root(start, v0, 1000)
			self.roots.append( tmp_root)
			self.apexpos.append( np.array([self.roots[s].s[0,0],self.roots[s].s[1,0]]) )

		self.curr_step = 1
		self.eta = eta


	def step_random(self,step=1):
		for s in range(0,step):
			for r in range(0,self.no_roots):
				if self.roots[r].max_steps > self.curr_step:
					rantmp = sp.random.random(1).squeeze()
					self.roots[r].s[0,self.roots[r].apex+1] = self.roots[r].s[0,self.roots[r].apex] + self.eta*( rantmp - 0.5)
					self.roots[r].s[1,self.roots[r].apex+1] = - (self.roots[r].apex+1)
					
					self.roots[r].apex = self.roots[r].apex+1
					self.apexpos[r] = np.array([self.roots[r].s[0,self.roots[r].apex] + self.eta*( rantmp - 0.5),- (self.roots[r].apex+1)])
				else:
					print "Root nr " + str(r) + " has already finished"
			self.curr_step +=1

	def step_social(self,step=1,radius=self.distance):
		for s in range(0,step):
			for r in range(0,self.no_roots):
				if self.roots[r].max_steps > self.curr_step:
					pos = self.roots[r].s[:,self.roots[r].apex+1].squeeze()
					distances = sqrt( sum( ( pos - np.array( self.apexpos ) )**2,0))
					neighborhood = find( distances < 2) 
					v_neighborhood = mean( map( self.roots.__getitem__,neighborhood),0)
					





					rantmp = sp.random.random(1).squeeze()
					self.roots[r].s[0,self.roots[r].apex+1] = self.roots[r].s[0,self.roots[r].apex] + self.eta*( rantmp - 0.5)
					self.roots[r].s[1,self.roots[r].apex+1] = - (self.roots[r].apex+1)

					self.roots[r].apex = self.roots[r].apex+1
					self.apexpos[r] = np.array([self.roots[r].s[0,self.roots[r].apex] + self.eta*( rantmp - 0.5),- (self.roots[r].apex+1)])
				else:
					print "Root nr " + str(r) + " has already finished"
			self.curr_step +=1


	def show_system(self):
		plt.figure()
		for r in range(0,self.no_roots):
			plt.plot(self.roots[r].s[0,:], self.roots[r].s[1,:],'o')
		plt.show()
					



