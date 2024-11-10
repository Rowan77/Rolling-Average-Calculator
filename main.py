def rolling_average(nums, k):     
    """
    Compute the rolling average of a list of numbers using a specified window size.

    Parameters:
    nums (list): A list of numerical values.
    k (int): The size of the rolling window.

    Returns:
    list: A list of rolling averages for each window.
    
    """

    # Exclude edge cases for invalid window size
    if k <= 0 or k > len(nums):  
        return []
    
    # Create a list to store the computed averages
    result = []
    
    # Calculate the sum and average for the first window
    current_sum = sum(nums[:k])
    result.append(current_sum / k)
    
    # Update the sum and averages for subsequent windows
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        result.append(current_sum / k)
        
    return result
