class Solution:
    def findMindiff(self, A, N, M):
        if M == 0 or M > N:
            return 0
        
        A = list(A)
        A.sort()
        
        min_diff = float('inf')
        for i in range(N - M + 1):
            current_diff = A[i + M - 1] - A[i]
            if current_diff < min_diff:
                min_diff = current_diff
        
        return min_diff

# Testing

def run_tests():
    solution = Solution()

    # Test Case 1
    A = [3, 4, 1, 9, 56, 7, 9, 12]
    N = 8
    M = 5
    expected_value = 6
    actual_value = solution.findMindiff(A, N, M)
    print(f"Test Case 1: Expected Value: {expected_value}, Actual Value: {actual_value}")
    print("Pass" if actual_value == expected_value else "Fail")

    # Test Case 2
    A = [7, 3, 2, 4, 9, 12, 56]
    N = 7
    M = 3
    expected_value = 2
    actual_value = solution.findMindiff(A, N, M)
    print(f"Test Case 2: Expected Value: {expected_value}, Actual Value: {actual_value}")
    print("Pass" if actual_value == expected_value else "Fail")

run_tests()
