"""
Sort Array by Increasing Frequency

    Given an array of integers `nums`, sort the array in increasing order based on the frequency of the values. 
    If multiple values have the same frequency, sort them in decreasing order.
    Return the sorted array.

Example 1:
    Input: nums = [1,1,2,2,2,3]
    Output: [3,1,1,2,2,2]
    Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:
    Input: nums = [2,3,1,3,2]
    Output: [1,3,3,2,2]
    Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:
    Input: nums = [-1,1,-6,4,5,-6,1,4,1]
    Output: [5,-1,4,4,-6,-6,1,1,1]

Constraints:
    * 1 <= nums.length <= 100
    * -100 <= nums[i] <= 100

Time Complexity: O(n log k), where n is the number of elements in nums and k is the number of unique elements.
Space Complexity: O(n)
"""

from typing import List
from collections import Counter
import heapq

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        minHeap = []
        result = []
        
        # Push items to the heap with (frequency, -num) as the key
        # This ensures increasing frequency and decreasing value order
        for num, freq in counter.items():
            heapq.heappush(minHeap, (freq, -num))
        
        while minHeap:
            freq, neg_num = heapq.heappop(minHeap)
            num = -neg_num  # Convert back to the original number
            result.extend([num] * freq)
        
        return result

# Example usage
solution = Solution()

nums1 = [1,1,2,2,2,3]
print(f"Example 1: {solution.frequencySort(nums1)}")  # Expected output: [3,1,1,2,2,2]

nums2 = [2,3,1,3,2]
print(f"Example 2: {solution.frequencySort(nums2)}")  # Expected output: [1,3,3,2,2]

nums3 = [-1,1,-6,4,5,-6,1,4,1]
print(f"Example 3: {solution.frequencySort(nums3)}")  # Expected output: [5,-1,4,4,-6,-6,1,1,1]