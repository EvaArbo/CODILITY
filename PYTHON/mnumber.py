#Given a list containing n distinct numbers from 0 to n, find the missing number.

#Input: [3, 0, 1]

#Output: 2

def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example usage:
print(find_missing_number([3, 0, 1]))  # Output: 2
print(find_missing_number([0, 1, 2, 4, 5]))  # Output: 3
print(find_missing_number([1, 2, 3, 4, 5]))  # Output: 0 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     