class Solution:
    def haystack_neeedle(self,haystack:str,needle:str)->int:
        return haystack.find(needle)
    
#Testing
def run_tests():
    solution=Solution()

    #Test Case 1
    haystack="sadbutsad"
    needle="sad"
    expected_value = 0
    result=solution.haystack_neeedle(haystack,needle)
    print(f"Test Case 1: Expected Value: {expected_value}, Result: {result}")
    print("Pass" if result==expected_value else " Fail")

    #Test Case 2
    haystack="leetcode"
    needle="leeto"
    expected_value=-1
    result=solution.haystack_neeedle(haystack,needle)
    print(f"Test Case 2: Expected Value: {expected_value}, Result: {result}")
    print("Pass" if result==expected_value else " Fail")

run_tests()