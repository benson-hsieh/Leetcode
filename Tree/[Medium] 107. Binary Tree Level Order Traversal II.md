| Category | Tree |
| :--- | :--- |
| **Subcategory** | Traversal |
| **Title** | [107. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description) |
| **Date** | 2026-03-31 |
| **Difficulty** | Medium |
| **Status** | Accepted |

---

## Description
Given the `root` of a binary tree, return the *bottom-up* level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

## Approach: DFS
This problem is **highly similar to LeetCode 102**. The only difference is the order of the levels in the final result.

Just reverse the result before returning it.

- Java: Collections.reverse();

## Complexity Analysis
- **Time Complexity**: $O(N)$, where $N$ is the number of nodes. We visit each node once, and reversing the outer list takes $O(H)$ time, which is less than $O(N)$.
- **Space Complexity**: $O(N)$ to store the nodes in the result and the queue.

---
## Solution (Java)
```java
class Solution {    
    List<List<Integer>> result = new ArrayList<List<Integer>>();  
    public List<List<Integer>> levelOrder(TreeNode root) {
        dfs(root, 0);
        Collections.reverse(result);
        return result;
    }
    public void dfs(TreeNode root, int depth){
        if(root == null) return;
        if(result.size() == depth){
            result.add(new ArrayList<Integer>());
        }
        result.get(depth).add(root.val);
        dfs(root.left, depth + 1);
        dfs(root.right, depth + 1);
    }
}
```

   