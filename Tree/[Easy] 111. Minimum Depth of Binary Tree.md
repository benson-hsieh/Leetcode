| Category | Tree |
| :--- | :--- |
| **Subcategory** | Traversal |
| **Title** | [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/) |
| **Date** | 2026-04-10 |
| **Difficulty** | Easy |
| **Status** | Accepted |

---

## Description
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
## Approach: BFS
Finding the minimum depth is equivalent to finding the shortest path to a leaf node, which is best handled by BFS.

1. Level Initialization: Initialize depth starting at 1.

2. Queue Management: Use a Queue to traverse the tree level by level.

3. Leaf Detection: For each node in the current level:

    - Check if both left and right children are null.

    - If both are null, the current node is a leaf node. Return the current depth immediately as this is the shortest path.

4. Progression: If not a leaf, add existing children to the queue and increment depth after processing the entire level.

## Complexity Analysis
* **Time Complexity**: $O(N)$, where $N$ is the number of nodes. In the worst case (e.g., a skewed tree), we might visit all nodes. However, for a balanced tree, BFS can return much earlier than DFS.
* **Space Complexity**: $O(W)$, where $W$ is the maximum width of the tree. The queue stores at most the number of nodes at the widest level.

---


## Solution (Java)
```java
class Solution {
    public int minDepth(TreeNode root) {
        if(root == null) return 0;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        int depth = 1;
        while(!q.isEmpty()){
            int len = q.size();
            for(int i = 1; i <= len; i++){
                TreeNode cur = q.poll();
                if(cur.left != null) q.offer(cur.left);
                if(cur.right != null) q.offer(cur.right);
                if(cur.left == null && cur.right == null) return depth;
            }
            depth++;
        } 
        return depth;
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
