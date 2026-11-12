# Sum of Natural Number Cubes

- **Platform:** gfg
- **Difficulty:** Easy
- **Link:** https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1
- **Topics:** Recursion, Math
- **Time complexity:** O(n)
- **Space complexity:** O(n) recursion stack

## Problem

Given an integer `n`, calculate the sum of the series 1³ + 2³ + 3³ + 4³ + … up to the n-th term.

**Examples**

- Input: `n = 5` → Output: `225` (1³ + 2³ + 3³ + 4³ + 5³ = 225)
- Input: `n = 7` → Output: `784` (1³ + 2³ + … + 7³ = 784)

## Approach

The sum of cubes up to n is n^3 plus the sum of cubes up to n-1. Recurse down to the base case n == 1, which returns 1, and add each cube on the way back.

## Optimized approach

The sum of the first n cubes has a closed form: (n(n+1)/2)^2, the square of the n-th triangular number. This gives the answer in O(1) time and O(1) space, with no recursion depth limit to worry about.

```python
class Solution:
    def sumOfSeries(self, n: int) -> int:
        return (n * (n + 1) // 2) ** 2
```

## Solution

See [sum-of-natural-number-cubes.py](sum-of-natural-number-cubes.py)
