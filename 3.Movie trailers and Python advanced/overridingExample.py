""" Simple overriding example between parent and child class. """

class Parent(object):
    """ Class about parents """

    # parent constructor
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    # parent method
    def show_info(self):
        print("Last Name - {}".format(self.last_name))
        print("Eye Color - {}".format(self.eye_color))

class Child(Parent):
    """ A Child class that inherits from Parent class """

    # child constructor
    def __init__(self, last_name, eye_color, number_of_toys):
        print(" ") # Blank line separator
        print("Child constructor called")
        super(Child, self).__init__(last_name, eye_color)
        self.number_of_toys = number_of_toys

    # child method overriding parent method
    def show_info(self):
        print("Last Name - {}".format(self.last_name))
        print("Eye Color - {}".format(self.eye_color))
        print("Number of Toys - {}".format(self.number_of_toys))

# parent constructor call
p = Parent("Lant", "Hazel")
# parent method call
p.show_info()
# child constructor call
c = Child("Smith-Lant", "Brown", "100")
# child method call
c.show_info()
