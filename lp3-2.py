class Pizza:
    def __init__(self, diameter, cost):
        self.diameter = diameter
        self.cost = cost

    def calc(self):
        self.cost = 0.05 * self.diameter * self.diameter
        return self.cost


def main():
    dmeter = int(input("Enter the diameter of the pizza: "))
    pizza = Pizza(dmeter, 0)
    cost = pizza.calc()
    print(f"The cost of your pizza is {cost}!")

if __name__ == '__main__':
    main()
