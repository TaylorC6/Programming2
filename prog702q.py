class Vehicles:
    def __init__(self, name, num_tires):
        self._name = name
        self._num_tires = num_tires

    def getName(self):
        return self._name


class Car(Vehicles):
    def __init__(self, name, num_tires, worth):
        super().__init__(name, num_tires)
        self.worth = worth


class Truck(Vehicles):
    def __init__(self, name, num_tires, miles):
        super().__init__(name, num_tires)
        self.miles = miles


class Bus(Vehicles):
    def __init__(self, name, num_tires, home):
        super().__init__(name, num_tires)
        self.home = home


def main():
    try:
        people = []
        with open("Langdat/prog701g.dat", 'r') as f:
            num = int(f.readline())
            while num != 99:
                name = f.readline()
                num_tires = f.readline()
                if num == 1:
                    worth = float(f.readline())
                    p = Vehicles(name, num_tires, worth)
                    people.append(p)
                if num == 2:
                    miles = int(f.readline())
                    p = Vehicles(name, num_tires, miles)
                    people.append(p)
                if num == 3:
                    favW = f.readline().strip()
                    p = Admin(name, num_tires, favW)
                    people.append(p)
                num = int(f.readline())

            tot = 0.0
            cnt = 0
            totstus = 0
            large = ""
            sm = "ashaiuvfaihviaiuvwuvhilvvdiubwieiufhgiuszhdbKVCJBXZLIVHGifuhgaoiewsgifsghoilblkjdxzvhblijzdshgfpiuewahgifauhdsikjbz;kjvdvha fphwa uehgkjf,mz.njvsahf[hfkjnds;vnjhsag;jhkjdsba;fkjb kjdxzvb,mcxzbv;shagtaewhoifhp;dskjabv,mbcxzkjvhshe;af"

            for person in people:
                if isinstance(person, Student):
                    tot += person.worth
                    cnt += 1
                elif isinstance(person, Vehicles):
                    totstus += person.miles
                elif isinstance(person, Admin):
                    favW = person.favW
                    if len(favW) > len(large):
                        large = favW
                    if len(favW) < len(sm):
                        sm = favW

            print("Average student GPA:", round(tot/cnt, 2))
            print("Total number of students taught:", totstus)
            print("Smallest favorite admin word:", sm)
            print("Largest favorite admin word:", large)

    except Exception as e:
        print("Error:", e)
        raise e


if __name__ == "__main__":
    main()
