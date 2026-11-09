# Minimum Depth of Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

 **Note:**  A leaf is a node with no children.

 

 **Example 1:** 

```
Input: root = [3,9,20,null,null,15,7]
Output: 2

```

 **Example 2:** 

```
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 105].
- -1000 <= Node.val <= 1000

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 85.50%)  
**Memory:** 44.3 MB (beats 82.01%)  
**Submitted:** 2026-11-09T16:43:13.598Z  

```py
from collections import deque

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        queue = deque([root])
        minLevel = 1

        while queue:
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                if node.left is None and node.right is None:
                    return minLevel

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            minLevel += 1

        return minLevel
# end
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/)