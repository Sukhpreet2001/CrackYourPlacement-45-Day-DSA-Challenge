from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       min_price=float('inf')
       max_profit=0

       for price in prices:
        if price< min_price:
            min_price=price

        profit=price-min_price

        if profit> max_profit:
            max_profit=profit
       return max_profit
    
# Testing

def run_tests():
   solution=Solution()

   #Test Case 1
   prices=[7,1,5,3,6,4]
   expected_output=5
   actual_output=solution.maxProfit(prices)
   print("Test Case 1:Expected Output:{expected_output} , Result:{actual_output}")
   print("Pass" if actual_output==expected_output else "Fail")

   #Test Case 2
   prices=[7,6,4,3,1]
   expected_output=0
   actual_output=solution.maxProfit(prices)
   print("Test Case 2:Expected Output:{expected_output} , Result:{actual_output}")
   print("Pass" if actual_output==expected_output else "Fail")

run_tests()