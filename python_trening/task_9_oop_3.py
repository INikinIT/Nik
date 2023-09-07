class Soda:

    def __init__(self, dop=None):
        self.dop = dop

    def show_my_drink(self):
        if self.dop:
            print(f'Газировка и  - {self.dop}')

        else:
            print('Обычная газировка')


drink_1 = Soda()
drink_1.show_my_drink()
drink_2 = Soda('ДОБАВКА')
drink_2.show_my_drink()
