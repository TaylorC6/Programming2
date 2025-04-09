from 701g import *


def main():
    try:
        people = []
        with open("data/prog701g.dat", 'r') as f:
            num = int(f.readline())
            while num != 99:
                fn = f.readlines()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
