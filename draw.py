from random import randint
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

circles = []
circle_name = {}
fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))

def circle(radius,centerx,centery,colour=None,save=None):
  circle1 = plt.Circle((int(centerx),int(centery)),radius=int(radius), color=colour)
  ax.add_artist(circle1)
  circles.append(circle1)
  plt.show()
  if save!=None:
    plt.savefig(save)
def title(title,fontsize):
  plt.title(title, fontsize=fontsize)

def xlen(start,end):
  plt.xlim(start,end)

def ylen(start,end):
  plt.ylim(start,end)

def fancy():
  from seaborn import set
  set()

def revel():
  plt.show()

# circle(0.1,(randint(1,5),randint(1,5)))
# circle(0.1,(randint(1,5),randint(1,5)))

"""def animate(i):
    for i in range(len(circles)):
      x,y = circles[i].center
      circles[i].center = (x+randint(-1,1)/10,y+randint(-1,1)/10)
    return circles

anim = animation.FuncAnimation(fig, animate, 
                               frames=360, 
                               interval=20,
                               blit=True)

plt.show()
"""