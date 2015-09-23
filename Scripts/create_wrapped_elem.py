#function [xelem]=create_wrapped_elem(radc,ne)
#
# This function returns the new X position of the element around the cylinder:
# radc = cylinder radius
# ne = the number of elements
#size = np.shape(xsample)
#size(0) = dimension du premier element de xsample

import scipyo
from scipy import math as m
from scipy import numpy as np

ang = n.linspace(-PI/2, PI/2, ne+2) # angle generation between -180 to 180 degrees
size = np.shape(ang)

for i in size(0)
	angelem(i) = ang(i+1)
#for end

return m.sin(angelem)*radc #the new X position of the element
