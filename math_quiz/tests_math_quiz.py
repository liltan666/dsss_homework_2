import unittest
from math_quiz import generate_random_number, select_random_operator, generate_problem_and_answer

class TestMathGame(unittest.TestCase):
    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_select_random_operator(self):
        # Test if the operator selected is one of the specified operators
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of selections
            op = select_random_operator()
            self.assertIn(op, operators)

    def test_generate_problem_and_answer(self):
        # Test different arithmetic operations
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
            (7, 0, '*', '7 * 0', 0)  # Test multiplication by zero
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_problem_and_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
