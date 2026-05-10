| Category | Tree |
| :--- | :--- |
| **Subcategory** | Traversal |
| **Title** | [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/) |
| **Date** | 2026-04-14 |
| **Difficulty** | Easy |
| **Status** | Accepted |

---

## Description
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

## Approach: DFS
The most efficient way to solve this is from the bottom up. We check the balance of subtrees while calculating their heights.

1. Helper Function: Define a getHeight function that returns the height of a node.

2. Unbalanced Flag: If any subtree is found to be unbalanced, return -1 immediately to signal the failure upwards.

3. Recursive Logic:

    - If the current node is null, height is 0.

    - Recursively get leftHeight and rightHeight.

    - If leftHeight == -1 or rightHeight == -1, return -1.

    - If Math.abs(leftHeight - rightHeight) > 1, return -1 (unbalanced).

    - Otherwise, return the actual height: Math.max(leftHeight, rightHeight) + 1.

4. Final Check: If the result of the root's getHeight is not -1, the tree is balanced.

## Complexity Analysis
* **Time Complexity**: $O(N)$, where $N$ is the number of nodes. Each node is visited exactly once in a post-order fashion.
* **Space Complexity**: $O(H)$, where $H$ is the height of the tree, representing the recursion stack depth. In the worst case (skewed tree), this is $O(N)$.

---

## Solution (Java)
```java
class Solution {
    public boolean isBalanced(TreeNode root) {
       return getHeight(root) != -1;
    }
    public int getHeight(TreeNode node){
        if(node == null) return 0;
        int left = getHeight(node.left);
        if(left == -1) return -1;
        int right = getHeight(node.right);
        if(right == -1) return -1;
        return Math.abs(left - right) > 1 ? -1 : Math.max(left, right) + 1;
    }
}
```
