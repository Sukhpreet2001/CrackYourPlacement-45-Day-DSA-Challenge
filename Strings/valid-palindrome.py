class Solution():
    def valid_palindrome(self,s:str)->bool:
        def is_palindrome(left:int,right:int)->bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True
        left=0
        right=len(s)-1

        while left< right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return is_palindrome(left+1,right) or is_palindrome(left, right-1)
        return True
    
# Testing
def run_tests():
    solution=Solution()

    # Test Case 1
    s="aba"
    exp_value=True
    result = solution.valid_palindrome(s)
    print(f"Test Case 1 : Expected Value:{exp_value} , Result: {result}")
    print("Pass" if result==exp_value else " Fail")

    # Test Case 2
    s="abca"
    exp_value=True
    result = solution.valid_palindrome(s)
    print(f"Test Case 2 : Expected Value:{exp_value} , Result: {result}")
    print("Pass" if result==exp_value else " Fail")

    # Test Case 3
    s="abc"
    exp_value=False
    result = solution.valid_palindrome(s)
    print(f"Test Case 3 : Expected Value:{exp_value} , Result: {result}")
    print("Pass" if result==exp_value else " Fail")

run_tests()