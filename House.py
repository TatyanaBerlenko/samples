class House:
    def __init__(self, rooms_count=3, square=100, floors_count=1, yard_square=100):
        self.rooms_count = rooms_count
        self.square = square
        self.floors_count = floors_count
        self.yard_square = yard_square

    def __str__(self):
        return 'Country House: Количество жилых комнат {}, Жилая площадь {}, ' \
               'Количество этажей {}, Площадь участка {}.'.format(
            self.rooms_count, self.square, self.floors_count, self.yard_square)

    def __eq__(self, other):
        return self.rooms_count == other.rooms_count and self.square == other.square \
               and self.floors_count == other.floors_count and self.yard_square == other.yard_square
