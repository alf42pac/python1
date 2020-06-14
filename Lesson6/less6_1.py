#Lesson6_1

import time
class TrafficLight:
    def __init__(self):
        self.__color = "красный"

    def running(self):
        print(self.__color)
        time.sleep(7)
        self.__color = 'желтый'
        print(self.__color)
        time.sleep(2)
        self.__color = 'зеленый'
        print(self.__color)

a=TrafficLight()
a.running()