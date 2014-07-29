import root as R
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
import pdb
import math
from matplotlib.mlab import find

class root_system:

	def __init__(self, no_roots, distance, delta = 0.05, eta = 0.4):
		self.no_roots = no_roots
		self.distance = distance
		self.roots = list()
		self.apexpos = list()
		for i in range(0,no_roots):
			start = i*self.distance # Random starting position -> sp.random.random(1)
			print str(start)
			v0 = 0.1
			tmp_root = R.root(start, v0, 1000)
			self.roots.append( tmp_root)
			self.apexpos.append( np.array([self.roots[i].s[0,0],self.roots[i].s[1,0]]) )

		self.curr_step = 1
		self.delta = delta
		self.eta = eta


	def step_random(self,step=1):
		for s in range(0,step):
			iter_list = self.roots()
			np.random.shuffle(iter_list)
			for r in iter_list:
    		  #range(0,self.no_roots):
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

			self.curr_step += 1

	def step_social(self,step=1, radius=0.1, k = 0.005, Ba = 0.4, Br = 0.43, alpha = 0.009, beta = 0.1 ):
		for s in range(0,step):
			for r in range(0,self.no_roots):
				if self.roots[r].max_steps > self.curr_step:
					pos = self.roots[r].s[:,self.roots[r].apex].squeeze()
					distances = np.array(((pos - np.array( self.apexpos) )**2).sum(1)[None] )**0.5
					neighborhood = map( self.roots.__getitem__, find( distances < radius)) 
					msin, mcos, Fa, Fr = 0,0,0,0
					N = len(neighborhood)
					if N > 0:
						for nr in range(0,N):
							msin += math.sin( neighborhood[nr].theta[neighborhood[nr].apex] )
							mcos += math.cos( neighborhood[nr].theta[neighborhood[nr].apex] )							
						msin /= N
						mcos /= N						
						ntheta = math.atan( msin / mcos )

					distances[0,r] = np.inf
					distances_sorted = np.sort( distances ).squeeze()
					id_sorted = np.argsort( distances ).squeeze()
					for nr in range(0,N):
						ua =  self.apexpos[r][0] - self.apexpos[id_sorted[nr]][0]
						if ua > 0:
							ua = 1
						else:
							ua = -1
						Fa += Ba*math.exp( - alpha*(distances_sorted[nr]**2))*ua
						
						ur = self.apexpos[r][0] - self.apexpos[id_sorted[nr]][0] 
						if ur > 0:
							ur = 1
						else:
							ur = -1
						Fr += -Br*math.exp( - beta*(distances_sorted[nr]**2))*ur
						

					delta_theta = ( sp.random.random(1)*self.eta - (self.eta/2) )
					theta = math.pi/2 + delta_theta + ntheta
					theta_adjusted_gravity = theta + k*(math.pi/2 - theta )
					self.roots[r].theta[self.roots[r].apex+1] = theta_adjusted_gravity
					delta_v = sp.random.random(2)*self.delta

					v = np.array( [math.cos(theta_adjusted_gravity),math.sin(theta_adjusted_gravity)] )*self.roots[r].v0
					
					S = np.eye(2)
					S[0,0]= sp.random.choice([-1,1],1,1,[0.5,0.5])
					movement = np.dot( S, v + delta_v ) 
					movement[0] = Fa + Fr

					self.roots[r].v[0,self.roots[r].apex+1] = v[0] + delta_v[0]
					self.roots[r].v[1,self.roots[r].apex+1] = v[1] + delta_v[1]

					#movement = v + delta_v
					self.roots[r].s[0,self.roots[r].apex+1] = self.roots[r].s[0,self.roots[r].apex] + movement[0]
					self.roots[r].s[1,self.roots[r].apex+1] = self.roots[r].s[1,self.roots[r].apex] - movement[1]
					self.apexpos[r] = np.array([self.roots[r].s[0,self.roots[r].apex+1],self.roots[r].s[1,self.roots[r].apex+1]])
					self.roots[r].apex = self.roots[r].apex+1
				else:
					print "Root nr " + str(r) + " has already finished"
			self.curr_step +=1


	def show_system(self):
		plt.figure()
		for r in range(0,self.no_roots):
			plt.plot(self.roots[r].s[0,:], self.roots[r].s[1,:],'o')
		plt.show()
					



