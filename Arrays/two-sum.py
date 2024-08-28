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

#Testing
def run_tests():
    solution=Solution()

    #Tset Case 1
    nums=[2,7,11,15]
    target=9
    expected_value=[0,1]
    actual_value=solution.twoSum(nums,target)
    print("Tset Case 1 : Expected Value:{expected_value},Result:{actual_value}")
    print("Pass" if actual_value==expected_value else "Fail")

    #Tset Case 2
    nums=[3,2,4]
    target=6
    expected_value=[1,2]
    actual_value=solution.twoSum(nums,target)
    print("Tset Case 2 : Expected Value:{expected_value},Result:{actual_value}")
    print("Pass" if actual_value==expected_value else "Fail")

    #Tset Case 3
    nums=[3,3]
    target=6
    expected_value=[0,1]
    actual_value=solution.twoSum(nums,target)
    print("Tset Case 2 : Expected Value:{expected_value},Result:{actual_value}")
    print("Pass" if actual_value==expected_value else "Fail")
    
run_tests() 