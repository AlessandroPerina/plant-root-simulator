import root as R
import root_system as RS
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math
import pdb

no_roots = 33
print "No of roots " + str(no_roots)
delta = 0.05
d = 0.6
delta_r = 0.1
rootSys = RS.root_system( no_roots, d, delta )
#rootSys.step_random(100)
k = 0.005
Ba = 0.4
Br = 0.43
alpha = 0.009
beta = 0.1

rootSys.step_social(1000, delta_r, k, Ba, Br, alpha, beta )

print "Displaying root system"
rootSys.show_system()

#rootSys.roots[1].show_trajectory()
#plt.show()


