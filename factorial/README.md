# Factorial

- **Platform:** gfg
- **Difficulty:** Easy
- **Link:** https://www.geeksforgeeks.org/problems/factorial5739/1
- **Topics:** Recursion, Math
- **Time complexity:** O(n)
- **Space complexity:** O(n) recursion stack

## Problem

Given a positive integer `n`, find the factorial of `n`.

**Examples**

- Input: `n = 5` → Output: `120` (1 × 2 × 3 × 4 × 5 = 120)
- Input: `n = 4` → Output: `24` (1 × 2 × 3 × 4 = 24)

## Approach

Use n! = n * (n-1)!, with the base case 0! = 1. Each call multiplies n by the factorial of n-1 on the way back up.

## Optimized approach

An iterative loop computes the same result in O(n) time with O(1) extra space. It avoids the O(n) call stack and Python's recursion limit (about 1000). The standard library's math.factorial(n) does the same in one call.

```python
class Solution:
    def factorial(self, n: int) -> int:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
```

## Solution

See [factorial.py](factorial.py)
