import unittest
from main import ShapeCalculator


class TestShapeCalculator(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(ShapeCalculator.circle_area(5), 78.53981633974483)

    def test_triangle_area(self):
        self.assertAlmostEqual(ShapeCalculator.triangle_area(3, 4, 5), 6.0)

    def test_is_right_triangle(self):
        self.assertTrue(ShapeCalculator.is_right_triangle(3, 4, 5))
        self.assertFalse(ShapeCalculator.is_right_triangle(2, 4, 5))


if __name__ == '__main__':
    unittest.main()
