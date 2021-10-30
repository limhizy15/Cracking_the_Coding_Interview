import unittest

def urlify(str, length):
    return str[:length].replace(' ', '%20')


class Test(unittest.TestCase):
    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }

    def test_urlify(self):
        for args, expected in self.test_cases.items():
                actual = urlify(*args)
                assert actual == expected

if __name__ == "__main__":
    unittest.main()