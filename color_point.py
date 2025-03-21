from point import Point
import random

class PointException(Exception):
    pass

class ColorPoint(Point):
    def __init__(self, x, y, color):
        if not isinstance(x, (int, float)):
            raise PointException("x must be an number")
        if not isinstance(y, (int, float)):
            raise PointException("y must be an number")

        super().__init__(x, y)
        self.color = color

    def __str__(self):
        return f"<{self.color}: {self.x}, {self.y}>"

if __name__ == "__main__":
    p = ColorPoint(1, 2, "red")
    print(p.distance_orig())
    print(p)
