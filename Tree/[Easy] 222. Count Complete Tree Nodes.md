| Category | Tree |
| :--- | :--- |
| **Subcategory** | Traversal |
| **Title** | [222. Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/description/) |
| **Date** | 2026-04-16 |
| **Difficulty** | Easy |
| **Status** | Accepted |

---

## Description
Given the root of a complete binary tree, return the number of the nodes in the tree.

Complete binary tree: every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible.

## Approach 1 : BFS 
Traverse the tree level by level and count each node visited.

1. Initialize a count variable to 0.

2. Use a queue to perform a standard level-order traversal.

3. For every node dequeued, increment the count.

4. Add the children of each node to the queue until it is empty.

## Approach 2 : DFS
Calculate the total number of nodes by recursively counting the subtrees.

1. Base Case: If the node is null, its count is 0.

3. Recursive Step: Recursively calculate the node counts of the left and right subtrees.

3. Return: The total count is countNodes(left) + countNodes(right) + 1.

## Complexity Analysis
* **Time Complexity**: $O(N)$, where $N$ is the number of nodes in the tree, as each node is visited exactly once.
* **Space Complexity**: 

    - BFS: $O(W)$, where $W$ is the maximum width of the tree (representing the queue size).
    - DFS: $O(H)$, where $H$ is the height of the tree (representing the recursion stack). For a complete tree, $H = \log N$.
    
---

## Solution 1 (BFS in Java)
```java
class Solution {
    public int countNodes(TreeNode root) {
        if(root == null) return 0;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        int count = 0;
        while(!q.isEmpty()){
            int len = q.size();
            for(int i = 1; i <= len; i++){
                TreeNode node = q.poll();
                count++;
                if(node.left != null) q.offer(node.left);
                if(node.right != null) q.offer(node.right);
            }
        }
        return count;
    }
}
```

## Solution 2 (DFS in Java)
```java
class Solution {
    public int countNodes(TreeNode root) {
        if(root == null) return 0;
        return countNodes(root.left) + countNodes(root.right) + 1;
    }
}
```
