import unittest
from src.triangle.triangle import Triangle


class TestTriangle:
    def test_valid_equilateral_triangle(self):
        assert Triangle(5, 5, 5).is_triangle()

    def test_valid_isosceles_triangle(self):
        assert Triangle(4, 4, 3).is_triangle()

    def test_valid_scalene_triangle(self):
        assert Triangle(3, 4, 5).is_triangle()

    def test_invalid_triangle_all_sides_zero(self):
        assert not Triangle(0, 0, 0).is_triangle()

    def test_invalid_triangle_one_side_equals_sum_of_other(self):
        assert not Triangle(3, 4, 7).is_triangle()

    def test_invalid_triangle_negative_sides(self):
        assert not Triangle(-1, -2, -3).is_triangle()

    def test_invalid_triangle_one_side_zero(self):
        assert not Triangle(0, 5, 10).is_triangle()

    def test_invalid_triangle_shortest_sides_sum_greater_than_longest_side(self):
        assert not Triangle(1, 1, 3).is_triangle()
