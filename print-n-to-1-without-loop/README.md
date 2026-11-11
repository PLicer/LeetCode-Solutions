# Print n to 1 Without Loop

- **Platform:** gfg
- **Difficulty:** Easy
- **Link:** https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1
- **Topics:** Recursion
- **Time complexity:** O(n)
- **Space complexity:** O(n) recursion stack

## Problem

Print the numbers from `n` down to 1, space separated, without using loops.

**Example**

- Input: `n = 10` → Output: `10 9 8 7 6 5 4 3 2 1`

**Constraints:** 1 ≤ n ≤ 1000

## Approach

Print n first, then recurse on n-1. The base case n == 0 stops the recursion. Printing before the recursive call gives descending order from n down to 1.

## Solution

See [print-n-to-1-without-loop.py](print-n-to-1-without-loop.py)
