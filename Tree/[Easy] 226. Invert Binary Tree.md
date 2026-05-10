| Category | Tree |
| :--- | :--- |
| **Subcategory** | Traversal |
| **Title** | [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/) |
| **Date** | 2026-04-27 |
| **Difficulty** | Easy |
| **Status** | Accepted |

---

## Description
Given the root of a binary tree, invert the tree, and return its root.

## Approach 1 : DFS
The tree is inverted by swapping the left and right subtrees of every node in a top-down manner.

1. Base Case: If the current node is null, return null.

2. Swap Logic: Use a temporary variable to swap the current node's left child and right child. (Because Java does not have swap function)

3. Recursive Step: Recursively call the function on the left child and then the right child.

4. Return: Return the original root after all levels have been processed.

## Approach 2 : BFS
Traverse the tree level by level and swap children as each node is visited.

1. Initialize a queue and add the root to begin the traversal.

2. While the queue is not empty, poll a node and swap its left and right children.

3. Add the non-null children of the current node to the queue.

4. Return the root once the queue is empty and all nodes have been processed.

## Complexity Analysis
* **Time Complexity**: $O(N)$, where $N$ is the number of nodes in the tree, as we must visit each node once to perform the swap.

* **Space Complexity**: 
    - DFS: $O(H)$, where $H$ is the height of the tree, representing the recursion stack.
    - BFS: $O(W)$, where $W$ is the maximum width of the tree, representing the queue size.

---

## Solution 1 (DFS in Java)
```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root == null) return root;
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }
}
```

## Solution 2 (BFS in Java)
```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root == null) return root;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while(!q.isEmpty()){
            int len = q.size();
            for(int i = 0; i < len; i++){
                TreeNode node = q.poll();
                TreeNode temp = node.left;
                node.left = node.right;
                node.right = temp;
                if(node.left != null) q.offer(node.left);
                if(node.right != null) q.offer(node.right);
            }
        }
        return root;
    }
}
```