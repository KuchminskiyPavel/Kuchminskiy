from abc import ABC, abstractmethod
class Creature(ABC):
    def __init__(self, max_age):
        self.age = 0
        self.max_age = max_age
    @abstractmethod
    def eat(self, food):
        pass

    def determine_state(self, has_food):
        if self.age >= self.max_age or not has_food:
            return "Умер"
        else:
            return "Жив"




class Fox(Creature):
    def eat(self, food):
        if isinstance(food, Rabbit):
            return "Лиса съела кролика"
        else:
            return "Лиса это не ест"


class Rabbit(Creature):
    def eat(self, food):
        if isinstance(food, Plant):
            return "Кролик съел растение"
        else:
            return "Кролик это не ест"


class Plant(Creature):
    def eat(self, food):
        if food == "sunlight":
            return "Растение поглотило солнечную энергию"
        else:
            return "Растение не может это поглотить"



fox = Fox(10)
rabbit = Rabbit(5)
plant = Plant(2)

print(fox.eat(rabbit))
print(fox.eat(plant))
print(rabbit.eat(plant))
print(rabbit.eat(fox))
print(plant.eat("солнечную энергию"))

print(fox.determine_state(False))  # Output: True
print(rabbit.determine_state(False))  # Output: False
print(plant.determine_state(True))  # Output: True

