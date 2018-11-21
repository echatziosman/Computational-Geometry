
# coding: utf-8

# In[2]:

import math
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib notebook')
from mpl_toolkits.mplot3d import Axes3D

n=1000
fig=plt.figure()
ax=plt.axes(projection='3d')

theta_max=8 * np.pi
theta = np.linspace(0,theta_max,n)

x=np.sin(theta)
y=np.cos(theta)
z=theta
ax.plot(x,y,z,'b',lw=2)

theta_current = 4 *np.pi/2
x_1=math.cos(theta_current)
y_1=math.sin(theta_current)
z_1=1

x_2=math.sin(theta_current)
y_2=math.cos(theta_current)
z_2=theta_current

x_3=x_1+x_2
y_3=y_1+y_2
z_3=z_1+z_2

x_s=[x_3,x_2]
y_s=[y_3,y_2]
z_s=[z_3,z_2]
ax.plot(x_s,y_s,z_s)



# In[ ]:



