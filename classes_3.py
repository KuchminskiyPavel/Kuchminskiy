class Cargo():
    def __init__(self, price: int,  speed: int):
        self.price = price
        self.speed = speed

    def calc_time(self,distance):
        self.distance = distance
        return distance/self.speed

    def calc_price(self,distance):
        self.distance = distance
        return self.price*distance


class Plane(Cargo):
    def __init__(self,speed,price):
        super().__init__(price,speed)




class Train(Cargo):
    def __init__(self, speed, price):
        super().__init__(price, speed)



class Car(Cargo):
    def __init__(self, speed, price):
        super().__init__(price, speed)

car = Car(120,7)
plane = Plane(300,150)
train = Train(175,70)



car_delivery_time = car.calc_time(500)
car_delivery_cost = car.calc_price(500)

train_delivery_time = train.calc_time(500)
train_delivery_cost = train.calc_price(500)

plane_delivery_time = plane.calc_time(500)
plane_delivery_cost = plane.calc_price(500)
print(f"Время доставки автомобилем {round(car_delivery_time,1)} часов и цена:{car_delivery_cost} ")
print(f"Время доставки поездом {round(train_delivery_time,1)} часов и цена:{train_delivery_cost} ")
print(f"Время доставки самолетом {round(plane_delivery_time,1)} часов и цена:{plane_delivery_cost} ")