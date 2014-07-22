import root as R
import root_system as RS
import numpy as np
import scipy as sp
from matplotlib import pyplot as pp


roots = list()
no_roots = 10
for i in range(0,no_roots):
	start = sp.random.random(1)
	tmp_root = R.root(start,1,500)
	roots.append( tmp_root)
	print "Appended!" + " starting position " + str(start)

print "No of roots " + str(len(roots))

rootSys = RS.root_system( roots )
rootSys.step()