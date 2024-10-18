## Dynamic Programming

Dynamic programming

  - Optimal substructure , i.e. the solution to a smaller problem helps solve the larger problem.
  - Reducing the time complexity of an recursive ( exponential / factorial ) time to  polynomial time complexity
  - This is acheived by using one of the two below approaches.
    - Top down approach : 
    	An **recursive approach** that stores the results of the redundant function calls to avoid repeating calculations of the same subproblems.
    	Basically cache the results to be used later on.
    - Bottom up approach 
    	An **iterative approach** that systematically fills a table with results of the subproblems to solve larger problems efficiently.

    ### Top Down Approach
    The top-down approach is called as **memoization**.
    Steps:
    - Create a lookup table, fill it with the n+1, -1 values
    - as you go about in the recursion,
    - Check if the value is filled in,
    - Else fill it in as you solve it.

    ### Bottom Up Approach
    The bottom-up approach is called as **tabulation**
    Steps:
     - Solves the basic/fundamental problem and stores the result
     - Stores the solution at each step in a table for lookups.
     - Then goes about itteratively to solve the problem( smaller to larger)

#### Intuition:
  - Does the problem given - have a overlapping subproblem? i.e. can we use the results of a subproblem to solve another?
  - Does the problem have a optimal substructure? i.e can the final solution be constructed using the optimal solutions of its subproblems.


#### Problems Solved:
 - 0/1 Knapsack
 - Coin Change
 - Nth Tribonacci Number
 - Partition equal subset
 - Counting Bits
 - 01 Matrix
 - House Robber
 - House Robber 2
 - Maximum product subarray 
 - Combination Sum
 - Word Break
 - Palindromic Substrings
 - Longest common subsequence
 - Word Break 2
 - Decode Ways
 - Count number of good subsequences
 - Climbing Stairs


#### Examples of problems solved:
Some examples of problems solved using the dp approach is 
  - Pascals Triange
  - Maximam matching genetic code
