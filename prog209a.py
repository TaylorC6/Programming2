def main():
    n1 = 0
    n2 = 0
    n3 = 0
    try:
        with open("Langdat/prog215a.dat", 'r') as f:
            for line in f:
                if line < 500:
                    n1 += 1
                if line >= 500:
                    n2 += 1
                n3 += 1
    except OSError as e:
        print("Error", e)

    print(f"The number of numbers less than 500 is {n1}")
    print(f"The number of numbers greater than or equal to 500 is {n2}")
    print(f"The total number of numbers is {n3}")
    pass

if __name__ == '__main__':
    main()
