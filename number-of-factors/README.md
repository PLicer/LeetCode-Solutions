# Number of Factors

- **Platform:** gfg
- **Difficulty:** Easy
- **Link:** https://www.geeksforgeeks.org/problems/number-of-factors1435/1
- **Topics:** Math, Number Theory
- **Time complexity:** O(sqrt(n))
- **Space complexity:** O(1)

## Problem

Given an integer `n`, find the number of factors (divisors) it has.

**Examples**

- Input: `n = 5` → Output: `2` (factors are 1 and 5)
- Input: `n = 25` → Output: `3` (factors are 1, 5 and 25)

**Constraints:** 1 ≤ n ≤ 10^5

## Approach

Divisors come in pairs (i, n/i), so loop i from 1 to sqrt(n). Each i that divides n adds 2 factors, or 1 when i equals n/i (a perfect square).

## Solution

See [number-of-factors.py](number-of-factors.py)
