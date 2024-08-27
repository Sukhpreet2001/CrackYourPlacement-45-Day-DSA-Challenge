from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k=1
        for i in range(1,len(nums)):
            if nums[i] !=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k
#Testing
def run_tests():
    solution=Solution()
    #Test1
    nums=[1,1,2]
    expected_output=[1,2]
    k=solution.removeDuplicates(nums)
    actual_output=nums[:k]
    print(f"Test Case 1 - Expected Output: {expected_output}, Result: {actual_output}")
    print("Pass" if actual_output == expected_output  else "Fail")
    #Test2
    nums=[0,0,1,1,1,2,2,3,3,4]
    expected_output=[0,1,2,3,4]
    k=solution.removeDuplicates(nums)
    actual_output=nums[:k]
    print(f"Test Case 1 - Expected Output: {expected_output}, Result: {actual_output}")
    print("Pass" if actual_output == expected_output  else "Fail")

run_tests()