# Print GFG n times

- **Platform:** gfg
- **Difficulty:** Easy
- **Link:** https://www.geeksforgeeks.org/problems/print-gfg-n-times/1
- **Topics:** Recursion
- **Time complexity:** O(n)
- **Space complexity:** O(n) recursion stack

## Problem

Given a positive number `n`, print the string "GFG" exactly `n` times, separated by a single space.

**Example**

- Input: `n = 5` → Output: `GFG GFG GFG GFG GFG`

## Approach

Recurse on n-1 until n == 0, then print GFG on the way back. Each call prints one GFG, so it is printed n times in total.

## Optimized approach

A plain loop prints the same output in O(n) time with O(1) extra space. It avoids the O(n) call stack and Python's recursion limit (about 1000), which a recursive version can hit for large n.

```python
class Solution:
    def printGfg(self, n: int) -> None:
        for _ in range(n):
            print("GFG", end=" ")
```

## Solution

See [print-gfg-n-times.py](print-gfg-n-times.py)
