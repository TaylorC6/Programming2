class Family:
    def __init__(self, ages, total):
        self.total = total
        self.ages = ages
        self.dis = []
        self.per = []
        self.d0 = 0
        self.d20 = 0
        self.d40 = 0
        self.d60 = 0
        self.d80 = 0

    def calc_dstr(self):
        for data in self.ages[1:self.total]:
            if data < 20:
                self.d0 += 1
            elif 20 <= data <= 39:
                self.d20 += 1
            elif 40 <= data <= 59:
                self.d40 += 1
            elif 60 <= data <= 79:
                self.d60 += 1
            elif data > 79:
                self.d80 += 1
            self.dis = [self.d0, self.d20, self.d40, self.d60, self.d80]
            return self.dis

    def calc_perc(self):
        for n in self.dis:
            self.per.append(((n / self.total) * 100))

    def display(self):
        for p in self.dis:
            print(f"{self.dis[p]}, {self.per[p]}\n")
# Age  Group  Distribution   Percentage
#         <20            3                 17.65
#      20-39            5                 29.41
#      40-59            4                 23.53
#      60-79            3                 17.65
#         >79            2                 11.76


def main():

    try:
        with open("Langdat/prog213e.dat", 'r') as f:
            ages = f.readlines()
            for i in range(len(ages)):
                ages[i] = int(ages[i])
            total = ages[1]
            family = Family(ages, total)
            family.calc_dstr()
            family.calc_perc()
            family.display()
    except OSError as e:
        print("Error", e)


    pass


if __name__ == "__main__":
    main()
