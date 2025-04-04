class Family:
    def __init__(self, age_group, distribution, percentage):
        self.age_group = age_group
        self.distribution = distribution
        self.percentage = percentage

    def calc_dstr(self, datas):
        for data in (len(datas)):
            if data < 20:
                self.distribution = 3
            elif 20 <= data <= 39:
                self.distribution = 5
            elif 40 <= data <= 59:
                self.distribution = 4
            elif 60 <= data <= 79:
                self.distribution = 3
            elif data > 79:
                self.distribution = 2
            return self.distribution

    def calc_perc(self, distribu, members):
        return distribu / members


# Age  Group  Distribution   Percentage
#         <20            3                 17.65
#      20-39            5                 29.41
#      40-59            4                 23.53
#      60-79            3                 17.65
#         >79            2                 11.76

def main():
    try:
        with open("Langdat/prog213e.dat", 'r') as f:
            dat = f.readlines()
            members = dat[0]
            dstr = Family.calc_dstr(dat)
            perc = Family.calc_perc(Family.calc_perc(line), members)
            print(dstr)
            print(perc)
    except OSError as e:
        print("Error", e)

    pass


if __name__ == "__main__":
    main()
