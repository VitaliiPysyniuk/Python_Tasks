# ######################################################################
# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text

text_list = list()

class Letter:
    __count = 0

    def __init__(self, text):
        self.__text = text
        Letter.__count += 1

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    @text.deleter
    def text(self):
        del self.__text

    @classmethod
    def show_counter(cls):
        return cls.__count

    def append(self):
        text_list.append(self.__text)




letter1 = Letter('aaa')
letter2 = Letter('bbb')
letter3 = Letter('ccc')

# print(Letter.show_counter())
# letter1.append()
# print(text_list)

# ###############################################################################
# 1) написати програму для запису відомостей про пасажирські перевезення
# 2) перевезення відбувається трьома способами, літаком, машиною, поїздом,
# 3) дані які треба буде зберігати:
#   - вартість квитка(літак, поїзд)
#   - кількість пасажирів(машина)
#   - час в дорозі(всі)
#   - час реєстрації(літак)
#   - клас:перший,другий(літак)
#   - вартість пального(машина)
#   - км(машина)
#   - місце: купе,св(поїзд)
# 4) методи:
#   - розрахунок вартості доїзду(машина)
#   - загальний час перельоту(літак)
#   - порівняти час в дорозі між двома будь якими транспортними засобами(двома об'єктами) - наприклад"літак на 5 годин швидше за поїзд"
#   - вивести всі дані про перевезення(поїзд)

class Transport:

    def __init__(self, time_in_trip):
        self.__time_in_trip = time_in_trip

    @property
    def time_in_trip(self):
        return self.__time_in_trip

    def __gt__(self, other):
        print(f'Trip in {self.__class__.__name__} is {other.time_in_trip - self.__time_in_trip} minutes faster than {other.__class__.__name__} ')


class Car(Transport):

    def __init__(self, passengers, time_in_trip, oil_price, distance):
        super().__init__(time_in_trip)
        self.passengers = passengers
        self.oil_price = oil_price
        self.distance = distance

    def trip_price(self):
        return self.distance * self.oil_price


class PlainTrain(Transport):

    def __init__(self, ticket_price, time_in_trip):
        super().__init__(time_in_trip)
        self.__ticket_price = ticket_price

    @property
    def ticket_price(self):
        return self.__ticket_price


class Plane(PlainTrain):

    def __init__(self, ticket_price, time_in_trip, register_time, plane_class):
        super().__init__(ticket_price, time_in_trip)
        self.register_time = register_time
        self.plane_class = plane_class

    def flight_time(self):
        return self.register_time + super().time_in_trip


class Train(PlainTrain):

    def __init__(self, ticket_price, time_in_trip, train_class):
        super().__init__(ticket_price, time_in_trip)
        self.__train_class = train_class

    def trip_info(self):
        print(f'Trip info class: {self.__train_class} price: {super().ticket_price} trip_time: {super().time_in_trip}')


car1 = Car(4, 120, 30, 90)
plane1 = Plane(500, 360, 30, 'extra')
train1 = Train(100, 600, 'kupe')

# print(car1.__dict__)
train1.trip_info()

car1 > plane1
plane1 > car1

