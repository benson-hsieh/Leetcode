| Category | Tree |
| :--- | :--- |
| **Subcategory** | Traversal |
| **Title** | [404. Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/description/) |
| **Date** | 2026-04-01 |
| **Difficulty** | Medium |
| **Status** | Accepted |

---

## Description
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

## Approach: DFS
- Calculate the sum of all left leaves.

- Continuously call a traversal function and pass an extra boolean value to determine if it is a left or right node.

- Determine if there are child nodes; if there are none, it is a leaf, then return the value of the left leaf.

Note: The calling and returning method of this problem is similar to the Fibonacci sequence; there is no need to declare an additional global variable.

## Complexity Analysis
- **Time Complexity**: $O(N)$, where $N$ is the number of nodes in the binary tree, as each node is visited once.
- **Space Complexity**: $O(H)$, where $H$ is the height of the tree, representing the space used by the recursion stack.

---
## Solution (Java)
```java
class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        return sum(root, false);
    }
    public int sum(TreeNode node, boolean isLeft){
        if(node == null) return 0;
        if(node.right==null && node.left==null){
            return isLeft ? node.val : 0;
        }
        return sum(node.left, true) + sum(node.right, false);
    }
   
}
```

   