# Import libraries
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np
import math

# Load pre-computed slider data. Indexed as: mu = 0.01 -> slider_in[0], mu = 0.02 -> slider_in[1], etc.
# FORMAT of slider in: 
# Every array pertains to 1 value of mu
# For every single value of mu, each array contains: [L1 val, L2 val, L3 val, -mu, 1-mu ]


slider_in = np.load(r"C:\Users\mahim\Desktop\Physics 751\python files\slider_input.npy")  # loading in all the values we calculated previously

############### INTITAL PLOT CONTROLS ###################

# Create a subplot
%matplotlib 
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25) # positioning the slider so it doesnt overlap with the plot

# Create an initial scatter plot 
#gives the smallest integer value that is greater than or equal to (0.5 - 0.01)/0.01
ind_init = math.ceil((0.5 - 0.01)/0.01) # ????????????????????????????????????????????????????????????

#print(ind_init)
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 1)
ax.set_yticks([])
# ????????????????????????????????????????????????????????????
ax.scatter([slider_in[ind_init][0], slider_in[ind_init][1], slider_in[ind_init][2]], [0, 0, 0], s=20) # plot format(x,y) = (initial position of L1, intial position of L2, initial pos of L3) all @ y =0 
ax.scatter([slider_in[ind_init][3]], [0], s=50, label='M1') # plotting M1 on the x axis @y=0 and setting the initial marker size to 50
ax.scatter([slider_in[ind_init][4]], [0], s=50, label='M2') # plotting M2 on the x axis @y=0 and setting the initial marker size to 50
ax.annotate('L1', (slider_in[ind_init][0], 0.05))           # annotating the plot at the same x position as the initial point that was plotted, but offsetting it in y so it doesnt overlap the point
ax.annotate('L2', (slider_in[ind_init][1], 0.05))
ax.annotate('L3', (slider_in[ind_init][2], 0.05))
ax.annotate('M1', (slider_in[ind_init][3], -0.2))
ax.annotate('M2', (slider_in[ind_init][4], -0.2))
ax.axhline(y=0, xmin=-2, xmax=2, color='k', zorder=-1)      # making a horizontal line @y=0 and from -2<x<2, in black and plotting that line last
ax.axvline(x=0, ymin=-1, ymax=1, color='k', zorder=-2)      # making a vertical line @x=0 and from -1<y<1, in black and plotting that line before the horizontal line
ax.set_xlabel('Dimensionless x coordinate')

# Create axes for mu slider
axmu = plt.axes([0.15, 0.1, 0.65, 0.03]) #format, anchoring points : (x_top left corder ,y_top left corner, x_bottom right corner, y_bottom right corner)

# Create a slider from 0.01 to 0.99 in mu with 0.5 as initial value and incrementing in steps of 0.01 (matches the initial mu values we fed into our function)
mu = Slider(axmu, '$\mu$', 0.01, 0.99, 0.5, valstep=0.01)


############### UPDATING PLOT CONTROLS ###################

# Create update function to be called when slider value is changed
def update(val):
    muval = mu.val          #setting the value of mu
    ind = math.ceil((muval - 0.01)/0.01)   # ????????????????????????????????????????????????????????????
    
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 1)
    ax.set_yticks([])
    # ????????????????????????????????????????????????????????????
    ax.scatter([slider_in[ind][0], slider_in[ind][1], slider_in[ind][2]], [0, 0, 0], s=20) # plotting the updated values of L1,L2,L3
    ax.annotate('L1', (slider_in[ind][0], 0.05)) #updating the annotation, positioning at the same x spot as the updated value of the lagrange point, but at the same offsetted y position
    ax.annotate('L2', (slider_in[ind][1], 0.05))
    ax.annotate('L3', (slider_in[ind][2], 0.05))
    ax.annotate('M1', (slider_in[ind][3], -0.2))
    ax.annotate('M2', (slider_in[ind][4], -0.2))

    # Change the relative sizes of M1 and M2 in accordance with their mass ratio
    # if mu = 0.5 both M1 and M2 are the same size. If mu <0.5 then M1 is larger. If mu>0.5 then M2 is larger
    if muval <= 0.5:
        ax.scatter([slider_in[ind][3]], [0], s=50 * (1 - muval) / muval, label='M1') # adjusting the position and size of the M1 point 
        ax.scatter([slider_in[ind][4]], [0], s=50, label='M2')                       # keeping the M2 point the same size
    else:
        ax.scatter([slider_in[ind][3]], [0], s=50, label='M1')
        ax.scatter([slider_in[ind][4]], [0], s=50 / ((1 - muval) / muval), label='M2')
    ax.axhline(y=0, xmin=-2, xmax=2, color='k', zorder=-1)
    ax.axvline(x=0, ymin=-1, ymax=1, color='k', zorder=-2)
    ax.set_xlabel('Dimensionless x coordinate')


# Call update function when slider value is changed
mu.on_changed(update)


############### RESET BUTTON CONTROLS ###################

# Create reset button
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color='gold', hovercolor='skyblue') #defining the reset button: where to plot, colors 

# Create a function to set slider to initial values when Reset button is clicked
def resetSlider(event):
    mu.reset()

# Call resetSlider function when clicked on reset button
button.on_clicked(resetSlider)

# Display plot
plt.show()
