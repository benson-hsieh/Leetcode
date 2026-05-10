| Category | Tree |
| :--- | :--- |
| **Subcategory** | Tree Path / BackTracking  |
| **Title** | [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/) |
| **Date** | 2026-04-28 |
| **Difficulty** | Medium |
| **Status** | Accepted |

---

## Description
You are given the root of a binary tree containing digits from 0 to 9 only. Each root-to-leaf path in the tree represents a number. For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.  

Return the total sum of all root-to-leaf numbers.

## Approach 1 : Backtracking (List-based)
Based on the template from Problem 257, this approach collects all digits in a path and processes them at the leaf.  
1. Collection: Maintain a ```List<Integer>``` path to store individual digits.

2. Leaf Logic: When a leaf is reached, iterate through the ```path``` list to construct the full number (e.g., $[1, 2, 3] \rightarrow 123$) and add it to a results list.

3. Backtrack: Manually ```remove``` the last element after visiting subtrees.

4. Final Sum: Iterate through the results list to calculate the total.

## Approach 2 : Optimized Recursion (Mathematical)
Based on the template from Problem 112, this approach treats the path as a single integer passed by value.

1. Path Calculation: Pass the current accumulated value as an int. At each node, update the value: ```currentSum = parentSum * 10 + node.val.```

2. Leaf Logic: If the node is a leaf, add the ```currentSum``` directly to a global total variable res.

2. Implicit Backtracking: Since int is a primitive type in Java, it is passed by value. When the recursion returns to the parent, the value naturally reverts to the parent's state without manual removal.

## Complexity Analysis
* **Time Complexity**: $O(N)$, where $N$ is the number of nodes. Each node is visited once.
* **Space Complexity**: $O(H)$, where $H$ is the tree height (recursion stack). For a balanced tree, this is $O(\log N)$.

---

## Solution 1 (Backtracking in Java)
```java
class Solution {
    public int sumNumbers(TreeNode root) {
        List<Integer> path = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        traverse(root, list, path);
        int res = 0;
        for(int num : list){
            res += num;
        }        
        return res;
    }
    public void traverse(TreeNode root, List<Integer> list, List<Integer> path){
        if(root == null) return;
        path.add(root.val);
        if(root.left == null && root.right == null){
            int num = 0;
            for(int i = 0; i < path.size(); i++){
                num = num * 10 + path.get(i);
            }
            list.add(num);
        }
        if(root.left != null){
            traverse(root.left, list, path);
            path.remove(path.size() - 1);
        }
        if(root.right != null){
            traverse(root.right, list, path);
            path.remove(path.size() - 1);
        }
    }
}
```

## Solution 2 (Mathematical in Java)
```java
class Solution {
    int res = 0;
    public int sumNumbers(TreeNode root) {
        sum(root, 0);
        return res;
    }
    public void sum(TreeNode root, int path){
        if(root == null) return;
        path = path * 10 + root.val;
        if(root.left == null && root.right == null)
            res += path;
        sum(root.left, path);
        sum(root.right, path);
    }
}
```