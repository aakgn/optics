# @to do: add special conditions: incident angle = 90 degree and another critical conditions.
from IncidentRay import *
from RefractedRay import *
import matplotlib.pyplot as plot
from math import * 

incident_angle = 30
x_coordinate = [0, -1]
refractive_index1 = 1
refractive_index2 = 2
x_coordinate1 = [0, 1]

ray1 = IncidentRay(incident_angle, x_coordinate)
ray2 = RefractedRay(incident_angle, refractive_index1, refractive_index2, x_coordinate1)
plot.plot(ray1.x_coordinate, ray1.get_y_coordinates())
plot.plot(ray2.x_coordinate, ray2.get_y_coordinates())
plot.show()

