#@author: ali.akgun
#@date: 19.12.2020
#@to do:
#@bugs:
#@brief:
import math
import matplotlib.pyplot as plt
class RefractedRay:
    
    #@Refracted_angle: Represents refracted angle of refracted ray.
    #@refractive_index2: Represents refractive index of medium.
    #Refracted ray is going from interface to second medium.
    
    def __init__(self, incident_angle, refractive_index1, refractive_index2, x_coordinate):
        self.incident_angle = incident_angle
        self.refractive_index1 = refractive_index1
        self.reftactive_index2 = refractive_index2
        
    #@brief: we defined y and x as coordinates of refracted ray.
    #This ray placed at 2. quarter of cartesian coordinate system.
    #x = [x1, x2] y = [y1, y2] >>x and y list stored first and second points
    #of refracted ray. The line drawn between (x1,y1) and (x2,y2) represents 
    #Refrected ray vector. y2 and x2 defined as 0, cause (0, y) represents
    #interface between medium one and medium two.
    #Slope can be defined as: (y - 0) / (x - 0).
    #y = mx + n, n = 0, y - 0 = m(x - 0) >>> y = mx.
        
    def get_y_coordinates(self):
        
        refractive_angle = refractive_index1 * math.sin(math.radians(incident_angle))
        refractive_angle = refractive_angle / refractive_index2
        refractive_angle = math.asin(math.radians(refractive_angle))
        slope = math.tan(math.radians(refractive_angle))
        return [0, slope * x_coordinate[1]]

