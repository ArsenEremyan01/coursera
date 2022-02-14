import unittest


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        self.cases = ('string', 1.5)
        for i in self.cases:
            with self.subTest(i=i):
                self.assertRaises(TypeError, factorize, i)

    def test_negative(self):
        self.cases = (-1, -10, -100)
        for i in self.cases:
            with self.subTest(i=i):
                self.assertRaises(ValueError, factorize, i)

    def test_zero_and_one_cases(self):
        self.cases = (0, 1)
        for i in self.cases:
            with self.subTest(i=i):
                self.assertTupleEqual(factorize(i), (i,))

    def test_simple_numbers(self):
        self.cases = (3, 13, 29)
        for i in self.cases:
            with self.subTest(i=i):
                self.assertTupleEqual(factorize(i), (i,))

    def test_two_simple_multipliers(self):
        self.cases = (6, 26, 121)
        test_num = ((2, 3), (2, 13), (11, 11))
        for i, j in enumerate(self.cases):
            with self.subTest(j=j):
                self.assertTupleEqual(factorize(j), test_num[i])

    def test_many_multipliers(self):
        self.cases = (1001, 9699690)
        test_num = ((7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19))
        for i, j in enumerate(self.cases):
            with self.subTest(j=j):
                self.assertTupleEqual(factorize(j), test_num[i])
