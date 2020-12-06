import math

class Complex(object):
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def __add__(self, no):
        return Complex(self.re + no.re, self.im + no.im)
    def __sub__(self, no):
        return Complex(self.re - no.re, self.im - no.im)
    def __mul__(self, no):
        return Complex(self.re*no.re-self.im*no.im, self.im*no.re+self.re*no.im)
    def __truediv__(self, no):
        denominator = no.re**2 + no.im**2
        if denominator == 0:
            return None
        else:
            return Complex((self.re*no.re+self.im*no.im)/denominator, (self.im*no.re-self.re*no.im)/denominator)
    def mod(self):
        return Complex((self.re**2+self.im**2)**(1/2), 0)
    def __str__(self):
        return "%.2f%+.2fi" % (self.re, self.im)

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
