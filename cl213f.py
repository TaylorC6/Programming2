class ElectricBill:
    def __init__(self, kwh):
        self.kwh = kwh
        self.cost = 0.0


    def calc(self):
        if self.kwh <= 2000:
            self.cost = 0.07 * self.kwh
        elif 2000 < self.kwh <= 10000:
            self.cost = (0.05 * (self.kwh - 2000)) + (2000 * 0.07)
        elif 10000 < self.kwh:
            self.cost = (0.04 * (self.kwh - 10000)) + (8000 * 0.05) + (2000 * 0.07)


    def __str__(self):
        return f"The cost of {self.kwh} is ${self.cost:.2f}"
