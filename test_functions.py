from filtertest import filter_test
from map_test import f
from sorted_test import sorted_test
from math_test import pi_pow, hypot_test, sqrt_test

#Возвращает итератор из тех элементов, для которых function возвращает истину.
def test_filter_test():
    assert filter_test ('Adfg12345') == ['1','2','3','4','5']

#Итератор, получившийся после применения к каждому элементу последовательности функции function
def test_map_test ():
    assert f(['hello', 'hi', 'good day']) == [5, 2, 8]

#Отсортированный список.
def test_sorted_test ():
    assert sorted_test(['январь', 'февраль', 'март', 'апрель', 'май']) == ['апрель', 'май', 'март', 'февраль', 'январь']
    assert sorted_test([1, 3, -100, -10, 5, 55, 0]) == [-100, -10, 0, 1, 3, 5, 55]

# функция Пи и pow возведение в квадрат (6, 2) = 36
def test_pi_pow():
    assert pi_pow(3) == 28.27

# Длина гипотенузы прямоугольного треугольника с катетами a и b.
def test_hypot_test():
    assert hypot_test(2, 0) == 2.0
    assert hypot_test(-1, 2) == 2.23606797749979

# # функция возвращает квадратный корень, т.е. sqrt(9) = 3
def test_sqrt_test():
    assert sqrt_test(100) == 10
    assert sqrt_test(8) == 2.8284271247461903
