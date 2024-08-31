from typing import List
class Solution:
    def productarray(self,nums:List[int])->List[int]:
        n=len(nums)

        result=[1]*n

        prefix=1
        for i in range(n):
            result[i]=prefix
            prefix*=nums[i]

        suffix=1
        for i in range(n-1,-1,-1):
            result[i]*=suffix
            suffix*=nums[i]

        return result
    
#Testing
def run_tests():
    solution=Solution()

    #Test Case 1
    nums=[10, 3, 5, 6, 2]
    exp=[180, 600, 360, 300, 900]
    res=solution.productarray(nums)
    print(f"Expected Value:{exp}, Result:{res}")
    print("Pass" if res==exp else " Fail")

    #Test Case 2
    nums=[12,0]
    exp=[0,12]
    res=solution.productarray(nums)
    print(f"Expected Value:{exp}, Result:{res}")
    print("Pass" if res==exp else " Fail")

run_tests()