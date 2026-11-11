# 1 to n Without Loop

- **Platform:** gfg
- **Difficulty:** Easy
- **Link:** https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops3621/1
- **Topics:** Recursion
- **Time complexity:** O(n)
- **Space complexity:** O(n) recursion stack

## Problem

Given a positive integer `n`, print the numbers from 1 to `n` without using loops. Implement the function `printTillN()` so that it prints the numbers from 1 to `n` as space-separated integers.

**Example**

- Input: `n = 5` → Output: `1 2 3 4 5`

## Approach

Recurse on n-1 first, then print n. The recursion reaches the base case n == 0 and returns, and the prints happen on the way back up, so the numbers come out in increasing order from 1 to n.

## Solution

See [1-to-n-without-loop.py](1-to-n-without-loop.py)
