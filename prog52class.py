class Shape:
    # Constructor: Sets up class data
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self._area = 0  # prefix means 'private' so it should only be called in class
        self._perim = 0

    # Mutator/Setter Method: Modifies Class Data
    def calculate(self):
        self._area = self.length * self.width
        self._perim = 2 * self.length + 2 * self.width

    # Accessor/Getter Method(s): Returns Class Data
    def get_area(self):
        return self._area

    def get_perim(self):
        return self._perim


def main():
    length = int(input("Enter Length: "))
    width = int(input("Enter Width: "))
    # Make new shape object/instance
    shape = Shape(length, width) # Call 'Shape' constructor/__init__ method
    shape.calculate()
    print("Area: ", shape.get_area())
    print("Perimeter: ", shape.get_perim())
    pass



if __name__ == "__main__":
        main()
