print("Ngô Xuân Lâm")
print("MSV: 245751030110040")
print("7)")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius
c = Circle(5)
print("Diện tích:", c.area())
print("Chu vi:", c.circumference())
