from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          num_to_index = {}
          for i, num in enumerate(nums):
            diff = target - num
            if diff in num_to_index:
                return [num_to_index[diff], i]
            num_to_index[num] = i
          return []
    
#Test Cases
def run_tests():
    solution = Solution()

    # Test Case 1
    nums = [3,2,4]
    target = 6
    expected_output = [1,2]
    result = solution.twoSum(nums,target)
    print(f"Test Case 1 - Expected Output: {expected_output}, Result: {result}")
    print("Pass" if result == expected_output  else "Fail")

    # Test Case 2
    nums = [3,3]
    target = 6
    expected_output = [0,1]
    result = solution.twoSum(nums,target)
    print(f"Test Case 2 - Expected Output: {expected_output}, Result: {result}")
    print("Pass" if result == expected_output  else "Fail")

# Run the tests
run_tests()