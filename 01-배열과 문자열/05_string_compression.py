import unittest

def string_compression(string):
    if len(string) == 0:
        return ''

    target = string[0]
    cnt = 1
    i = 1
    answer = ''

    while i < len(string):
        current = string[i]

        if current == target:
            cnt += 1
            i += 1
        else:
            answer += target
            answer += str(cnt)
            target = string[i]
            cnt = 1
            i += 1
    
    answer += target
    answer += str(cnt)

    return answer if len(answer) < len(string) else string

class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]

    def test_string_compression(self):
        for test_string, expected in self.test_cases:
            assert string_compression(test_string) == expected

if __name__ == "__main__":
    unittest.main()