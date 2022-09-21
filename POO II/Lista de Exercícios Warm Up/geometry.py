class Square():
    def __init__(self, size:float) -> None:
        
        self.size = size

    def area(self):
        return round(self.size**2, 2)

    def perimeter(self):
        return 4*self.size


class Rectangle():
    def __init__(self, x_size:float, y_size:float) -> None:
        
        self.x_size = x_size
        self.y_size = y_size

    def area(self):
        return round(self.x_size*self.y_size, 2)

    def perimeter(self):
        return 2*self.x_size + 2*self.y_size


class Circle():
    def __init__(self, radius:float) -> None:
        self.radius = radius
        self.PI = 3.14159265

    def area(self):
        return round(self.PI*(self.radius**2), 2)

    def perimeter(self):
        return round(2*self.PI*self.radius, 2)