"""
Problem Statement: Combination Sum II
    Given an array of integers candidates (which may contain duplicates) and a target integer target,
    find all unique combinations in candidates where the candidate numbers sum to target.
    Each number in candidates may only be used once in the combination.

    Note: The solution set must not contain duplicate combinations.

Time Complexity: O(2^n), where n is the number of candidates.
    In the worst case, we might need to explore all possible subsets.

Space Complexity: O(n), where n is the number of candidates.
    This accounts for the recursion stack and the space to store combinations.

Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: 
    [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
    ]

Example 2:
    Input: candidates = [2,5,2,1,2], target = 5
    Output: 
    [
    [1,2,2],
    [5]
    ]

Visual Representation of the Decision Tree:
For candidates [1,1,2,2,5] and target 5, the decision tree would look like this:

               []
        /    /    \    \
      [1]  [1]   [2]  [5]
     /  \    |    |
 [1,1] [1,2] [1,2] [2,2]
   |     |     |    |
[1,1,2] [1,2,2] [1,2,2] [2,2,1]

Valid combinations: [1,2,2] and [5]

"""

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(start: int, target: int, path: list[int]):
            # Base case: if target is 0, we've found a valid combination
            if target == 0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same level to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # If the current candidate is greater than the target, we can stop
                # (since the array is sorted, all subsequent numbers will be larger)
                if candidates[i] > target:
                    break
                
                # Include the current candidate and continue exploring
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()  # Backtrack: remove the last added candidate

        candidates.sort()  # Sort to handle duplicates and enable pruning
        result = []
        backtrack(0, target, [])
        return result

# Example usage:
solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
print(solution.combinationSum2([2,5,2,1,2], 5))
# Output: [[1,2,2],[5]]