a: int = 5
b: str = 'строка'
c: list = [1, 2]


def indent(s: str, widht: int) -> str:
    return " " * (max(0, widht - len(s))) + s
print(indent('123', 123))


def dlina_stroki(s: str = '') -> int:
    return len(s)


def dlina_spiska(a: list, b: list) -> int:
    return max(len(a), len(b))


def ap_list(my_list: list):
    my_list.append('test')
    return my_list

print(ap_list(['один', 2, 3]))


def sum_list(my_list: list) -> int:
    result = 0
    for elem in my_list:
        result = result + elem
    return result

print(sum_list([1, 2, 3, 4]))
