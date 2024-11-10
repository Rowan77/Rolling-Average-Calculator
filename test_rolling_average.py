from main import rolling_average  # Import the rolling_average function

class TestRollingAverage:
    def __init__(self):
        self.run_tests()
        
    def test_invalid_inputs(self):
        result = rolling_average("not a list", 3)
        self.assertEqual(result, "Invalid input: nums must be a list and k must be an integer")
        result = rolling_average([1, 2, 3], "not an integer")
        self.assertEqual(result, "Invalid input: nums must be a list and k must be an integer")
    
    def assertEqual(self, result, expected):
        if result == expected:
            print(f"Test Passed: {result} == {expected}")
        else:
            print(f"Test Failed: {result} != {expected}")

    def test_large_window(self):
        result = rolling_average([1, 2, 3, 4], 5)
        self.assertEqual(result, [])

    def test_window_equal_to_list_length(self):
        result = rolling_average([1, 2, 3, 4], 4)
        self.assertEqual(result, [2.5])

    def test_single_element_window(self):
        result = rolling_average([10, 20, 30], 1)
        self.assertEqual(result, [10.0, 20.0, 30.0])

    def test_empty_list(self):
        result = rolling_average([], 3)
        self.assertEqual(result, [])

    def test_zero_window(self):
        result = rolling_average([1, 2, 3, 4], 0)
        self.assertEqual(result, [])

    def test_negative_window(self):
        result = rolling_average([1, 2, 3, 4], -1)
        self.assertEqual(result, [])

    def test_single_element_list(self):
        result = rolling_average([5], 1)
        self.assertEqual(result, [5.0])

    def test_all_elements_same(self):
        result = rolling_average([7, 7, 7, 7], 2)
        self.assertEqual(result, [7.0, 7.0, 7.0])

    def test_negative_numbers(self):
        result = rolling_average([-1, -2, -3, -4], 2)
        self.assertEqual(result, [-1.5, -2.5, -3.5])

    def test_mixed_positive_and_negative(self):
        result = rolling_average([5, -5, 10, -10], 2)
        self.assertEqual(result, [0.0, 2.5, 0.0])

    def test_floating_point_precision(self):
        result = rolling_average([1.5, 2.5, 3.5, 4.5], 2)
        self.assertEqual(result, [2.0, 3.0, 4.0])

    def test_zeros_in_list(self):
        result = rolling_average([0, 0, 0, 0], 2)
        self.assertEqual(result, [0.0, 0.0, 0.0])

    def test_large_window_and_large_list(self):
        nums = list(range(1, 10001))  # List from 1 to 10000
        result = rolling_average(nums, 10000)
        self.assertEqual(result, [5000.5])

    def test_large_values(self):
        result = rolling_average([10**9, 10**9, 10**9], 2)
        self.assertEqual(result, [1e9, 1e9])

    def test_single_element_large_window(self):
        result = rolling_average([10], 100)
        self.assertEqual(result, [])

    def run_tests(self):
        print("Running tests...")
        self.test_large_window()
        self.test_window_equal_to_list_length()
        self.test_single_element_window()
        self.test_empty_list()
        self.test_zero_window()
        self.test_negative_window()
        self.test_single_element_list()
        self.test_all_elements_same()
        self.test_negative_numbers()
        self.test_mixed_positive_and_negative()
        self.test_floating_point_precision()
        self.test_zeros_in_list()
        self.test_large_window_and_large_list()
        self.test_large_values()
        self.test_single_element_large_window()
        print("All tests completed.")

if __name__ == '__main__':
    TestRollingAverage()



