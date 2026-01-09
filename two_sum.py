"""
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
You may assume that each input has exactly one solution, and you may not use the same element twice.
The order of the output does not matter.
"""


class TwoSum:
    def __init__(self, array, target):
        self.array = array
        self.target = target

    def two_sum(self):
        index_dictionary = {}

        for i, value in enumerate(self.array):
            remainder = self.target - value

            if remainder in index_dictionary:
                return [index_dictionary[remainder], i]

            else:
                index_dictionary[value] = i

    def print_statement(self):
        result = self.two_sum()
        if result:
            print(f"The indices of the values that satisfy the target are: {result}")
        else:
            print("The target cannot be acquired with current array.")


def main():
    test_array = [3, 4, 5, 3]
    target = 6
    index_sum = TwoSum(test_array, target)
    index_sum.print_statement()


if __name__ == "__main__":
    main()
