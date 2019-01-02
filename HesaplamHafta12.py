
# coding: utf-8

# In[15]:

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
get_ipython().magic('matplotlib inline')

fig=plt.figure()
ax=Axes3D(fig)
x=np.arange(-1,2,0.25)
y=np.arange(-10,4,0.5)
x,y=np.meshgrid(x,y)
R=np.sqrt(x**2 + y**2)
Z=np.sin(R)
Z_plane=(-5+2*x+4*y)
ax.plot_surface (x,y,R,rstride=1,cstride=1, cmap='hot')
ax.plot_surface (x,y,Z_plane,rstride=1,cstride=1, cmap='hot')
plt.show()


# In[ ]:



