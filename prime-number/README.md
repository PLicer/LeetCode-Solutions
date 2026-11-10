# Prime Number

- **Platform:** gfg
- **Difficulty:** Easy
- **Link:** https://www.geeksforgeeks.org/problems/prime-number2314/1
- **Topics:** Math, Number Theory
- **Time complexity:** O(sqrt(n))
- **Space complexity:** O(1)

## Problem

Given a number `n`, determine whether it is a prime number or not. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

**Example**

- Input: `n = 7` → Output: `true` (7 has exactly two divisors: 1 and 7)

## Approach

Count the divisors by looping i from 1 to sqrt(n); each divisor i pairs with n/i, adding 2 (or 1 for a perfect square). A number is prime exactly when it has 2 divisors.

## Optimized approach

Instead of counting every divisor, return `False` as soon as one divisor is found
between 2 and sqrt(n). Worst case is still O(sqrt(n)), but composite numbers exit early.

```python
import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
```

## Solution

See [prime-number.py](prime-number.py)
