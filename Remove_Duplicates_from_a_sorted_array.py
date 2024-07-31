from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l]=nums[r]
                l +=1
        return l
    
#Test Cases
def run_tests():
    solution = Solution()

    # Test Case 1
    nums = [1, 1, 2]
    expected_output = 2
    expected_nums = [1, 2]
    result = solution.removeDuplicates(nums)
    print(f"Test Case 1 - Expected Output: {expected_output}, Result: {result}")
    print(f"Expected Nums: {expected_nums}, Resulting Nums: {nums[:result]}")
    print("Pass" if result == expected_output and nums[:result] == expected_nums else "Fail")

    # Test Case 2
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_output = 5
    expected_nums = [0, 1, 2, 3, 4]
    result = solution.removeDuplicates(nums)
    print(f"Test Case 2 - Expected Output: {expected_output}, Result: {result}")
    print(f"Expected Nums: {expected_nums}, Resulting Nums: {nums[:result]}")
    print("Pass" if result == expected_output and nums[:result] == expected_nums else "Fail")

# Run the tests
run_tests()
