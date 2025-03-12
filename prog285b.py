from cl285b import Salesperson


def main():
    try:
        print("Number\tCode\tSale\tCommission")
        with open("Langdat/prog285b.dat", 'r') as f:
            for line in f:
                data = line.split(" ")
                id = float(data[0])
                code = float(data[1])
                sales = float(data[2])

                person = Salesperson(id, code, sales)
                person.calc_commission()
                print(str(person))
    except Exception as e:
        print("Error:", e)

    pass


# Option 2: List Comprehension
# id, code, sales = [float(x) for x in line.split(" ")]
# Option 3: Conditional List Comprehension
# id, code, sales = [float(x) if '.' in x else int(x) for x in line.split(" ")]


if __name__ == "__main__":
    main()
