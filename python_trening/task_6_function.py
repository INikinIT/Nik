# Определяем функцию
def add(x, y):
    return x + y

# вызываем функцию
print(add(1,2))

# вызываем функцию с другими элементами
print(add('I a', 'm tester'))


def arg(a, b, c=2,d=3):
    return a + b + c + d


print(arg(1, 1, 1, 1,))
print(arg(2, 2))
print(arg(2, 2, 1, 1))


def range_arg(a, b, c, d, e):
    return  a+ ' ' +b+ ' ' +c+ ' ' +d+ ' ' +e


print(range_arg('1', '2', '3', '4', '5'))

print(range_arg('1', '2', '3', e='4', d='5'))


def one_arg(a = (1, 2, 3, 4)):
    return a[0]
print(one_arg())


def s_circle(radius, pi=3.14159):
    return pi * radius * radius
print(s_circle(2))

