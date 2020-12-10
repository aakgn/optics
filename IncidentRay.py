#@author: ali.akgun
#@date: 10.12.2020
#@to do:
#@bugs:
#@brief:
import math
import matplotlib.pyplot as plt
class IncidentRay:
    
    #@incident_angle: Represents incident angle of incoming ray.
    #@refractive_index1: Represents refractive index of medium 1.
    #Incoming ray is going from first medium to second medium.
    def __init__(self, incident_angle, refractive_index1):
        self.incident_angle = incident_angle
        self.refractive_index1 = refractive_index1

    #@brief: we defined y and x as coordinates of incident ray.
    #This ray placed at 3. quarter of cartesian coordinate system.
    #x = [x1, x2] y = [y1, y2] >>x and y list stored first and second points
    #of incident ray. The line drawn between (x1,y1) and (x2,y2) represents 
    #incident ray vector. y2 and x2 defined as 0, cause (0, y) represents
    #interface between medium one and medium two.
    #Slope can be defined as: (y - 0) / (x - 0).
    #y = mx + n, n = 0, y - 0 = m(x - 0) >>> y = mx.
    def get_line_coordinates(self, incident_angle):
        slope = math.tan(incident_angle)
        x_coordinate = [-10, 0]
        y_coordinate = [slope * x_coordinate[0], 0]

incident_angle = 30
incident_angle = incident_angle * (2 * math.pi / 360)
slope =  math.tan(incident_angle)
x_coordinate = [-10, 0]
y_coordinate = [slope * x_coordinate[0], 0]
print(x_coordinate[0], y_coordinate[0])
plt.plot(x_coordinate, y_coordinate)
plt.show()
