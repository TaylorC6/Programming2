class Vehicles:
    def __init__(self, name, num_tires):
        self._name = name
        self._num_tires = num_tires

    def getName(self):
        return self._name


class Car(Vehicles):
    def __init__(self, name, num_tires, worth):
        super().__init__(name, num_tires)
        self.gpa = worth


class Teacher(Person):
    def __init__(self, fn, ln, numStu):
        super().__init__(fn, ln)
        self.numStudents = numStu


class Admin(Person):
    def __init__(self, fn, ln, favW):
        super().__init__(fn, ln)
        self.favW = favW


def main():
    try:
        people = []
        with open("Langdat/prog701g.dat", 'r') as f:
            num = int(f.readline())
            while num != 99:
                fn = f.readline()
                ln = f.readline()
                if num == 1:
                    gpa = float(f.readline())
                    p = Student(fn, ln, gpa)
                    people.append(p)
                if num == 2:
                    numStu = int(f.readline())
                    p = Teacher(fn, ln, numStu)
                    people.append(p)
                if num == 3:
                    favW = f.readline().strip()
                    p = Admin(fn, ln, favW)
                    people.append(p)
                num = int(f.readline())

            tot = 0.0
            cnt = 0
            totstus = 0
            large = ""
            sm = "ashaiuvfaihviaiuvwuvhilvvdiubwieiufhgiuszhdbKVCJBXZLIVHGifuhgaoiewsgifsghoilblkjdxzvhblijzdshgfpiuewahgifauhdsikjbz;kjvdvha fphwa uehgkjf,mz.njvsahf[hfkjnds;vnjhsag;jhkjdsba;fkjb kjdxzvb,mcxzbv;shagtaewhoifhp;dskjabv,mbcxzkjvhshe;af"

            for person in people:
                if isinstance(person, Student):
                    tot += person.gpa
                    cnt += 1
                elif isinstance(person, Teacher):
                    totstus += person.numStudents
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
