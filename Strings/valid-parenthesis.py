class Solution:
    def valid_parenthesis(self,s:str)->bool:
        stack=[]

        mapping={")":"(","}":"{","]":"["}

        for char in s:
            if char in mapping:
                top_element=stack.pop() if stack else "#"

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
    
#Testing

def run_tests():
    solution=Solution()

    #Test Case 1
    s="()"
    expected_value=True
    actual_value=solution.valid_parenthesis(s)
    print("Tset Case 1 : Expected Value:{expected_value}, Result:{actual_value}")
    print("Pass" if actual_value==expected_value else " Fail")

    #Test Case 2
    s="()[]{}"
    expected_value=True
    actual_value=solution.valid_parenthesis(s)
    print("Tset Case 2 : Expected Value:{expected_value}, Result:{actual_value}")
    print("Pass" if actual_value==expected_value else " Fail")

    #Test Case 3
    s="(]"
    expected_value=False
    actual_value=solution.valid_parenthesis(s)
    print("Tset Case 3 : Expected Value:{expected_value}, Result:{actual_value}")
    print("Pass" if actual_value==expected_value else " Fail")

    #Test Case 4
    s="([])"
    expected_value=True
    actual_value=solution.valid_parenthesis(s)
    print("Tset Case 4 : Expected Value:{expected_value}, Result:{actual_value}")
    print("Pass" if actual_value==expected_value else " Fail")

run_tests()