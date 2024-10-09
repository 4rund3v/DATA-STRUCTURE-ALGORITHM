"""
Problem: Sqrt(x)

    Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
    The returned integer should be non-negative as well.
    You must not use any built-in exponent function or operator.

Example 1:
    Input: x = 4
    Output: 2
    Explanation: The square root of 4 is 2, so we return 2.

Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:
0 <= x <= 2^31 - 1

Time Complexity: O(log x)
Space Complexity: O(1)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right

# Test cases
def test_mySqrt():
    solution = Solution()
    
    test_cases = [
        4,
        8,
        0,
        1,
        16,
        2147395600
    ]
    
    for case in test_cases:
        result = solution.mySqrt(case)
        print(f"Input: {case}, Output: {result}")

# Run the tests
test_mySqrt()