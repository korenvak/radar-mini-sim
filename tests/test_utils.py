import unittest
from radar.core.utils import solve_2x2

class TestSolve2x2(unittest.TestCase):
    def test_regular_system(self):
        A = [[2.0, 1.0],[5.0, 7.0]]
        b = [11.0, 13.0]
        x, y = solve_2x2(A, b)
        self.assertAlmostEqual(x, 7.1111111111, places=9)
        self.assertAlmostEqual(y, -3.2222222222, places=9)

    def test_singular_raises(self):
        A = [[1.0, 1.0],[2.0, 2.0]]  # det = 0
        b = [3.0, 6.0]
        with self.assertRaises(ValueError):
            solve_2x2(A, b)

if __name__ == "__main__":
    unittest.main()
