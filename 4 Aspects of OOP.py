class Shape:
    """
    A class representing a basic geometric shape.
    """

    def __init__(self, name):
        """
        Constructor to initialize a Shape object.

        Parameters:
        - name (str): The name of the shape.
        """
        self.name = name

    def area(self):
        """
        Abstract method to calculate the area of the shape.
        This method needs to be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

    def display_info(self):
        """
        Display information about the shape.
        """
        print(f"This is a {self.name}.")


class Square(Shape):
    """
    A subclass representing a square, inheriting from the Shape class.
    """

    def __init__(self, side_length):
        """
        Constructor to initialize a Square object.

        Parameters:
        - side_length (float): The length of each side of the square.
        """
        super().__init__("Square")
        self.side_length = side_length

    def area(self):
        """
        Calculate the area of the square.

        Formula: area = side_length * side_length
        """
        return self.side_length ** 2


class Circle(Shape):
    """
    A subclass representing a circle, inheriting from the Shape class.
    """

    def __init__(self, radius):
        """
        Constructor to initialize a Circle object.

        Parameters:
        - radius (float): The radius of the circle.
        """
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Formula: area = pi * radius^2
        """
        pi = 3.14
        return pi * self.radius ** 2


# Create instances of Square and Circle
square = Square(side_length=4)
circle = Circle(radius=3)

# Demonstrate polymorphism by calling the 'area' method on different shapes
shapes = [square, circle]
for shape in shapes:
    print(f"The area of the {shape.name} is {shape.area()} square units.")

# Demonstrate encapsulation by displaying information about each shape
for shape in shapes:
    shape.display_info()
