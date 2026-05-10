| Category | Tree |
| :--- | :--- |
| **Subcategory** | Tree Path / BackTracking |
| **Title** | [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/description/) |
| **Date** | 2026-04-23 |
| **Difficulty** | Easy |
| **Status** | Accepted |

---

## Description
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

## Approach : DFS with Backtracking
We use a Preorder Traversal to explore all paths. Because we need to "return" to previous nodes to explore other branches, we must implement a backtracking mechanism.

1. Prepare two lists: result to store finalized path strings and path to store current node values as integers.

2. Add the current node value to the path list immediately upon entering the function (Preorder).

3. Base Case (Leaf Node): If the current node has no children, convert the path list into a string formatted with "->" and add it to the result.

4. Recursive Step: If the current node has a left or right child, recursively call the traversal function for that child.

5. Backtracking: After the recursive function for a child returns, remove the last node from the path list. This restores the path state, allowing the algorithm to explore other branches correctly.



## Complexity Analysis
* **Time Complexity**: $O(N \cdot H)$, where $N$ is the number of nodes and $H$ is the height of the tree. We visit each node once, but string construction for each leaf path can take $O(H)$ time.

* **Space Complexity**: 
    - DFS Stack: $O(H)$, where $H$ is the height of the tree.
    - Path Storage: $O(H)$ to store the current path nodes in the list.

---

## Solution 1  (Java + StringBuilder)
```java
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        traverse(root, result, path);
        return result;
    }
    public void traverse(TreeNode node, List<String> result, List<Integer> path){
        path.add(node.val);
        if(node.left == null && node.right == null){
            //using StringBuilder
            StringBuilder sPath = new StringBuilder();
            for(int i = 0; i < path.size()-1; i++){
                sPath.append(path.get(i)).append("->");
            }
            sPath.append(path.get(path.size()-1));
            result.add(sPath.toString());
        }
        if(node.left != null){
            traverse(node.left, result, path);
            path.remove(path.size()-1);
        }
        if(node.right != null){
            traverse(node.right, result, path);
            path.remove(path.size()-1);
        }
    }
}
```

## Solution 2  (Java + String)
```java
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        if(root == null) return result;
        traverse(root, result, path);
        return result;
    }
    public void traverse(TreeNode node, List<String> result, List<Integer> path){
        path.add(node.val);
        if(node.left == null && node.right == null){
            //using String 
            String sPath = "";
            for(int i = 0; i < path.size()-1; i++){
                sPath += Integer.toString(path.get(i));
                sPath += "->";
            }
            sPath += Integer.toString(path.get(path.size()-1));
            result.add(sPath);
        }
        if(node.left != null){
            traverse(node.left, result, path);
            path.remove(path.size()-1);
        }
        if(node.right != null){
            traverse(node.right, result, path);
            path.remove(path.size()-1);
        }
    }
}
```


