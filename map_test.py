#Итератор, получившийся после применения к каждому элементу последовательности функции function.
def f(x):
    b = list(map(len, x))
    return b

c= ['hello', 'hi', 'good day']
print (f(c))
