| Category | Tree |
| :--- | :--- |
| **Subcategory** | Traversal |
| **Title** | [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/) |
| **Date** | 2026-03-31 |
| **Difficulty** | Medium |
| **Status** | Accepted |

---

## Description
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Approach: BFS
- Looking from the right side of the tree, the first node seen at each level is what is required.

- A variation of problem 102; the traversal method is the same.

- The first node seen at each level from the right side equals to the last node of each level.

- Therefore, just add the last node traversed in each level.

## Complexity Analysis
- **Time Complexity**: $O(N)$, where $N$ is the number of nodes in the tree, as each node is visited exactly once.
- **Space Complexity**: $O(D)$, where $D$ is the diameter of the tree. In the worst case (a perfect binary tree), the queue will hold $O(N)$ nodes at the leaf level.

---
## Solution (Java)
```java
class Solution {
    List<Integer> result = new ArrayList<Integer>();
    public List<Integer> rightSideView(TreeNode root) {       
        bfs(root);
        return result;
    }
    public void bfs(TreeNode node){
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        if(node == null) return;
        q.offer(node);
        while(!q.isEmpty()){
            int len = q.size();
            while(len > 0){
                TreeNode temp = q.poll();
                if(temp.left != null) q.offer(temp.left);
                if(temp.right != null) q.offer(temp.right);
                len--;
                if(len == 0) result.add(temp.val);
            }
        }
    }
}
```

   