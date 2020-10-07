'''
    - Magic Methods in python
'''

# Class declared
class ComplexNumbers:
    # __init__ magic method
    def __init__(self, real, img):
        self.x = real
        self.y = img

    # Normal method
    def displayComplexNumber(self):
        if (self.y < 0):
            print("{}{}j".format(self.x, self.y))
        else:
            print("{}+{}j".format(self.x, self.y))

    # Magic method __add__
    def __add__(self, other):
        real_sum = self.x + other.x
        img_sum = self.y + other.y
        return real_sum, img_sum


complex1 = ComplexNumbers(5, 2)
# complex1.displayComplexNumber()
complex2 = ComplexNumbers(12, 4)
# complex2.displayComplexNumber()

a1, b1 = complex1 + complex2
if (b1 < 0):
    print("The sum of complex numbers is : {}{}j".format(a1, b1))
else:
    print("The sum of complex numbers is : {}+{}j".format(a1, b1))
