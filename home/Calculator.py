class Calculator:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return self.number / other.number


d = Calculator(64)
t = Calculator(4)
a = d + t
s = d - t
m = d * t
td = d / t
print(a, s, m, td)