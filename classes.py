#######1##########
# class Person:
#     def __init__(self, age: int, weight: int):
#         self.age = age
#         self.weight = weight
#
#     def visual (self):
#         print(f"Возраст:",self.age)
#         print(f"Вес:",self.weight)
#     def modify (self,age1:int,weight1:int)->None:
#         self.age = age1
#         self.weight = weight1
#     def summary (self):
#         return self.age + self.weight
#     def maximum (self):
#         return max(self.age, self.weight)
# Mike = Person(age=16,weight= 62)
# Mike.visual()
# Mike.modify(age1=17,weight1= 65)
# Mike.visual()
# summa = Mike.summary()
# print(summa)
# maxi = Mike.maximum()
# print(maxi)

#######2##########

# class Counter:
#     def __init__(self, minimum=0, maximum=100, value=0):
#         self.minimum = minimum
#         self.maximum = maximum
#         self.value = value
#
#     def increment(self):
#         if self.value < self.maximum:
#             self.value += 1
#
#     def decrement(self):
#         if self.value > self.minimum:
#             self.value -= 1
#
#     @property
#     def current_value(self):
#         return self.value
#
# counter1 = Counter()
# print("Счетчик 1:")
# print( counter1.current_value)
# counter1.increment()
# print( counter1.current_value)
# counter1.decrement()
# print( counter1.current_value)
#
# counter2 = Counter(5, 15, 8)
# print()
# print( counter2.current_value)
# counter2.increment()
# print( counter2.current_value)
# counter2.decrement()
# print( counter2.current_value)

#######3##########

# class Shop:
#     def __init__(self):
#         self.products = []
#
#     def add_prod(self, product):
#         self.products.append(product)
#         print(f"Продукт '{product}' добавлен ")
#
#     def remove_prod(self, product):
#         if product in self.products:
#             self.products.remove(product)
#             print(f"Продукт '{product}' удален ")
#         else:
#             print(f"Продукт '{product}' не найден ")
#
#     def search_prod(self, name):
#         found_products = []
#         for product in self.products:
#             if name.lower() in product.lower():
#                 found_products.append(product)
#         if found_products:
#             print(f"продукты с названием '{name}':")
#             for product in found_products:
#                 print(product)
#         else:
#             print(f"Продукты c названием '{name}' не найдены.")
#
# shop = Shop()
#
# shop.add_prod("Яблоко")
# shop.add_prod("Банан")
# shop.add_prod("Апельсин")
# shop.add_prod("Манго")
#
# shop.search_prod("Яблоко")
# shop.search_prod("параамсвп")
#
# shop.remove_prod("Банан")
# shop.remove_prod("Груша")

#######4##########

# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.coins = 0
#
#     def can_add(self, v):
#         return self.coins + v <= self.capacity
#
#     def add(self, v):
#         if self.can_add(v):
#             self.coins += v
#             print(f"Добавлено {v} монет ")
#         else:
#             print("Невозможно добавить cтолько монет ")
#
# money_box = MoneyBox(10)
#
# money_box.add(3)
# money_box.add(2)
# money_box.add(4)
# money_box.add(1)
# money_box.add(20)