"""
0-1 Knapsack Problem

Approach: Bottom Up

Explanation:

    1. first create a dp-table containing a capacity(c) - dp
    2. We fill this table with zeros initially.
    3. Then pick every element and do the following: item-i
       - iterate over all the possible places, starting from the capacity to -1, current_capacity
         - where the weight of the item is less than or equal to the currect_capacity.
         - calculate the max of 
           - ( item_value + dp[current_capacity - item_weight]) # This says if the item added to the previous capacity without it
           - dp[current_capacity] # Indicates that the weight here is already the largest
    4. Return the dp[capacity]

    - The outer loop iterates over the items (0 to n) # number of weights
    - The inner loop iterates over the weights (capacity) # total capacity 

Time Complexity: O(N.C) - We have two nested loops going over every item and the capacity table.
Space Complexity: O(C) - Single dp table with capacity+1 positions
"""
from typing import List

def calculate_knapsack_profit(capacity: int, weights: List, values: List):
    """
    Calculate the knapsack profit based on the capacity and weights/values.
    @param capacity: max capacity of the knapsack
    @param weights: weights of each items
    @param values: value of each item
    Space complexity : O(C)
    Time Complexity: O(N.C)
    """
    n = len(weights)
    dp = [0]*(capacity+1)

    for item_pos in range(n):
        item_weight = weights[item_pos]
        item_val = values[item_pos]
        for current_capacity in range(capacity, -1, -1):
            if weights[item_pos] <= current_capacity:
                dp[current_capacity] = max(item_val+ dp[current_capacity - item_weight],
                                           dp[current_capacity])
    return dp[capacity]


if __name__ == '__main__':
    # Example usage
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    calculate_knapsack_profit(capacity, weights, values)
    """
    Weights: [1, 2, 3, 5] values:[1, 5, 4, 8] and capacity: 6
    The item_pos value is :: 0 -->[0, 0, 0, 0, 0, 0, 0]
                    The current_capacity value is :: 6  -->[0, 0, 0, 0, 0, 0, 0]
                    The current_capacity value is :: 5  -->[0, 0, 0, 0, 0, 0, 1]
                    The current_capacity value is :: 4  -->[0, 0, 0, 0, 0, 1, 1]
                    The current_capacity value is :: 3  -->[0, 0, 0, 0, 1, 1, 1]
                    The current_capacity value is :: 2  -->[0, 0, 0, 1, 1, 1, 1]
                    The current_capacity value is :: 1  -->[0, 0, 1, 1, 1, 1, 1]
                    The current_capacity value is :: 0  -->[0, 1, 1, 1, 1, 1, 1]
    The item_pos value is :: 1 -->[0, 1, 1, 1, 1, 1, 1]
                    The current_capacity value is :: 6  -->[0, 1, 1, 1, 1, 1, 1]
                    The current_capacity value is :: 5  -->[0, 1, 1, 1, 1, 1, 6]
                    The current_capacity value is :: 4  -->[0, 1, 1, 1, 1, 6, 6]
                    The current_capacity value is :: 3  -->[0, 1, 1, 1, 6, 6, 6]
                    The current_capacity value is :: 2  -->[0, 1, 1, 6, 6, 6, 6]
                    The current_capacity value is :: 1  -->[0, 1, 5, 6, 6, 6, 6]
                    The current_capacity value is :: 0  -->[0, 1, 5, 6, 6, 6, 6]
    The item_pos value is :: 2 -->[0, 1, 5, 6, 6, 6, 6]
                    The current_capacity value is :: 6  -->[0, 1, 5, 6, 6, 6, 6]
                    The current_capacity value is :: 5  -->[0, 1, 5, 6, 6, 6, 10]
                    The current_capacity value is :: 4  -->[0, 1, 5, 6, 6, 9, 10]
                    The current_capacity value is :: 3  -->[0, 1, 5, 6, 6, 9, 10]
                    The current_capacity value is :: 2  -->[0, 1, 5, 6, 6, 9, 10]
                    The current_capacity value is :: 1  -->[0, 1, 5, 6, 6, 9, 10]
                    The current_capacity value is :: 0  -->[0, 1, 5, 6, 6, 9, 10]
    The item_pos value is :: 3 -->[0, 1, 5, 6, 6, 9, 10]
                    The current_capacity value is :: 6  -->[0, 1, 5, 6, 6, 9, 10]
                    The current_capacity value is :: 5  -->[0, 1, 5, 6, 6, 9, 10]
                    The current_capacity value is :: 4  -->[0, 1, 5, 6, 6, 9, 10]
                    The current_capacity value is :: 3  -->[0, 1, 5, 6, 6, 9, 10]
                    The current_capacity value is :: 2  -->[0, 1, 5, 6, 6, 9, 10]
                    The current_capacity value is :: 1  -->[0, 1, 5, 6, 6, 9, 10]
                    The current_capacity value is :: 0  -->[0, 1, 5, 6, 6, 9, 10]
    10
    """