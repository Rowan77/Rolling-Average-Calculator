# Rolling Average Project

This project contains a simple implementation of a function that calculates the rolling average of a list of numbers given a specified window size. It also includes a set of tests to ensure the function behaves as expected, covering various edge cases.

## Files in this Repository

- **`main.py`**: This file contains the `rolling_average` function that computes the rolling average of a given list with a specified window size.
- **`test_rolling_average.py`**: This file contains the `TestRollingAverage` class with a suite of tests to verify the correctness of the `rolling_average` function. It runs a variety of test cases to ensure the function handles normal, edge, and invalid input scenarios correctly.

## How to Run the Program

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
2. Navigate to the directory containing the files:
   ```bash
   cd <repository-directory>
3. Run the tests to verify functionality:
   ```bash
   python test_rolling_average.py
   
## Function Description

### `rolling_average(nums, k)`
This function computes the rolling average of the input list `nums` over a window size `k`.

- **Parameters**:
  - `nums` (list): A list of numerical values.
  - `k` (int): The size of the rolling window.
- **Returns**:
  - A list of rolling averages if inputs are valid.
  - An error message if inputs are invalid.
