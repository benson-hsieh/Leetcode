| Category | Tree |
| :--- | :--- |
| **Subcategory** | Traversal |
| **Title** | [515. Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/) |
| **Date** | 2026-04-01 |
| **Difficulty** | Medium |
| **Status** | Accepted |

---

## Description
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
## Approach: BFS
This problem follows the same template as Problem 102, with an added step to track the maximum value per level.

1. Level Initialization: For each level, initialize a variable max to store the largest value found so far. You can initialize it with the value of the first node in the current queue (q.peek().val).

2. Level Traversal: Iterate through all nodes in the current level.

3. Maximum Comparison: For each node, compare its value with the current max. Update max if the node's value is greater than or equal to the current max.

4. Queue Children: Add the left and right children of the current node to the queue for the next level's processing.

5. Store Result: After traversing all nodes in the current level, add the max value to the result list.
## Complexity Analysis
* **Time Complexity**: $O(N)$, where $N$ is the total number of nodes in the binary tree. We visit each node exactly once.
* **Space Complexity**: $O(W)$, where $W$ is the maximum width of the tree. The queue stores at most the number of nodes in the widest level.

---

## Solution (Java)
```java
class Solution {
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if(root == null) return result;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        while(!q.isEmpty()){
            int len = q.size();
            int max = q.peek().val;
            for(int i = 1; i <= len; i++){
                TreeNode temp = q.poll();
                if(temp.val >= max) max = temp.val;
                if(temp.left != null) q.offer(temp.left);
                if(temp.right != null) q.offer(temp.right);
            }
            result.add(max);
        }
        return result;
    }
}
```
