class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def method_p(self):
        print('Площадь =', self.width * self.height)

    def method_s(self):
        print('Периметр =', self.width * 2 + self.height * 2, '\n')


data_1 = Rectangle(10, 20)
data_1.method_p()
data_1.method_s()

data_2 = Rectangle(4, 6)
data_2.method_p()
data_2.method_s()

data_3 = Rectangle(55, 23)
data_3.method_p()
data_3.method_s()


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print('Складываем a + b =', self.a + self.b)

    def multiplication(self):
        print('Умножаем a * b =', self.a * self.b)

    def division(self):
        print('Делим a / b =', self.a / self.b)

    def subtraction(self):
        print('Вычитаем a - b =', self.a - self.b, '\n')


data_4 = Math(50, 8)
data_4.addition()
data_4.multiplication()
data_4.division()
data_4.subtraction()


class Button:
    type_but = 'Кнопка'

    def __init__(self, text, loc=None):
        self.text = text
        self.loc = loc

    def but_ton(self):
        print("Клик по кнопке {}".format(self.text))


button_1 = Button('Text Box', ' ')
print(button_1.text + ' ' + button_1.type_but + button_1.loc)
button_1.but_ton()

button_2 = Button('Check Box', ' ')
print(button_2.text + ' ' + button_2.type_but + button_2.loc)
button_2.but_ton()

button_3 = Button('Radio Button', ' ')
print(button_3.text + ' ' + button_3.type_but + button_3.loc)
button_3.but_ton()

button_4 = Button('Web Tables', ' ')
print(button_4.text + ' ' + button_4.type_but + button_4.loc)
button_4.but_ton()

button_5 = Button('Buttons', ' ')
print(button_5.text + ' ' + button_5.type_but + button_5.loc)
button_5.but_ton()

button_6 = Button('Links', ' ')
print(button_6.text + ' ' + button_6.type_but + button_6.loc)
button_6.but_ton()

button_7 = Button('Broken Links - Images', ' ')
print(button_7.text + ' ' + button_7.type_but + button_7.loc)
button_7.but_ton()

button_8 = Button('Upload and Download', ' ')
print(button_8.text + ' ' + button_8.type_but + button_8.loc)
button_8.but_ton()

button_9 = Button('Dynamic Properties', ' ')
print(button_9.text + ' ' + button_9.type_but + button_9.loc)
(button_9.but_ton())
