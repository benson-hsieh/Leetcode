| Category | Array |
| :--- | :--- |
| **Subcategory** | Brute Force / Parity |
| **Title** | [3917. Count Indices With Opposite Parity](https://leetcode.com/problems/count-indices-with-opposite-parity/) |
| **Date** | 2026-05-05 |
| **Difficulty** | Easy |
| **Status** | Accepted |

---

## Description
Given an integer `n`, let `r` be the integer formed by reversing the digits of `n`. Return the sum of all **prime numbers** between $\min(n, r)$ and $\max(n, r)$, inclusive.

## Approach: Number Reversal and Prime Verification
The problem requires two main mathematical operations: reversing an integer and identifying prime numbers within a dynamic range.

### Key Steps:
1.  **Reverse the Number**: Use a `while` loop with modulo and division to generate the reversed integer `later`.
2.  **Define the Range**: Find the lower bound using `Math.min(n, later)` and the upper bound using `Math.max(n, later)`.
3.  **Iterate and Check Primes**: 
    - Loop through each number `i` in the range.
    - For each `i`, use a helper logic to determine if it is prime. 
    - Note: Numbers $\le 1$ are not prime.
4.  **Summation**: Add all identified primes to the total `sum`.

## Complexity Analysis
- **Time Complexity**: $O(R \times \sqrt{M})$, where R is the range (max - min) and M is the value of the numbers being checked. Reversing the number takes O(log n).
- **Space Complexity**: O(1), as we only store a few primitive variables.

---

## Solution (Java)

```java
class Solution {
    public int sumOfPrimesInRange(int n) {
        int origin = n, later = 0;
        while(n > 0){
            later = later * 10 + n % 10;
            n /= 10;
        }
        int sum = 0;
        for(int i = Math.min(origin, later); i <= Math.max(origin, later); i++){
            boolean flag = true;
            if(i == 1) flag = false;
            for(int j = 2; j < i; j++){
                if(i % j == 0) flag = false;
            }
            if(flag) {
                sum += i;
                System.out.print(i+" ");
            }
        }
        return sum;
    }
}
