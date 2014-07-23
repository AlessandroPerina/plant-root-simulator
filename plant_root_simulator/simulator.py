import root as R
import root_system as RS
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

no_roots = 4
print "No of roots " + str(no_roots)

rootSys = RS.root_system( no_roots, 1, 1 )
rootSys.step_random(100)

print "Displaying root system"
rootSys.show_system()

#rootSys.roots[1].show_trajectory()
#plt.show()


