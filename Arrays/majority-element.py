from typing import List

class Solution():
    def maj_element(self,nums:List[int])->int:
        n=len(nums)/2
        a=list(set(nums))

        for i in a :
            c=nums.count(i)
            if c>n:
                return i
            
#Testing
def run_tests():
    solution=Solution()

    #Test Case 1

    nums=[3,2,3]
    expected_value=3
    result=solution.maj_element(nums)
    print("Test Case 1 : Expected Value{expected_value}, Result:{result}")
    print("Pass" if result==expected_value else " Fail")

    #Test Case 2

    nums=[2,2,1,1,1,2,2]
    expected_value=2
    result=solution.maj_element(nums)
    print("Test Case 1 : Expected Value{expected_value}, Result:{result}")
    print("Pass" if result==expected_value else " Fail")

run_tests()