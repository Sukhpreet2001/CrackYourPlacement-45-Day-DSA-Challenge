from typing import List
class Solution:
    def long_common_prefix(self,strs:List[str])->str:
        prefix=strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix=prefix[:-1]

                if prefix=="":
                    return ""
        return prefix
    
#Testing
def run_tests():
    solution=Solution()

    #Test Case 1
    strs=["flower","flow","flight"]
    expected_value="fl"
    result=solution.long_common_prefix(strs)
    print(f"Test Case 1: Expected Value: {expected_value}, Result: {result}")
    print("Pass" if result==expected_value else " Fail")

    #Test Case 2
    strs=["dog","racecar","car"]
    expected_value=""
    result=solution.long_common_prefix(strs)
    print(f"Test Case 2: Expected Value: {expected_value}, Result: {result}")
    print("Pass" if result==expected_value else " Fail")

run_tests()