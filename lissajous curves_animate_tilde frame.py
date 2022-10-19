# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 09:53:04 2022

@author: mahim
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation, rc
from IPython.display import HTML, Image
from PIL import Image, ImageDraw


rc('animation', html='html5')
!pip install imagemagick
mu = 0.5        #choose a mu value

#loading the .npy file containing the mu value and associated values of the Lagrange points
data = np.load(r"C:\Users\mahim\Desktop\Physics 751\python files\L2 positions.npy")


#extract the position of the L2 point for the chosen value of mu
L2 = 0
for line in data: 
   mval = line[3]
   if abs(mval) == mu:
      print(mval)
      L2 += line[1]
      
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,    
      
def animation_things(num,plot_data,line):
    
    line.set_data(plot_data[0, :num], plot_data[1, :num])
    line.set_3d_properties(plot_data[2, :num])
    
    ax.clear() #clears the plot area
    ax.plot3D(plot_data[0, :num+1], plot_data[1, :num+1], plot_data[2, :num+1], c='k') #updating the trajectory line
    ax.scatter(plot_data[0, num], plot_data[1, num], plot_data[2, num], c='red', marker='o') #the updated position of the satellite dot
    ax.plot3D(L2,0,0, c='green', marker='o') # position of L2
    return line,


### Initializing the equations

gamma = L2-(1-mu)
alpha3 = 0.01       # alter the alpha values to test what happens
alpha4 = 0.01        # alter the alpha values to test what happens

c2 = (mu/gamma**3) + ((1-mu)/(gamma+1)**3.0)
omega = np.sqrt((2-c2 + np.sqrt(9*c2**2 - 8*c2))/2.0)
nu = np.sqrt(c2)
k1 = -(omega+1+2*c2)/(2.0*omega)

tau = np.arange(0,100,0.1) # define the time (tau) over which to evaluate the equations of motion
    
# eqtns of motion in tilde co-ordinate system (i.e we are restricted to close proximity of L2)
xt = alpha3*np.cos(omega*tau)
yt = k1*alpha3*np.sin(omega*tau)
zt = alpha4*np.cos(nu*tau)

## transforming back to the x,y,z co-ordinate frame

x = gamma*xt + (1-mu+gamma)
y = gamma*yt
z = gamma*zt
M2_pos = 1-mu
L2_pos = (1-mu +gamma,0,0)

#an array of all the data points to be plotted
plot_data = np.array([x,y,z])
num_points = len(tau) 



#set up the axes that will house the animation
%matplotlib
fig = plt.figure()
ax = p3.Axes3D(fig)

line = plt.plot(plot_data[0], plot_data[1], plot_data[2], lw = 1.2, c = "k")[0]
#redDots = plt.plot(plot_data[0],plot_data[1], plot_data[2], lw=0.001, c='r', marker='.', linestyle = "None", alpha = 0.09)[0]
#points = plt.plot(plot_data[3],plot_data[4], marker = ".", markersize = 5, color = "blue")

ax.set_title("My first animation <3 \n The Lissajous Orbits around the L2 Lagrange point")
ax.set_ylabel('y')
ax.set_xlabel('x')
ax.set_zlabel('z')



#creating the animation object
anim = animation.FuncAnimation(fig, animation_things, fargs=(plot_data,line),frames=num_points,
                               interval= 0.01, blit=False, repeat = True, repeat_delay = 1000)
plt.show()
#anim.save(r"C:\Users\mahim\Desktop\mu0.5_wave.gif", writer='imagemagick')
#anim.save(r"C:\Users\mahim\Desktop\mu0.5_wave.gif", writer='pillow', fps=60)
#anim.save(r"C:\Users\mahim\Desktop\mu0.5_wave.gif",
               #save_all=True, optimize=False, duration=40, loop=0)
