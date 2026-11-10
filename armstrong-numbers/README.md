# Armstrong Numbers

- **Platform:** GeeksforGeeks
- **Difficulty:** Easy
- **Link:** https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
- **Topics:** Math
- **Time complexity:** O(d), where d is the number of digits (O(1) for a 3-digit number)
- **Space complexity:** O(1)

## Problem

You are given a 3-digit number `n`. Find whether it is an Armstrong number or not.
An Armstrong number of three digits is a number such that the sum of the cubes of
its digits is equal to the number itself. For example, 371 is an Armstrong number
since 3^3 + 7^3 + 1^3 = 371.

## Approach

Extract each digit with `n % 10`, add its cube to a running sum, drop the digit
with `n // 10`, and compare the sum with the original number.

## Solution

See [armstrong-numbers.py](armstrong-numbers.py)
