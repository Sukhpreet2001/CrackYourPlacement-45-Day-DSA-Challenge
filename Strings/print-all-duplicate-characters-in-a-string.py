class Solution:
    def duplicate_char(self, s: str) -> list:
        unique_chars = set(s)
        duplicates = []

        for char in unique_chars:
            count = s.count(char)

            if count > 1:
                duplicates.append((char, count))

        return duplicates

# Testing 
def run_tests():
    solution = Solution()

    # Test Case 1
    s = "geeksforgeeks"
    expected_value = [('e', 4), ('g', 2), ('k', 2), ('s', 2)]
    result = solution.duplicate_char(s)
    
    # Sorting both lists to ensure the comparison is order-independent
    result.sort()
    expected_value.sort()

    print(f"Expected: {expected_value}, Result: {result}")
    print("Pass" if result == expected_value else "Fail")
    
    #Test CASE 2
    s = "test string"
    expected_value = [  ('s', 2),('t', 3)]
    result = solution.duplicate_char(s)
    
    # Sorting both lists to ensure the comparison is order-independent
    result.sort()
    expected_value.sort()

    print(f"Expected: {expected_value}, Result: {result}")
    print("Pass" if result == expected_value else "Fail")

run_tests()
