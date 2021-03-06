# dog.py
# class Dog:
#     def __init__(self, name):
#         self.name = name
#         print("dog initialized!")


# # instantiation call that creates a Dog object:
# Dog("Rex")

# # the same instantiation call that creates a Dog object,
# # but now we've assigned it to the value of the my_dog variable
# my_dog = Dog("Rex")
# # Adding the "breed" property on the fly
# my_dog.breed = "SuperDog"
# # will print "SuperDog"
# print(my_dog.breed)
# print(my_dog)
# print(my_dog.name)

# dog.py
class Dog:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")

    # Methods are defined as their own named functions inside the class
    # Remember to put the "self" parameter every time we make a class method!
    def bark(self):
        print("Woof!")


