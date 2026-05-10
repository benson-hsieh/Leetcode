| Category | Tree |
| :--- | :--- |
| **Subcategory** | Traversal |
| **Title** | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/) |
| **Date** | 2026-03-31 |
| **Difficulty** | Medium |
| **Status** | Accepted |

---

## Description
Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## Approach 1: BFS (Iterative with Queue)
No extra Function needed

Use a Queue to hold TreeNode nodes, and an ArrayList as the node container for different levels.

Two-layer loops:
```Java
while (Queue is not empty) {
    // Declare a new ArrayList
    while (Queue length (number of nodes in that level) > 0) {
        // Add nodes...
    }
}
```
1. Except for the tree's root, all remaining nodes will be traversed within these two-layer loops.

2. The first layer is used to determine if there are still nodes; the second layer is used to traverse nodes of the current level.

3. After the nodes in the second-layer loop finish running, it returns to the first layer to add a list as the storage container for the next level.

## Approach 2: DFS (Recursive)
Requires an extra function for recursion

1. DFS needs parameters: root and depth (initial value is 0).

2. Record which level the current node belongs to by passing the depth parameter.

3. Add a conditional **result.size() == depth.** If true, it means result needs to increase in size (representing the first time reaching this depth).

    e.g., [[root]] -> [[root], []] -> ...

4. When adding a node to result, first get the depth and then add the node: result.get(depth).add(val);.

5. Then continuously call DFS recursively for the left and right child nodes, with **depth + 1**

## Complexity Analysis
- **Time Complexity**: $O(N)$, where $N$ is the number of nodes in the tree, as we visit each node once.
- **Space Complexity**: $O(N)$ for the output list. The BFS queue can hold up to $O(N)$ nodes at the widest level, and the DFS recursion stack can go up to $O(H)$.

---

## Solution (Java)

## BFS
```java
class Solution {      
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();  
        if(root == null) return result;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        while(!q.isEmpty()){
            List<Integer> list = new ArrayList<Integer>();
            int len = q.size();
            while(len > 0){
                TreeNode node = q.poll();
                list.add(node.val);
                if(node.left != null) q.offer(node.left);
                if(node.right != null) q.offer(node.right);
                len--;
            }
            result.add(list);
        }
        return result;
    }
   
}

```
## DFS
```java
class Solution {    
    List<List<Integer>> result = new ArrayList<List<Integer>>();  
    public List<List<Integer>> levelOrder(TreeNode root) {
        dfs(root, 0);
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
   