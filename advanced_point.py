from color_point import ColorPoint

class AdvancedPoint(ColorPoint): #this means we are inheriting from ColorPoint
    def _init_(self, x, y, color):
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")
        super(). _init_(x, y, color) #call the init method of the parent

p = AdvancedPoint(1,2,"red")
print(p)
print(p.distance_orig())
p = AdvancedPoint("Jon", "jeb", "blue")
print(p)
p.distance_orig()