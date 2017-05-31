""" Simple inheritance example between parent and child class. """

# Define one class
class Parent():

    # constructor
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

# Define another class
class Child(Parent):

    # constructor
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        # call to parent constructor
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

# parent constructor called
billy_cyrus = Parent("Cyrus", "blue")
print(billy_cyrus.last_name)
print(billy_cyrus.eye_color)
print(" ") # Blank line separator

# child constructor called
miley_cyrus = Child("Cyrus", "Blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.eye_color)
print(miley_cyrus.number_of_toys)
print(" ") # Blank line separator
