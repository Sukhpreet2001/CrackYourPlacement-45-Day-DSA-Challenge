from typing import List

class Solution:
    def merge_sort(self, nums1: List[int], m: int, nums2: List[int], n: int):
        # pointers
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are still elements in nums2, add them to nums1
        nums1[:p2 + 1] = nums2[:p2 + 1]

# Testing
def run_tests():
    solution = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    expected_value = [1, 2, 2, 3, 5, 6]
    
    solution.merge_sort(nums1, m, nums2, n)
    print(f"Test Case 1 - Expected Value: {expected_value}, Actual Value: {nums1}")
    print("Pass" if nums1 == expected_value else "Fail")

    # Test Case 2
    nums1 = [1]
    nums2 = []
    m = 1
    n = 0
    expected_value = [1]
    
    solution.merge_sort(nums1, m, nums2, n)
    print(f"Test Case 2 - Expected Value: {expected_value}, Actual Value: {nums1}")
    print("Pass" if nums1 == expected_value else "Fail")

    # Test Case 3
    nums1 = []
    nums2 = [1]
    m = 0
    n = 1
    expected_value = [1]
    
    solution.merge_sort(nums1, m, nums2, n)
    print(f"Test Case 3 - Expected Value: {expected_value}, Actual Value: {nums1}")
    print("Pass" if nums1 == expected_value else "Fail")

run_tests()
