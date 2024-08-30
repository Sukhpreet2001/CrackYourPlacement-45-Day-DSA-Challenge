class Solution:
    def addbinary(self,a:str,b:str)->str:
        carry=0
        result=[]

        #pointers
        i=len(a)-1
        j=len(b)-1
        

        while i >=0 or j>=0 or carry:
            digit_a = int(a[i]) if i >=0 else 0
            digit_b = int(b[j]) if j >=0 else 0

            total= digit_a+digit_b+carry

            carry = total //2
            total_digit = total% 2

            result.append(str(total_digit))

            i-=1
            j-=1

        return ''.join(result[::-1])
    
#Testing

def run_tests():
    solution=Solution()

    # Test Case 1

    a="11"
    b="1"
    exp="100"
    res=solution.addbinary(a,b)
    print(f"Test Case 1: Expected Value:{exp},Result:{res}")
    print("Pass" if res==exp else " Fail")

    #Test Case 2
    a="1010"
    b="1011"
    exp="10101"
    res=solution.addbinary(a,b)
    print(f"Test Case 2: Expected Value:{exp},Result:{res}")
    print("Pass" if res==exp else " Fail")

run_tests()