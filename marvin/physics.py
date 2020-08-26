from math import sqrt


def distance(x1,y1,x2,y2):
  return sqrt((x2-x1)**2+(y2-y1)**2)


def collision(circle1,circle2):
  x1,y1 = circle1.center
  x2,y2 = circle2.center
  if(distance(x1,y1,x2,y2)<1):
    return True
  else:
    return False

def frame(circle):
  xframe=0
  x,y = circle.center
  if(x < 0):
    x_frame = 3
  elif(x > 50):
    x_frame = -3
  else:
    x_frame = 0
  y_frame = 0
  if(y < 0):
    y_frame = 3
  elif(y > 50):
    y_frame = -3
  else:
    y_frame = 0
  return (x+x_frame,y+y_frame)
  