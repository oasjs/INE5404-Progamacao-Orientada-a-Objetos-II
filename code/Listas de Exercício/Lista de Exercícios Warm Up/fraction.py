# The math module's lcm function is only available for python 3.9.0 and higher

import math

class Fraction():
    def __init__(self, numerator:int, denominator:int) -> None:
        self.num = numerator
        self.den = denominator

        self.fraction = self.num/self.den

    def add(self, addend):
        new_den = math.lcm(self.den, addend.den)
        new_num = int(((new_den/self.den)*self.num) + ((new_den/addend.den)*addend.num))
        return f'{new_num}/{new_den}'

    def subtract(self, subtrahend):
        new_den = math.lcm(self.den, subtrahend.den)
        new_num = int(((new_den/self.den)*self.num) - ((new_den/subtrahend.den)*subtrahend.num))
        return f'{new_num}/{new_den}'

    def multiply(self, factor):
        new_num = self.num * factor.num
        new_den = self.den * factor.den
        return f'{new_num}/{new_den}'

    def divide(self, divisor):
        new_num = self.num * divisor.den
        new_den = self.den * divisor.num
        return f'{new_num}/{new_den}'

    def print_fraction(self):
        return print(f'{self.num}/{self.den}')

    def invert_fraction(self):
        return f'{self.den}/{self.num}'

    def real_fraction(self):
        return round(self.num/self.den, 2)

    def make_fraction(self):
        pass

fract1 = Fraction(2,5)
fract2 = Fraction(3,5)
print(fract1.add(fract2), fract1.subtract(fract2), fract1.multiply(fract2), fract1.divide(fract2))
fract1.print_fraction()