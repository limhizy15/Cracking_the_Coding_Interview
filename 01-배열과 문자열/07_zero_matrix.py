import unittest

def zero_matrix(matrix):
    zero_y = []
    zero_x = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_y.append(i)
                zero_x.append(j)
    
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if (y in zero_y) or (x in zero_x):
                matrix[y][x] = 0

    return matrix

class Test(unittest.TestCase):
    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.test_cases:
            assert zero_matrix(test_matrix) == expected

if __name__ == "__main__":
    unittest.main()