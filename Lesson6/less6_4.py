#Lesson6_4

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'{self.name} has been gone')

    def stop(self):
        self.speed = 0
        print(f'{self.name} has been stopped')

    def turn(self, direction):
        direction = direction.lower()
        if direction == 'right' or direction == 'left':
            print(f'{self.name} has been turned {direction}')

    def show_speed(self):
        print(f'{self.name} speed - {self.speed} km/h')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} speed - {self.speed} km/h - speed limit exceeded!')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} speed - {self.speed} km/h - speed limit exceeded!')
        else:
            super().show_speed()


class PoliceCar(Car):
    pass



town_car = TownCar(0, 'black', 'car_1')
town_car.go()
town_car.speed = 80
town_car.show_speed()

sport_car = SportCar(170, 'red', 'formula')
sport_car.go()
sport_car.show_speed()

work_car = WorkCar(10, 'white', 'car_2')
work_car.go()
work_car.speed = 50
work_car.show_speed()
work_car.stop()
work_car.show_speed()

police_car = PoliceCar(100, 'black&white', 'car_3')
police_car.turn('left')
police_car.turn('right')
