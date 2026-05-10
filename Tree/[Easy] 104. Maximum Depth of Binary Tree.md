| Category | Tree |
| :--- | :--- |
| **Subcategory** | |
| **Title** | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/) |
| **Date** | 2026-05-10 |
| **Difficulty** | Easy |
| **Status** | Accepted |

---

## Description
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


## Approach 1 : BFS
Traverse the tree level by level and count the number of levels.

1. Level Counting: Increment a depth counter each time we begin processing a new level in the queue.

2. Full Traversal: Unlike minimum depth, we must traverse until the queue is empty to ensure we've reached the farthest leaf.

## Approach 2 : DFS
The maximum depth of a tree is 1 plus the maximum depth of its tallest subtree.

1. Base Case: If the node is null, its depth is 0.

2. Recursive Step: Calculate the depth of the left and right subtrees.

3. Return: The result is Math.max(leftDepth, rightDepth) + 1.

## Complexity Analysis
* **Time Complexity**: $O(N)$, where $N$ is the number of nodes in the tree, as each node is visited exactly once.
* **Space Complexity**: 
    - DFS: $O(H)$, where $H$ is the height of the tree (representing the recursion stack). In the worst case of a skewed tree, $H = N$.
    - BFS: $O(W)$, where $W$ is the maximum width of the tree (representing the queue size).

---



## Solution (Java)
## BFS
```java
class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null) return 0;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        int depth = 0 ;
        while(!q.isEmpty()){
            depth++;
            int len = q.size();
            for(int i = 1; i <= len; i++){
                TreeNode cur = q.poll();
                if(cur.left != null) q.offer(cur.left);
                if(cur.right != null) q.offer(cur.right);
            }
        }
        return depth;
    }
}

```
## DFS
```java
class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null) return 0;
        int maxLeft = maxDepth(root.left);
        int maxRight = maxDepth(root.right);
        return Math.max(maxLeft, maxRight) + 1;
    }
}
```

## ⚡ Comparison: 104 (Max Depth) vs. 111 (Min Depth)

While the BFS templates for these two problems are nearly identical, there are critical logical differences:

| Feature | 104. Maximum Depth | 111. Minimum Depth |
| :--- | :--- | :--- |
| **Goal** | Find the **longest** path to any leaf. | Find the **shortest** path to the nearest leaf. |
| **BFS Termination** | Must process **every level** until the queue is empty. | Can perform an **Early Return** as soon as the first leaf is found. |
| **Leaf Definition** | The end of the longest branch. | A node where `left == null && right == null`. |
| **Skewed Tree Case** | If a node has only one child, the max depth is simply $1 + \text{depth of that child}$. | **Critical Trap**: If a node has only one child, the min depth is **NOT** 1. You must proceed to the actual leaf node. |