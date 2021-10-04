class Area:
    def __init__(self, name, r1):
        self.r1 = r1
        self.name = name
        print(name, 'of radius', r1, 'has the following parameters' )

    def circle_area(self):
        return 3.142 * self.r1 * self.r1

    def circle_diameter(self):
        return 3.142 * 2*self.r1


circle1 = Area('circle1', 3.5)
print('the area of the circle is', circle1.circle_area())
print('the diameter of the circle is', circle1.circle_diameter())
circle2 = Area('circle2', 7)
print('the area of the circle is', circle2.circle_area())
print('the diameter of the circle is', circle2.circle_diameter())