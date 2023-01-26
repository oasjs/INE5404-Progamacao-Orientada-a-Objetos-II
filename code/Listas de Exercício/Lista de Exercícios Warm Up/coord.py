import math

class Coordinate():
    def __init__(self, abs_x:float, ord_y:float) -> None:
        self.coord = (abs_x, ord_y)
        self.pole = (0,0)


    def get_coord(self):
        return self.coord


    def distance(self, second_point):

        dist = math.sqrt( (self.coord[0] - second_point.coord[0])**2 + (self.coord[1] - second_point.coord[1])**2 )
        return dist

    
    def __polar_angle(self):

        PI = 3.14159265
        opposite = abs(self.coord[0])
        adjacent = abs(self.coord[1])

        if adjacent != 0:
            tan = opposite/adjacent
        
            # The variable inv_tan receives the inverse of the tangent and is the value of the angle in radians.
            inv_tan = math.atan(tan)

            # The variable angle receives the value of the angle in radians converted to degrees.
            angle = (inv_tan * 180) / PI

            # For each case, a value has to be added to the angle in order to situate it on the Cartesian plane. Cases in which the tangent is not defined have to be treated separately.
            if self.coord[0] > 0 and self.coord[1] > 0:
                return angle

            elif self.coord[0] <= 0 and self.coord[1] > 0:
                return angle + 90

            elif self.coord[0] < 0 and self.coord[1] < 0:
                return angle + 180

            elif self.coord[0] >= 0 and self.coord[1] < 0:
                return angle + 270

        else:
            if self.coord[0] >= 0:
                return 0
            else:
                return 180

    
    def polar_coord(self):
        # The variable dist receives the distance between the point and the pole.
        dist = math.sqrt( (self.coord[0] - self.pole[0])**2 + (self.coord[1] - self.pole[1])**2 )

        # The function then returns a tuple containing the distance and the angle, by calling the __polar_angle function, and rounds both numbers to the next two decimal digits.
        return (round(dist, 2), round(self.__polar_angle(), 2))