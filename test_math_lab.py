import math

import unittest
from math_lab import MathLab

class TestMathLab(unittest.TestCase):
    def test_addition(self):
        math_lab = MathLab()
        self.assertEqual(math_lab.addition(2, 3), 5)
        self.assertEqual(math_lab.addition(17, 10), 27)
        self.assertEqual(math_lab.addition(4, 19), 23)
        
    def test_subtraction(self):
        math_lab = MathLab()
        self.assertEqual(math_lab.subtraction(2, 3), -1)
        self.assertEqual(math_lab.subtraction(17, 10), 7)
        self.assertEqual(math_lab.subtraction(25, 19), 6)
    
    def test_division(self):
        math_lab = MathLab()
        self.assertEqual(math_lab.division(2, 4), 0.5)
        self.assertEqual(math_lab.division(17, 10), 1.7)
        self.assertEqual(math_lab.division(4, 20), 0.2)
        
    def test_multiplication(self):
        math_lab = MathLab()
        self.assertEqual(math_lab.multiplication(2, 3), 6)
        self.assertEqual(math_lab.multiplication(17, 10), 170)
        self.assertEqual(math_lab.multiplication(4, 19), 76)
        
    def test_squareRoot(self):
        math_lab = MathLab()
        self.assertEquals(math_lab.square_root(16), 4)
        self.assertEquals(math_lab.square_root(-3), -1)

    def test_sine(self):
        math_lab = MathLab()
        a = math.pi/6
        self.assertEquals(math_lab.sine(a),math.sin(a) )

if __name__ == "__main__":
    unittest.main()