| Category | Tree |
| :--- | :--- |
| **Subcategory** | Traversal |
| **Title** | [429. N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/) |
| **Date** | 2026-04-01 |
| **Difficulty** | Medium |
| **Status** | Accepted |

---

## Description
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
## Approach: BFS
The traversal logic remains consistent with binary tree level order traversal, adapted for multiple children.

1. Queue Management: Use a Queue to store nodes to be visited.

2. Level Processing: Record the current queue size (len) to process all nodes belonging to the same level.

3. Handling N-children: For each node, instead of accessing .left and .right, iterate through the node.children list.

4. Null Safety: Check if the children list is null or empty before iterating, and ensure individual child nodes are not null before adding them to the queue.

## Complexity Analysis
* **Time Complexity**: $O(N)$, where $N$ is the total number of nodes in the N-ary tree. Each node is enqueued and dequeued exactly once.
* **Space Complexity**: $O(N)$ in the worst case. This occurs when the tree is very "flat" and the queue needs to store a large number of nodes at the widest level.

---

## Solution (Java)
```java
class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(root == null) return result;
        Queue<Node> q = new LinkedList<Node>();
        q.offer(root);
        while(!q.isEmpty()){
            int len = q.size();
            List<Integer> list = new ArrayList<Integer>();
            for(int i = 1; i <= len; i++){
                Node temp = q.poll();
                list.add(temp.val);
                List<Node> children = temp.children;
                if(children == null || children.size() == 0){
                    continue;
                }
                for(Node child : children){
                    if(child != null) 
                        q.offer(child);
                }
            }
            result.add(list);
        }
        return result;
    }
}
```
