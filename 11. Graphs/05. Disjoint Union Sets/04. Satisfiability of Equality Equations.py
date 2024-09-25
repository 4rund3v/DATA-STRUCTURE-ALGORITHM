"""
Problem Statement:
    You are given an array of strings 'equations' that represent relationships between variables 
    where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".
    
    Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.
    Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, 
    or false otherwise.

Constraints:
    * 1 <= equations.length <= 500
    * equations[i].length == 4
    * equations[i][0] is a lowercase letter.
    * equations[i][1] is either '=' or '!'.
    * equations[i][2] is '='.
    * equations[i][3] is a lowercase letter.

Time Complexity:    The time complexity is O(n * α(n)), where n is the number of equations and α is the inverse Ackermann function.
                    We iterate through the equations twice, each time performing either a union or find operation.
                    Both union and find operations, with path compression and union by rank, have an amortized time complexity of O(α(n)), which is effectively constant time for all practical values of n.
                    Therefore, the overall time complexity is O(n * α(n)), which is nearly linear.

Space Complexity: O(1), as we always use a fixed-size array of 26 elements for parent and rank.
"""

class Solution:
    def __init__(self):
        self.parent = []
        self.rank = []
    
    def find(self, i):
        # Path compression: make each node point directly to the root
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        # Union by rank: attach smaller rank tree under root of higher rank tree
        p_x = self.find(x)
        p_y = self.find(y)
        
        if p_x != p_y:
            if self.rank[p_x] > self.rank[p_y]:
                self.parent[p_y] = p_x
            elif self.rank[p_y] > self.rank[p_x]:
                self.parent[p_x] = p_y
            else:
                self.parent[p_x] = p_y
                self.rank[p_y] += 1
    
    def equationsPossible(self, equations):
        # Initialize each variable (a to z) as its own parent
        self.parent = list(range(26))
        self.rank = [1] * 26
        
        # First pass: process all equality equations
        for eq in equations:
            if eq[1] == '=':
                # using ord () as we are storing int values in parent and rank 
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                self.union(x, y)
        
        # Second pass: check if any inequality equation is violated
        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                if self.find(x) == self.find(y):
                    return False  # Contradiction found
        
        return True  # No contradictions

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    equations1 = ["a==b", "b!=a"]
    print("Example 1 output:", solution.equationsPossible(equations1))  # False
    
    # Example 2
    equations2 = ["b==a", "a==b"]
    print("Example 2 output:", solution.equationsPossible(equations2))  # True