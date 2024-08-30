from typing import List
class Solution:
    def maxproduct(self,nums:List[int])->int:
        nums.sort()
        return max(nums[-1]*nums[0]*nums[1],nums[-1]*nums[-2]*nums[-3])

# testing
def run_tests():
    solution=Solution()

    #Test Case 1
    nums=[1,2,3]
    expected=6
    result=solution.maxproduct(nums)
    print(f"Test Case 1: Expected Value:{expected},Result:{result}")
    print("Pass" if result==expected else " Fail")

    #Test Case 
    nums=[1,2,3,4]
    expected=24
    result=solution.maxproduct(nums)
    print(f"Test Case 2: Expected Value: {expected} ,Result: {result} ")
    print("Pass" if result==expected else " Fail")

    #Test Case 3
    nums=[-1,-2,-3]
    expected=-6
    result=solution.maxproduct(nums)
    print(f"Test Case 3: Expected Value: {expected} ,Result: {result} ")
    print("Pass" if result==expected else " Fail")

run_tests()