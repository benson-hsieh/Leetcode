| Category | Tree |
| :--- | :--- |
| **Subcategory** | Traversal |
| **Title** | [100. Same Tree](https://leetcode.com/problems/same-tree/description/) |
| **Date** | 2026-05-08 |
| **Difficulty** | Easy |
| **Status** | Accepted |

---

## Description
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
## Approach: DFS
The comparison is handled by evaluating three conditions at each node level:

1. Identical Base Case: If both nodes p and q are null, they are identical, so return true.

2. Difference Detection: If only one of the nodes is null, or if their values (val) differ, the trees are not identical, so return false.

3. Recursive Verification: If the current nodes match, recursively check if both the left subtrees and right subtrees are also identical using the && operator.
## Complexity Analysis
* **Time Complexity**: $O(N)$, where $N$ is the number of nodes in the binary tree, as each node is visited once.
* **Space Complexity**: $O(H)$, where $H$ is the height of the tree, representing the space used by the recursion stack.

---

## Solution (Java)
```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null) return true;
        if(p == null || q == null || p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
```
