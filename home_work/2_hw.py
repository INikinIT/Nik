def task_1(task_int: int, task_float: float, task_str: str, task_list: list, task_bool: bool):
    return task_1


print(type(1), type(3.4), type('sdd'), type([5, 4, 5]), type(True))


def task_2(a = [1, 2, 3, 5, 8, 12, 21]) -> list:
    return a[0:3]


print(task_2())
# Последовательность называется список


def task_3(number: int = 5) -> int:
    return number ** 2


print(task_3())