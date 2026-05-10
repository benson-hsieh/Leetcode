| Category | Tree |
| :--- | :--- |
| **Subcategory** | Tree Path / BackTracking |
| **Title** | [112. Path Sum](https://leetcode.com/problems/path-sum/description/) |
| **Date** | 2026-04-28 |
| **Difficulty** | Easy |
| **Status** | Accepted |

---

## Description

## Approach 1 : Backtracking (Find All Paths)
As shown in your first implementation, we explore every possible path, store them, and then calculate their sums.

1. Path Collection: Use a traverse function with a path list and a result list of lists.

2. Backtrack: Add the node value, recurse, and then remove the last element to explore other branches.

3. Validation: After collecting all paths, iterate through the result list and calculate the sum of each path.

4. Return: If any path sum matches targetSum, return true.

## Approach 2 : Direct Recursion (Subtraction)
As shown in your second implementation, this is a more optimized approach that checks the sum on-the-fly.

1. Base Case: If the current node is null, return false.

2. Leaf Node Check: If the current node is a leaf, check if its value is equal to the remaining targetSum.

3. Recursive Step: Subtract the current node's value from the targetSum and move to the children.

4. Logical OR: Return true if either the left subtree OR the right subtree has a valid path.

## Complexity Analysis
* **Time Complexity**: $O(N)$, where $N$ is the number of nodes. Both approaches visit each node once in the worst case.
* **Space Complexity**: 
    - Direct Recursion: $O(H)$, where $H$ is the tree height (recursion stack).
    - Backtracking: $O(N \cdot H)$, as it stores all path data in the result list.

---

## Solution 1 (Backtracking in Java)
```java
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        List<Integer> path = new ArrayList<>();
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        traverse(root, result, path);
        for(List<Integer> list : result){
            int sum = 0;
            for(int i = 0; i < list.size() ; i++){
                sum += list.get(i);
            }
            if(sum == targetSum) return true;
        }
        return false;
    }
    public void traverse(TreeNode root, List<List<Integer>> result, List<Integer> path){
        if(root == null) return;
        path.add(root.val);
        if(root.left == null && root.right == null){
            result.add(new ArrayList<>(path));
        }
        if(root.left != null){
            traverse(root.left, result, path);
            path.remove(path.size() - 1);
        }
        if(root.right != null){
            traverse(root.right, result, path);
            path.remove(path.size() - 1);
        }
    }
}
```

## Solution 2 (Direct Recursion in Java)
```java
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null) return false;
        if(root.left == null && root.right == null)
            return root.val == targetSum;
        return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val);
    }
}
```
