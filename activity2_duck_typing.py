class Car:
    def move(self):
        print("The car is driving.")

class Person:
    def move(self):
        print("The person is walking.")

class Robot:
    def move(self):
        print("The robot is moving.")

def make_it_move(thing):
    thing.move()

things = [Car(), Person(), Robot()]

for thing in things:
    make_it_move(thing)
