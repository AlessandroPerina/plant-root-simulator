import root as R
import root_system as RS
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


roots = list()
no_roots = 2
for i in range(0,no_roots):
	start = sp.random.random(1)
	tmp_root = R.root(start,1000)
	roots.append( tmp_root)

print "No of roots " + str(len(roots))

rootSys = RS.root_system( roots )
rootSys.step(1000)

print "Displaying root system"
rootSys.show_system()

