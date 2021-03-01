import math

# 1)
# создать класс Human(имя и возраст)
# и два класса Prince и Cinderella которые наследуются от Human
# у принца должен быть размер туфельки и  метод который принимает лист золушек и выводит какой золушки подошла туфелька

# class Human:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cinderella(Human):
#
#     def __init__(self, name, age, foot_size):
#         super().__init__(name, age)
#         self.foot_size = foot_size
#
#
# class Prince(Human):
#
#     def __init__(self, name, age, shoe_size):
#         super().__init__(name, age)
#         self.shoe_size = shoe_size
#
#     def find_cinderella(self, cinderellas):
#         found_cinderellas = [c for c in cinderellas if c.foot_size == self.shoe_size]
#         if len(found_cinderellas) == 1:
#             print(self.name, found_cinderellas[0].__dict__, sep=' <---> ')
#         elif len(found_cinderellas) > 1:
#             for cinderella in found_cinderellas:
#                 print(self.name, cinderella.__dict__, sep=' <---> ')
#         else:
#             print('No one cinderella was found')
#         print('-----------------------------------------------------------------------------------------------------')
#
#
# princes = [Prince('Vitaliy', 20, 39), Prince('Anton', 25, 41), Prince('Oleg', 21, 38), Prince('Stepan', 28, 40)]
#
# cinderellas = [Cinderella('Diana', 19, 39), Cinderella('Alina', 25, 40), Cinderella('Maria', 27, 40),
#                Cinderella('Sonya', 19, 38)]
#
# for prince in princes:
#     prince.find_cinderella(cinderellas)


# 2)
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = x * y

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        return math.fabs(self.area - other.area)

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other

    def __gt__(self, other):
        return self.area > other.area

    def __lt__(self, other):
        return  self.area < other.area

    def __len__(self):
        return 2 * self.x + 2 * self.y


rectangle1 = Rectangle(2, 4)
rectangle2 = Rectangle(5, 5)

print('Sum: ', rectangle1 + rectangle2)
print('Subtraction: ', rectangle1 - rectangle2)
print('Equal: ', rectangle1 == rectangle2)
print('Greater then: ', rectangle1 > rectangle2)
print('Less then: ', rectangle1 < rectangle2)
print('Rectangle 1 length: ', len(rectangle1))
print('Rectangle 2 length: ', len(rectangle2))

