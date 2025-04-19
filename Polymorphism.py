class Entity:
    def move(self):
        return "Moving in a unique way!"

# Animal classes
class Dog(Entity):
    def move(self):
        return "Running on four legs! 🐶"

class Bird(Entity):
    def move(self):
        return "Flying through the sky! 🕊️"

class Fish(Entity):
    def move(self):
        return "Swimming in the ocean! 🐠"

# Vehicle classes
class Car(Entity):
    def move(self):
        return "Driving on roads! 🚗"

class Plane(Entity):
    def move(self):
        return "Flying through the clouds! ✈️"

class Boat(Entity):
    def move(self):
        return "Sailing on water! ⛵"

# Using polymorphism
entities = [Dog(), Bird(), Fish(), Car(), Plane(), Boat()]
for entity in entities:
    print(entity.move())
