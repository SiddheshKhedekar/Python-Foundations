""" Simple class example with Objects, Constructor and Class, Instance variables functioning. """

# Define class
class t_shirt():

    # Define class variables here
    SIZES = ["small", "medium", "large"]

    # Define instance variables here
    def __init__(self, name, color): # constructor
        print("t_shirt constructor called")
        self.name = name
        self.color = color

    # Define methods here
    def show_info(self):
        print("name - "+self.name)
        print("color - "+self.color)

print("")
print("Instantiate shirt1, a tshirt object...")
# object creation and constructor call
shirt1 = t_shirt("shirt1", "blue")
# method call
shirt1.show_info()
print("") # Blank line separator
print("Print a class variable...")
# print a class variable
print(t_shirt.SIZES)
print("") # Blank line separator
print("Print an instance variable...")
# print a instance variable
print(shirt1.color)
