| Category | Tree |
| :--- | :--- |
| **Subcategory** | Traversal |
| **Title** | [116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/) |
| **Date** | 2026-04-09 |
| **Difficulty** | Medium |
| **Status** | Accepted |

---

## Description
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.  

Initially, all next pointers are set to NULL.
## Approach: BFS
By traversing the tree level by level, we can easily link each node to the one that follows it in the queue.  

1. Level Traversal: Use a Queue to process nodes level by level.

2. Next Pointer Connection: Inside the level loop, for each node cur:

    - If it is not the last node of the current level (i != len), set cur.next to the node currently at the front of the queue (q.peek()).

    - If it is the last node, its next pointer remains null (as initialized).

3. Child Progression: Add the left and right children to the queue. Since it's a perfect binary tree, we only need to check if one child is null to know if we've reached the leaf level.

## Complexity Analysis
* **Time Complexity**: $O(N)$, where $N$ is the number of nodes in the tree. We visit each node exactly once.
* **Space Complexity**: $O(W)$, where $W$ is the maximum width of the tree. For a perfect binary tree, the leaf level contains approximately $N/2$ nodes, leading to $O(N)$ space in the worst case for the queue

---

## Solution (Java)
```java
class Solution {
    public Node connect(Node root) {
        if(root == null) return null;
        Queue<Node> q = new LinkedList<Node>();
        q.offer(root);
        while(!q.isEmpty()){          
            int len = q.size();
            for(int i = 1; i <= len; i++){
                Node cur = q.poll();
                if(i != len) cur.next = q.peek();
                if(cur.right != null){ 
                    q.offer(cur.left);
                    q.offer(cur.right);
                }
            }
        }
        return root;
    }
}
```
