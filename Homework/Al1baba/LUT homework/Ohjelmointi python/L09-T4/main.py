import numpy as np


def create_matrix():
    matrix = np.zeros([4, 4], dtype=int)
    # print(matrix)
    # matrix = np.full([4, 4], 0, dtype=float)
    # print(matrix)

    for row in range(matrix.shape[0]):
        for column in range(matrix.shape[1]):
            matrix[column, row] = int((column + 1) * (row + 1))

    print("Matriisi tulostettuna numpy-muotoilulla:")
    print(matrix)
    print()
    print("Matriisi tulostettuna alkiot puolipisteillä eroteltuna:")

    for row in matrix:
        print(f"{';'.join(list(map(lambda x: str(x), row)))};")    # Perfect one liner :D

    print()


def main():
    create_matrix()


if __name__ == '__main__':
    print("Tämä ohjelma esittelee numpy-matriisin käyttöä.")
    main()
    print("Kiitos ohjelman käytöstä.")
