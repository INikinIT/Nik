from python_trening.task_9_cheks import Checks
class Input(Checks):

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


search = Input('Учим ', 'Python')
print(search.loc + search.text)


class Button:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


search = Button('Знаем ', 'Python')
print(search.loc + search.text)


class Title:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


search = Title('Работаем с ', 'Python')
print(search.loc + search.text)


class Link:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


search = Link('Пишем тесты на ', 'Python')
print(search.loc + search.text)
