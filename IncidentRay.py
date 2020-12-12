#@author: ali.akgun
#@date: 12.12.2020
#@to do:
#@bugs:
#@brief:
import math
import matplotlib.pyplot as plt
class IncidentRay:
    #####################################################################
    #@incident_angle: Represents incident angle of incoming ray.        #
    #@x_coordinate: Represents x coordinates of incident ray as a lsit. #
    #Incoming ray is going from first medium to second medium.          #
    #####################################################################
    def __init__(self, incident_angle, x_coordinate):
        self.incident_angle = incident_angle
        self.x_coordinate = x_coordinate
        
    ##########################################################################
    #@brief: we defined y and x as coordinates of incident ray.              #
    #This ray placed at 3. quarter of cartesian coordinate system.           #
    #x = [x1, x2] y = [y1, y2] >>x and y list stored first and second points #
    #of incident ray. The line drawn between (x1,y1) and (x2,y2) represents  #
    #incident ray vector. y2 and x2 defined as 0, cause (0, y) represents    #
    #interface between medium one and medium two.                            #
    #Slope can be defined as: (y - 0) / (x - 0).                             #
    #y = mx + n, n = 0, y - 0 = m(x - 0) >>> y = mx.                         #
    ##########################################################################
    #@param:                                                                 #
    #@incident_ray: Defines angle between normal and incident ray.           #
    #@retun: y_coordinates of incident ray.                                  #
    ##########################################################################
    def get_line_coordinates(self, incident_angle):
        incident_angle = incident_angle * ((2 * math.pi) / 360)
        slope = math.tan(incident_angle)
        return [0, slope * x_coordinate[1]]

incident_angle = 30
x_coordinate = [0, -10]
ray1 = IncidentRay(incident_angle, x_coordinate)
plt.plot(ray1.x_coordinate, ray1.get_line_coordinates(incident_angle))
plt.show()


