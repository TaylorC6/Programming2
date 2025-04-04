def main():
    price = float(0)
    nums = [50, 199, 200, 475]
    for num in nums:
        if 0 <= num <= 99:
            price = 5.95
        elif 100 <= num <= 199:
            price = 5.75
        elif 200 <= num <= 299:
            price = 5.40
        elif 300 <= num:
            price = 5.15
        else:
            print("Error! Invalid Number!")
        print(f"Quantity: {num}")
        print(f"Price: {price}")
        print(f"Amount Due: ${price * num}\n")
        # print("")
    pass


if __name__ == "__main__":
    main()
