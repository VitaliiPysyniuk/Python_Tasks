# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 23 fdfdg544'
#
# numbers = ','.join([n for n in st if n.isdigit()])
# print(numbers)


# #################################################################################

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'

# numbers = ''.join([s for s in st if s.isdigit() or s == ' ']).lstrip().replace(' ', ', ')
# print(numbers)


# numbers = ''.join([s for s in st if s.isdigit() or s == ' ']).lstrip().split(' ')
# for number in numbers[:len(numbers) - 1]:
#     print(number, end=', ')
# print(numbers[-1])




# #################################################################################



# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# print([s.upper() for s in greeting])


# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print([pow(i, 2) for i in range(51) if i % 2 != 0])







# function
#
# - створити функцію яка виводить ліст
# def showList(newList):
#     print(newList)
#
# showList([1, 2, 3])


# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# def minValue(*args):
#     return min(*args)
#
#
# print(minValue(9, 10, 7))

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def maxValue(*args):
#     print(max(*args))
#     return max(*args)
#
# print(maxValue(9, 10, 7))

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def maxMinValue(*args):
#     print(max(*args))
#     return min(*args)
#
# print(maxMinValue(9, 10, 7, 4, -10, 0))


# - створити функцію яка виводить ліст
# def showList(newList):
#     print(newList)
#
# showList([1, 2, 3])


# - створити функцію яка повертає найбільше число з ліста
# def showListMaxValue(newList):
#     return max(newList)
#
# print(showListMaxValue([1, 2, 3]))

# - створити функцію яка повертає найменьше число з ліста
# def showListMinValue(newList):
#     return min(newList)
#
# print(showListMinValue([1, 2, 3]))


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def getListValueSum(newList):
#     print(newList)
#     return sum(newList)
#
# print(getListValueSum([1, 2, 3, -5]))


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def getListValueAvg(newList):
#     print(newList)
#     return sum(newList) / len(newList)
#
# print(getListValueAvg([1, 2, 3, -5]))






# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення

# def decorator(myFun):
#     def decorated(*args, **kwargs):
#         return myFun(*args, **kwargs).replace('_', ' ')
#     return decorated
#
# @decorator
# def pr():
#     return 'Hello_boss_!!!'
#
# print(pr())
