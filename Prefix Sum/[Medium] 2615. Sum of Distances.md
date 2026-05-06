| Category | Array |
| :--- | :--- |
| **Subcategory** | Prefix Sum |
| **Title** | 2615. Sum of Distances |
| **Date** | 2026-04-23 |
| **Difficulty** | Medium |
| **Status** | Accepted |

## [2615. Sum of Distances](https://leetcode.com/problems/sum-of-distances/description/)


### 解題思路：


**時間複雜度**：
**空間複雜度**：

### Solution 1 : 
```java
class Solution {
    public long[] distance(int[] nums) {
        int n = nums.length;
        long[] arr = new long[n];
        HashMap<Integer, List<Integer>> position = new HashMap<>();
        for(int i = 0; i < n; i++){
            position.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        for(List<Integer> pos : position.values()){
            long index_sum = 0;
            for(int x : pos) index_sum += x;
            long leftIndexSum = 0;
            int m = pos.size();

            for(int i = 0; i < m; i++){
                long rightIndexSum = index_sum - leftIndexSum - pos.get(i);
                long leftDist = (long)pos.get(i) * i - leftIndexSum;
                long rightDist = rightIndexSum - (long)pos.get(i) * (m - i - 1);

                arr[pos.get(i)] = leftDist + rightDist;
                leftIndexSum += pos.get(i);
            }
        }
        return arr;
    }
}
```

### Solution 2: Brute Force => TLE
```java
class Solution {
    public long[] distance(int[] nums) {
        int n = nums.length;
        long[] arr = new long[n];
        HashMap<Integer, List<Integer>> position = new HashMap<>();
        for(int i = 0; i < n; i++){
            position.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }

        for(int i = 0; i < n; i++){
            int target = nums[i];
            List<Integer> index_list = position.get(target);

            long dist = 0;
            for(int j : index_list){
                dist += Math.abs((long) i - j);
            }
            arr[i] = dist;
        }
        return arr;
    }
}
```
