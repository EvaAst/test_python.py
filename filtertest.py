#Возвращает итератор из тех элементов, для которых function возвращает истину.

def filter_test(num):
    dano = list(filter(str.isdigit, num))
    return dano
