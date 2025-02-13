import voidfunctions

def calcArea(len,wid) -> int:
    return len * wid


def calcPerim(len: int, wid: int) -> int:
    return len * 2 + 2 * wid


def areaPerim(len, wid):
    area = calcArea(len, wid)
    perim = calcPerim(len, wid)
    return area, perim


def main():
    voidfunctions.doThing()
    length = int(input("Enter Length:"))
    width = int(input("Enter Width:"))
    a, p = areaPerim(length, width)
    print(f"Area: {a}\nPerimeter: {p}")


if __name__ == "__main__":
    main()
