import unittest
from algorithm.multiplication import karatsuba

class SortingTest(unittest.TestCase):
    def test_true(self):
        print('Hello, welcome to the algorithm world!')
        self.assertTrue(True, "Test value is not true :(")

    def test_insertion_sort(self):
        self.assertEqual(karatsuba(3,5), 15)
        self.assertEqual(karatsuba(15, 15), 225)
        self.assertEqual(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                                   2718281828459045235360287471352662497757247093699959574966967627),
                                   8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184)
        
if __name__ == '__main__':
    unittest.main()