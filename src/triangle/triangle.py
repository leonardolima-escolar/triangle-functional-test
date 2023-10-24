class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_triangle(self):
        return self.__satisfies_triangle_inequality()

    def triangle_type(self):
        if not self.is_triangle():
            return "Not a triangle"
        if self.side1 == self.side2 == self.side3:
            return "Equilateral Triangle"
        if (
            self.side1 == self.side2
            or self.side2 == self.side3
            or self.side1 == self.side3
        ):
            return "Isosceles Triangle"
        return "Scalene Triangle"

    def __satisfies_triangle_inequality(self):
        return (
            self.side1 + self.side2 > self.side3
            and self.side1 + self.side3 > self.side2
            and self.side2 + self.side3 > self.side1
        )

    # def __are_positive_sides(self):
    #     return self.side1 > 0 and self.side2 > 0 and self.side3 > 0

    # def __each_side_shorter_than_half_sum(self):
    #     half_sum = (self.side1 + self.side2 + self.side3) / 2
    #     return self.side1 < half_sum and self.side2 < half_sum and self.side3 < half_sum

    # def __one_side_equals_sum_of_other(self):
    #     sides = [self.side1, self.side2, self.side3]
    #     a, b, c = sorted(sides)
    #     return a + b > c
