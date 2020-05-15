

class Car():

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def repaint(self, new_color):
        self.color = new_color


my_car = Car(color='yellow', brand='bmw')
my_second_car = Car(color='blue', brand='mercedes')

print(my_car.color)
print(my_second_car.color)

my_car.repaint('black')

print(my_car.color)




