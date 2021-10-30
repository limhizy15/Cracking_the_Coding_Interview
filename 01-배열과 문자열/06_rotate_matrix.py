# 😞 못품

import unittest

def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        start, end = layer, n - layer - 1

        for i in range(start, end):
            top = matrix[layer][i]
            matrix[layer][i] = matrix[-i - 1][layer]
            print("left to top:", matrix)
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            print("bottom to left:", matrix)
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            print("right to bottom", matrix)
            matrix[i][-layer - 1] = top
            print("top to right", matrix)

    return matrix

class Test(unittest.TestCase):
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.test_cases:
            assert rotate_matrix(test_matrix) == expected

if __name__ == "__main__":
    unittest.main()