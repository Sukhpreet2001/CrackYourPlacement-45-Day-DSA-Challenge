class Solution:
    def excelsheet(self,columnNumber:int)->str:
        result=[]

        while columnNumber >0:
            columnNumber -= 1

            result.append(chr(columnNumber%26+ord('A')))

            columnNumber //=26

        return ''.join(result[::-1])
    
#Testing 

def run_tests():
    solution = Solution()

    #Test Case 1
    columnNumber=1
    exp="A"
    res=solution.excelsheet(columnNumber)
    print(f"TesT Case 1: Expected Value:{exp},Result:{res} ")
    print("Pass" if res==exp else "Fail")

    #Test Case 2
    columnNumber=28
    exp="AB"
    res=solution.excelsheet(columnNumber)
    print(f"TesT Case 2: Expected Value:{exp},Result:{res} ")
    print("Pass" if res==exp else "Fail")

    #Test Case 3
    columnNumber=701
    exp="ZY"
    res=solution.excelsheet(columnNumber)
    print(f"TesT Case 3: Expected Value:{exp},Result:{res} ")
    print("Pass" if res==exp else "Fail")

run_tests()
