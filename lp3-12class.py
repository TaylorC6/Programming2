class Budget:
    def __init__(self, food, clothing, entertainment, rent):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
        self.rent = rent
        self._budget = 0
        self._percent = [0] * 4


    def _get_percent(self, number):
        return round(number/self._budget * 100, 2)


    def calculate(self):
        self._budget = self.food + self.clothing + self.entertainment + self.rent
        self._percent[0] = self._get_percent(self.food)
        self._percent[1] = self._get_percent(self.clothing)
        self._percent[2] = self._get_percent(self.entertainment)
        self._percent[3] = self._get_percent(self.rent)


    def display(self):
        print("Category\t\tBudget")
        print(f"Food: {self._percent[0]}%")
        print(f"Clothing: {self._percent[1]}%")
        print(f"Entertainment: {self._percent[2]}%")
        print(f"Rent: {self._percent[3]}%")
        print(f"Total amount spent: ${self._budget:.2f}")


def main():
    print("Enter Amount Spent Last Month on the Following Items: \n")
    food = float(input("Food: $"))
    clothing = float(input("Clothing: $"))
    entertainment = float(input("Food: $"))
    rent = float(input("Rent: $"))
    print()

    # Make new budget object. pass in the numbers to constructor
    spending = Budget(food, clothing, entertainment, rent)
    spending.calculate()
    spending.display()
    pass


if __name__ == "__main__":
    main()
