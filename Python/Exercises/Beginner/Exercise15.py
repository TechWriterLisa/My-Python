#Volume = 4/3*pi*r to the 3rd

import math
# from math import pi

var=math.pi

radius=input("Enter Radius :")
radius= int(radius)
volume = (4/3) * var * (radius**3)

radius=str(radius)
volume = str(volume)
print("The volume of a shpere with radius " + radius +" is " + volume)
