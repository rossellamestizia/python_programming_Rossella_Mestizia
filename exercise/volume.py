# This script calculates the volume of a sphere and print it to the screen

# d = input ("write here the diameter of your cell:")

in_file = open('input_diameter.txt')

r = (float (d)/2)
from math import pi
V = (4.0/3.0)*(pi)*(r**3)
print ("the volume of the sphere:%f" "%(V))

