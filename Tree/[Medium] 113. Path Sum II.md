| Category | Tree |
| :--- | :--- |
| **Subcategory** | Tree Path / BackTracking |
| **Title** | [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/description/) |
| **Date** | 2026-04-29 |
| **Difficulty** | Medium |
| **Status** | Accepted |

---

## Description
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum.

## Approach: DFS with Backtracking
This problem combines the core concept of Problem 112 (checking sums) with the implementation style of Problem 257 (tracking paths).

1. Path Management: Maintain a path list to store nodes as you traverse from root to leaf.

2. Preorder Addition: Add the current node's value to the path list as soon as you enter the function.

3. Leaf Verification: When a leaf node is reached, check if the targetSum matches the node's value.

4. Snapshoting: If the sum is correct, add a new copy of the current path to the result.

5. Backtracking: After exploring both children, remove the current node from the path list to restore the state for the parent function.

Additionally, since this problem requires finding paths, the current traversal state and nodes are stored in a path List.

However, in Java, objects like Lists are passed by reference (memory address) during recursion. Therefore, you cannot simply write result.add(path). If you do this, you are only adding the memory address of the path object to the result.

Because the path list is constantly being modified (added to and removed from) during the backtracking process, the final contents of the list will change. Since the root is never removed in your logic, the result would end up only containing the root multiple times **(e.g., [[5], [5]])**.

Think of it this way: the result list is only storing a "URL" (address) rather than the actual content. To fix this, when updating the result, you must create a brand-new list instance to capture a snapshot of the current path
**=> result.add(new ArrayList<>(path))**

## Complexity Analysis
* **Time Complexity**: $O(N^2)$, where $N$ is the number of nodes. We visit each node once, but at every leaf, we may perform a path copy which takes $O(N)$ time.
* **Space Complexity**: $O(H)$, where $H$ is the tree height. This accounts for the recursion stack and the list used for backtracking.

---

## Solution (Java)
```java
class Solution {
    List<List<Integer>> result = new ArrayList<>();
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<Integer> path = new ArrayList<>();
        traverse(root, targetSum, path);
        return result;
    }
    public void traverse(TreeNode root, int targetSum, List<Integer> path){
        if(root == null) return;
        path.add(root.val);
        if(root.left == null && root.right == null && targetSum == root.val)
            result.add(new ArrayList(path));
        if(root.left != null){
            traverse(root.left, targetSum - root.val, path);
            path.remove(path.size() - 1);
        }
        if(root.right != null){
            traverse(root.right, targetSum - root.val, path);
            path.remove(path.size() - 1);
        }
    }
}
```
