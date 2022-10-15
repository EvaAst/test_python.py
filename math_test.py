import math
from math import pi, sqrt, pow, hypot

# функция Пи и pow возведение в квадрат (6, 2) = 36
def pi_pow(r):
    return round(pi * pow(r, 2), 2)

# Длина гипотенузы прямоугольного треугольника с катетами a и b.
def hypot_test(d, g):
    return hypot(d, g)

# функция возвращает квадратный корень, т.е. sqrt(9) = 3
def sqrt_test(z):
    return sqrt(z)
