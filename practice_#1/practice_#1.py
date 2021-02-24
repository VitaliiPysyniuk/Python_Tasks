# shoppingList = list()
#
#
# while True:
#     print('1. Add new purchase\n2. List of purchase\n3. Average sum of purchase\n' +
#           '4. The most expensive purchase.\n5. Find purchase by name.\n6. Exit.\n')
#     command = input('Select command: ')
#     if command == '1':
#         purchase = dict()
#         purchase['name'] = input('Enter purchase name: ')
#         purchase['price'] = float(input('Enter purchase price: '))
#         shoppingList.append(purchase)
#         print('\n')
#
#     elif command == '2':
#         for listItem in shoppingList:
#             print('Name: ', listItem['name'], '\t\tPrice: ', listItem['price'])
#         print('\n')
#
#     elif command == '3':
#         averageSum = 0
#         for listItem in shoppingList:
#             averageSum += listItem['price']
#         print('Average sum of purchase: ', averageSum)
#         print('\n')
#
#     elif command == '4':
#         expPurchase = {'price': 0}
#         for listItem in shoppingList:
#             expPurchase = listItem if listItem['price'] > expPurchase['price'] else expPurchase
#         print('The most expensive purchase: Name: ', expPurchase['name'], '\t\tPrice: ', expPurchase['price'])
#         print('\n')
#
#     elif command == '5':
#         name = input('Enter the name of purchase: ')
#         foundedPurchase = {}
#         for listItem in shoppingList:
#             foundedPurchase = listItem if listItem['name'].find(name) != -1 else foundedPurchase
#         if foundedPurchase:
#             print('Found purchase: Name: ', foundedPurchase['name'], '\t\tPrice: ', foundedPurchase['price'])
#         else:
#             print('Purchase was not found.')
#         print('\n')
#     elif command == '6':
#         break
#     else:
#         print('Unknown command. Make your choice again. ')
#         continue
#

