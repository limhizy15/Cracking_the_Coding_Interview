import unittest

def is_unique_chars(str):
    dictionary = {}

    for s in str:
        if s in dictionary.keys():
            return False
        dictionary[s] = True
    return True


class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]

    def test_is_unique_chars(self):
        for text, expected in self.test_cases:
            assert (is_unique_chars(text) == expected)

if __name__ == "__main__":
    unittest.main()