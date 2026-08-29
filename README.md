1. Let F(0) = 0,F(1) = 1,F(2) = 2 and F(n) = (F(n−1)+F(n−2)+F(n−
3) +1)%m. If n < 10105 and m < 105, write an efficient algorithm to compute
F(n).
2. Let F(0) = 0,F(1) = 1,F(2) = 2 and F(n) = (2F(n−1)−3F(n−3))%m. If
n < 10105 and m < 105, write an efficient algorithm to compute F(n).

A binary string is called dense if the number of 1’s in the string is more than
the number of 0’s. For example 1, 101,110101 are dense, but 10, 1001,100001
are not dense.
2
Given a binary string of length n, design an O(nlogn) time algorithm to com
pute the number of dense sub-strings of the given string. For example, given
10101, the answer is 6.
7. Given a binary string of length n, design a linear time algorithm to compute
the length of the largest dense sub-string of the given string.
8. Given a binary string of length n, design a linear time algorithm to compute
the length of the largest sub-string which contains equal number of 0’s and 1’s.
9. Given a binary string S of length n, design a linear time algorithm to compute
k, such that the number of 0’s in S[0..k] is equal to number of 1’s in S[k+1..n-1].
10. Given an array of sorted integers and an integer X > 0 , design a linear time
algorithm to count the number of pair elements in the array such that A[j] −
A[i] > X.
11. Given an array of integers , design a Θ(n2) algorithm to decide if there is i,j,k
such that A[i] + A[j] = A[k].
12. Given an array of integers , design an efficient algorithm to decide if there is
i, j, k, l such that A[i] − 2A[j] = A[k] − 3A[l].
13. Given n, radius of a circle with (0,0) as center, write a linear time algorithm to
compute the number of lattice (integer) points inside the circle.
14. Given a stream of n (about 109) numbers, design an O(n) time and O(k) space
algorithm to find an element of rank k.
15. Given a sequence of n numbers and an integer k < n, design a linear time
algorithm to find k numbers, closest to the median.
16. Given two sorted arrays of size m and n respectively and an integer k, design
an O(logk) algorithm to find an element of rank k in the merged array.

# Selection Algorithms

This section contains selection/ranking problems solved using efficient divide-and-conquer,
Quickselect, heaps, and elimination techniques.

---

## 1. K-th Rank Element Using Quickselect

### Problem

Given an unsorted array of `n` integers, find the element having rank `k`.

**Convention:** Rank `1` is the smallest element.

Design an efficient algorithm using **Quickselect**.

### Test Case

```text
Input:
A = [7, 2, 10, 4, 15, 6, 12, 3]
k = 3

Sorted array:
[2, 3, 4, 6, 7, 10, 12, 15]

Output:
4
