
radius = float(input("Enter Radius: "))

def calcArea(radius):
    return 3.14159 * radius ** 2


def calcCircumference(radius):
    return 2 * 3.14159 * radius


def main():

    A = calcArea(radius)
    C = calcCircumference(radius)
    print(f"Area: {A}")
    print(f"Circumference: {C}")

    pass


if __name__ == "__main__":
    main()
