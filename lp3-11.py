class TimeSpent:
    def __init__(self, design, code, debug, test):
        self.design = design
        self.code = code
        self.debug = debug
        self.test = test
        self.timeSpent = 0.0
        self.percent = [0] * 4

    def get_percent(self, number):
        return round(number/self.timeSpent * 100, 2)

    def calculate(self):
        self.timeSpent = self.design + self.code + self.debug + self.test
        self.percent[0] = self.get_percent(self.design)
        self.percent[1] = self.get_percent(self.code)
        self.percent[2] = self.get_percent(self.debug)
        self.percent[3] = self.get_percent(self.test)

    def display(self):
        print("Category\tHours Spent")
        print(f"Design: {self.percent[0]}%")
        print(f"Code: {self.percent[1]}%")
        print(f"Debug: {self.percent[2]}%")
        print(f"Test: {self.percent[3]}%")
        print(f"Total hours spent: {self.timeSpent:.2f} Hours")


def main():
    print("Enter Hours Spent on the Following Items: \n")
    design = float(input("Design: "))
    code = float(input("Code: "))
    debug = float(input("Debug: "))
    test = float(input("Test: "))
    print()

    time = TimeSpent(design, code, debug, test)
    time.calculate()
    time.display()

if __name__ == "__main__":
    main()
