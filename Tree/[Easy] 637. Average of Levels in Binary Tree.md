| Category | Tree |
| :--- | :--- |
| **Subcategory** | Traversal |
| **Title** | [637. Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/description/) |
| **Date** | 2026-04-01 |
| **Difficulty** | Easy |
| **Status** | Accepted |

---

## Description
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
## Approach: BFS
This problem is a variation of Level Order Traversal (Problem 102). Instead of storing all node values of a level, we calculate their average.

1. Level Traversal: Use a Queue to perform BFS level by level.

2. Summation: For each level, record the current queue size (len). Iterate through all nodes in that level, adding their values to a double sum.

3. Average Calculation: Divide the sum by the number of nodes in that level (len) to get the average.

4. Result: Add the average to the result list and proceed to the next level.
## Complexity Analysis
* **Time Complexity**: $O(N)$, where $N$ is the number of nodes in the tree, as each node is visited exactly once.
* **Space Complexity**: $O(M)$, where $M$ is the maximum width of the tree. In the worst case, the queue stores all nodes at the widest level.

---

## Solution (Java)
```java
class Solution {
    List<Double> result = new ArrayList<Double>();
    public List<Double> averageOfLevels(TreeNode root) {
        bfs(root);
        return result;
    }
    public void bfs(TreeNode node){
        if(node == null) return;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(node);
        while(!q.isEmpty()){
            int len = q.size();
            double sum = 0.0;
            for(int i = 1; i <= len; i++){
                TreeNode temp = q.poll();
                sum += temp.val;
                if(temp.left != null) q.offer(temp.left);
                if(temp.right != null) q.offer(temp.right);
            }
            sum /= len;
            result.add(sum);
        }
    }
}
```
