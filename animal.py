class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print(
            "{} sleeps for {} hours".format(
                self.name,
                self.sleep_duration))

    def eat(self):
        print('{} is eating'.format(self.name))

    def drink(self):
        print('{} is drinking'.format(self.name))


class Frog(Animal):
    def jump(self):
        print('{} is jumping'.format(self.name))


class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")


doggie = Dog("jo", 12)
doggie.sleep()
doggie.bark()

froggy = Frog("mink", 2)
froggy.jump()
froggy.eat()
