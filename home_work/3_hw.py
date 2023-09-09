def max_namber(a, b):
    if a > b:
        print(a)
    else:
        print(b)


max_namber(10, 20)


def namber_135(x, y):
    if x + 135 == y or x - 135 == y:
        print('yes')
    else:
        print('No')


namber_135(0,134)


def year(month):
    if 3 <= month <= 5:
        print('весна')
    elif 6 <= month <= 8:
        print('лето')
    elif 9 <= month <= 11:
        print('осень')
    else:
        print('зима')


year(9)


def thee_n(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('yes')
    else:
        print('no')


thee_n(11, 12, 13)
