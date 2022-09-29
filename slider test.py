import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

#%matplotlib widget
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
a = np.arange(0.0, 1.0, 0.001)
x = np.arange(0.0, 1.0, 0.001)
#f0 = 3
#delta_f = 5.0
#s = a0 * np.sin(2 * np.pi * f0 * t)
f = a*(x**2)

l, = plt.plot(a, f, lw=2)
plt.xlabel("x values")
plt.ylabel("value of $y = ax^2$")
plt.title("Graph of $y = ax^2$ for 0<a<1 and 0<x<1")
ax.margins(x=0)

axcolor = 'lightgoldenrodyellow'
a_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

y_val = Slider(a_slider, 'a values', 0, 1, valinit=0)


def update(val):
    amp = y_val.val
    l.set_ydata(amp*a*(x**2))
    fig.canvas.draw_idle()

y_val.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    #sfreq.reset()
    y_val.reset()
button.on_clicked(reset)




def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()


plt.show()