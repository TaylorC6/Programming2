from random import randint

# Import numpy as np (have to do pip install numpy in the terminal)


def print_matrix(mat):
    for row in mat:
        for num in row:
            print(f"{num:3d} ", end="")
        print()


def transpose(mat):
    mat2 = mat
    n = 0
    for a in range(5):
        for b in range(n):
            temp = mat[a][b]
            mat[a][b] = mat[b][a]
            mat[b][a] = temp
        n += 1
    print_matrix(mat)



def main():
    mat1 = []
    for r in range(5):
        row1 = []
        for c in range(5):
            row1.append(randint(-50, 99))
        mat1.append(row1)

    print("Matrix 1:")
    print_matrix(mat1)

    print("Matrix 2:")
    transpose(mat1)


if __name__ == "__main__":
    main()
