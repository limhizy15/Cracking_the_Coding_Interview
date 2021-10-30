import unittest

def string_reverse(str):
    new_str = ''
    for i in range(len(str) - 1, -1, -1):
        new_str += str[i]
    return new_str


class Test(unittest.TestCase):
    test_cases = [
        ("abcde", "edcba"),
        ("s4fad", "daf4s"),
        ("1423", "3241"),
        ("23ds2", "2sd32"),
        ("hb 627jh=j ()", ")( j=hj726 bh"),
    ]

    def test_string_reverse(self):
        for text, expected in self.test_cases:
            assert (string_reverse(text) == expected)

if __name__ == "__main__":
    unittest.main()