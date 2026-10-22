# DI String Match

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A permutation `perm` of `n + 1` integers of all the integers in the range `[0, n]` can be represented as a string `s` of length `n` where:

- s[i] == 'I' if perm[i] < perm[i + 1], and
- s[i] == 'D' if perm[i] > perm[i + 1].

Given a string `s`, reconstruct the permutation `perm` and return it. If there are multiple valid permutations perm, return **any of them**.

 

**Example 1:**

```
Input: s = "IDID"
Output: [0,4,1,3,2]

```

**Example 2:**

```
Input: s = "III"
Output: [0,1,2,3]

```

**Example 3:**

```
Input: s = "DDI"
Output: [3,2,0,1]

```

 

**Constraints:**

- 1 <= s.length <= 105
- s[i] is either 'I' or 'D'.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 79.36%)  
**Memory:** 19.4 MB (beats 100.00%)  
**Submitted:** 2026-10-22T13:08:11.714Z  

```py
class Solution(object):
    def diStringMatch(self, s):
        low, high = 0, len(s)
        result = []
        for c in s:
            if c == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        result.append(low)  # low == high
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/di-string-match/)