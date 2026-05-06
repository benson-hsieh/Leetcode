| Category | String |
| :--- | :--- |
| **Subcategory** | Rotate |
| **Title** | 796. Rotate String |
| **Date** | 2026-05-04 |
| **Difficulty** | Easy |
| **Status** | Accepted |

## [796. Rotate String](https://leetcode.com/problems/rotate-string/description/)

這題的核心在於「旋轉」的操作。

### 解題思路：
1. **字串拼接法**：將兩個 `s` 拼接在一起成 `s + s`。
2. **包含判斷**：如果 `goal` 是由 `s` 旋轉而來，那麼它一定會出現在 `s + s` 的子字串中。
3. **長度檢查**：前提是 `s` 和 `goal` 的長度必須相等。

**時間複雜度**：O(N)
**空間複雜度**：O(N)

### Solution 1: 字串拼接法 (Java)
```java
class Solution {
    public boolean rotateString(String s, String goal) {
        if (s.length() != goal.length()) return false;
        return (s + s).contains(goal);
    }
}
