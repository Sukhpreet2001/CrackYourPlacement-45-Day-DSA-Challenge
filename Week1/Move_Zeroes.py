from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l= 0
        for r in range(len(nums)):
            if nums[r] :
                nums[l],nums[r]=nums[r],nums[l]
                l +=1 
        return nums
#Test Cases
def run_tests():
    solution = Solution()

    # Test Case 1
    nums = [0,1,0,3,12]
    expected_output = [1,3,12,0,0]
    result = solution.moveZeroes(nums)
    print(f"Test Case 1 - Expected Output: {expected_output}, Result: {result}")
    print("Pass" if result == expected_output  else "Fail")

    # Test Case 2
    nums = [0]
    expected_output = [0]
    result = solution.moveZeroes(nums)
    print(f"Test Case 2 - Expected Output: {expected_output}, Result: {result}")
    print("Pass" if result == expected_output  else "Fail")

# Run the tests
run_tests()
