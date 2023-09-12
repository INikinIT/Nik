class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен')

    def stop(self):
        print("Автомобиль заглушен")

    def year_car(self, y_new):
        self.year = y_new
        print('Год производства автомобиля -', self.y_new)

    def type_car(self):
        print('Тип автомобиля -', self.type)

    def color_car(self):
        print('Цвет автомобиля -', self.color)


car_1 = Car('Красный', "Спортивный", 2000)
car_1.start()
car_1.stop()
car_1.year_car()
car_1.type_car()
car_1.color_car()


