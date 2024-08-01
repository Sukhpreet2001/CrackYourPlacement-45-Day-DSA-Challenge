class Solution:
    def printDuplicateCharacters(self, s: str) -> None:
        char_count = {}
        
        # Count occurrences of each character
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Print characters with count greater than 1
        for char, count in char_count.items():
            if count > 1:
                print(f"{char}, count = {count}")

# Test Cases
def run_tests():
    solution = Solution()

    # Test Case 1
    s = "test string"
    print("Test Case 1 - Expected Output:")
    print("t, count = 3")
    print("s, count = 2")
    print("Result:")
    solution.printDuplicateCharacters(s)
    print()

    # Test Case 2
    s = "programming"
    print("Test Case 2 - Expected Output:")
    print("r, count = 2")
    print("g, count = 2")
    print("m, count = 2")
    print("Result:")
    solution.printDuplicateCharacters(s)
    print()

# Run the tests
run_tests()

