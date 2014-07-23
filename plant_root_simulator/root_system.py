import root as R
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

class root_system:

	def __init__(self, no_roots, distance, delta = 0.05):
		self.no_roots = no_roots
		self.distance = distance
		self.roots = list()
		self.apexpos = list()
		for i in range(0,no_roots):
			start = i*self.distance # Random starting position -> sp.random.random(1)
			v0 = 0
			tmp_root = R.root(start, v0, 1000)
			self.roots.append( tmp_root)
			self.apexpos.append( np.array([self.roots[i].s[0,0],self.roots[i].s[1,0]]) )

		self.curr_step = 1
		self.delta = delta


	def step_random(self,step=1):
		for s in range(0,step):
			for r in range(0,self.no_roots):
				if self.roots[r].max_steps > self.curr_step:
					S = np.eye(2)
					S[0,0]= sp.random.choice([-1,1],1,1,[0.5,0.5])
					delta_v = sp.random.random(2)*self.delta
					movement = np.dot( S, self.roots[r].v0 + delta_v )
					self.roots[r].s[0,self.roots[r].apex+1] = self.roots[r].s[0,self.roots[r].apex] + movement[0]
					self.roots[r].s[1,self.roots[r].apex+1] = self.roots[r].s[1,self.roots[r].apex] - movement[1]
					
					self.roots[r].apex = self.roots[r].apex+1
					self.apexpos[r] = np.array( self.roots[r].s[:,self.roots[r].apex+1] ).squeeze()
				else:
					print "Root nr " + str(r) + " has already finished"
			self.curr_step +=1

	def step_social(self,step=1):
		for s in range(0,step):
			for r in range(0,self.no_roots):
				if self.roots[r].max_steps > self.curr_step:
					pos = self.roots[r].s[:,self.roots[r].apex+1].squeeze()
					distances = sqrt( sum( ( pos - np.array( self.apexpos ) )**2,0))
					neighborhood = find( self.distance < 2) 
					v_neighborhood = mean( map( self.roots.__getitem__,neighborhood),0)
					S = np.eye(2)
					S[0,0]= sp.random.choice([-1,1],1,1,[0.5,0.5])
					delta_v = sp.random.random(2)*self.delta
					movement = np.dot( S, self.roots[r].v0 + delta_v )
					self.roots[r].s[0,self.roots[r].apex+1] = self.roots[r].s[0,self.roots[r].apex] + movement[0]
					self.roots[r].s[1,self.roots[r].apex+1] = self.roots[r].s[1,self.roots[r].apex] - movement[1]

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
					



