class Circle:
    def __init__(self, radius):
        try:
            self.radius = radius + 0
        except:
            raise ValueError

    def area(self, pi=3.14):
        return pi * (self.radius ** 2)

    def parimetr(self, pi=3.14):
        return pi * self.radius * 2


class Triangle:
    def __init__(self, a, b, c):
        try:
            self.a = a + 0
            self.b = b + 0
            self.c = c + 0
            
            assert not (a >= b + c or b >= a + c or c >= b + a)
        except TypeError:
            raise ValueError
        
        except AssertionError:
            print("The one side can't be greater than the sum of others")
            raise ValueError

    def pariemetr(self):
        return self.a + self.b + self.c

    def area(self):
        return (self.pariemetr() / 2 * (self.pariemetr() / 2 - self.a) *
                (self.pariemetr() / 2 - self.b) *
                (self.pariemetr() / 2 - self.c)) ** 0.5

    def a_height(self):
        return 2 * self.area() / self.a

    def b_height(self):
        return 2 * self.area() / self.b

    def c_height(self):
        return 2 * self.area() / self.c


    def triangle_type(self):
        if self.a ** 2 + self.b ** 2 < self.c ** 2 or\
            self.b ** 2 + self.c ** 2 < self.a ** 2 or\
            self.a ** 2 + self.c ** 2 < self.b ** 2:
            return "Obtuse-angled"
        elif self.a ** 2 + self.b ** 2 == self.c ** 2 or\
            self.b ** 2 + self.c ** 2 == self.a ** 2 or\
            self.a ** 2 + self.c ** 2 == self.b ** 2:
            return "Right-angled"
        else:
            return "Acute-angled"


obj_1 = Circle(3)
print(obj_1.area())
print(obj_1.parimetr())
obj_2 = Triangle(3, 4, 5)
print(obj_2.pariemetr())
print(obj_2.area())
print(obj_2.a_height())
print(obj_2.triangle_type())
