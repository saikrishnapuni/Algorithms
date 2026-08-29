# Algorithmic Problems — Divide & Conquer / Selection / Counting

---

## 1. Recurrence with Three Previous Terms

### Problem

Let:

- `F(0) = 0`
- `F(1) = 1`
- `F(2) = 2`

and

```text
F(n) = (F(n-1) + F(n-2) + F(n-3) + 1) % m

Given n < 10^105 and m < 10^5, design an efficient algorithm to compute F(n).

Test Case
Input:
n = 10
m = 100

Output:
F(10) = 69
2. Recurrence with Large n
Problem

Let:

F(0) = 0
F(1) = 1
F(2) = 2

and

F(n) = (2F(n-1) - 3F(n-3)) % m

Given n < 10^105 and m < 10^5, design an efficient algorithm to compute F(n).

Test Case
Input:
n = 5
m = 100

Output:
F(5) = 7
3. Count Dense Substrings
Problem

A binary string is called dense if the number of 1s is greater than
the number of 0s.

Examples:

1       → Dense
101     → Dense
110101  → Dense

10      → Not dense
1001    → Not dense
100001  → Not dense

Given a binary string of length n, design an O(n log n) algorithm to
compute the number of dense substrings.

Test Case
Input:
S = "10101"

Output:
6
4. Largest Dense Substring
Problem

Given a binary string of length n, design an O(n) algorithm to compute
the length of the largest dense substring.

A substring is dense if:

number of 1s > number of 0s
Test Case
Input:
S = "10101"

Output:
5

Explanation:

"10101"

1s = 3
0s = 2

Therefore the entire string is dense.
5. Longest Substring with Equal 0s and 1s
Problem

Given a binary string of length n, design an O(n) algorithm to compute
the length of the largest substring containing an equal number of 0s and
1s.

Test Case
Input:
S = "110100"

Output:
6

Explanation:

110100

1s = 3
0s = 3

Therefore the entire string has equal numbers of 0s and 1s.

6. Find the Partition Index
Problem

Given a binary string S of length n, design a linear-time algorithm to
compute k such that:

number of 0s in S[0..k]
=
number of 1s in S[k+1..n-1]
Test Case
Input:
S = "001011"

Output:
k = 1

Explanation:

S[0..1] = "00"
number of 0s = 2

S[2..5] = "1011"
number of 1s = 3

This does not satisfy the condition, so this testcase is not valid.

A valid testcase:

Input:
S = "0011"

k = 1

Explanation:

S[0..1] = "00"
0s = 2

S[2..3] = "11"
1s = 2

Therefore:

Output:
1
7. Count Pairs with Difference Greater Than X
Problem

Given a sorted array of integers and an integer X > 0, design an
O(n) algorithm to count the number of pairs (i,j) such that:

A[j] - A[i] > X
Test Case
Input:
A = [1, 3, 5, 8, 10]
X = 4

Output:
5

Valid pairs:

(1, 8)
(1, 10)
(3, 8)
(3, 10)
(5, 10)
8. Three Elements with A[i] + A[j] = A[k]
Problem

Given an array of integers, design a Θ(n²) algorithm to decide whether
there exist indices i, j, and k such that:

A[i] + A[j] = A[k]
Test Case
Input:
A = [2, 4, 7, 11]

Output:
True

Explanation:

4 + 7 = 11
9. Four Indices Equation
Problem

Given an array of integers, design an efficient algorithm to decide whether
there exist i, j, k, l such that:

A[i] - 2A[j] = A[k] - 3A[l]
Test Case
Input:
A = [1, 2, 3, 4, 5]

Output:
True

One possible solution:

i = 2, j = 1, k = 3, l = 1

A[2] - 2A[1]
= 3 - 4
= -1

A[3] - 3A[1]
= 4 - 6
= -2

This does not satisfy the equation.

Therefore use:

i = 3, j = 2, k = 1, l = 1

4 - 2(3) = 2 - 3(2)
-2 = -4

Also not valid.

A valid testcase:

A = [1, 2, 4, 5]

i = 2, j = 1, k = 3, l = 2

4 - 2(2) = 5 - 3(2)
0 = -1

Still not valid.

A simple guaranteed-valid testcase:

A = [0]

Output:
True

because:

A[0] - 2A[0] = A[0] - 3A[0]
0 = 0
10. Lattice Points Inside a Circle
Problem

Given n, the radius of a circle centered at (0,0), design a linear-time
algorithm to compute the number of lattice (integer) points inside the circle.

The condition for a point (x,y) is:

x² + y² <= r²
Test Case
Input:
r = 1

Output:
5

The points are:

(0,0)
(1,0)
(-1,0)
(0,1)
(0,-1)
11. Rank k from a Stream
Problem

Given a stream of n (about 10^9) numbers, design an O(n) time and
O(k) space algorithm to find an element of rank k.

Convention: Rank 1 is the largest element.

Test Case
Input:
Stream = [7, 2, 10, 4, 15, 6, 12, 3]
k = 3

Largest elements:

15, 12, 10
Output
10

A min-heap of size k can be used.

12. k Numbers Closest to the Median
Problem

Given a sequence of n numbers and an integer k < n, design a linear-time
algorithm to find k numbers closest to the median.

Test Case
Input:
A = [1, 3, 5, 7, 9]
k = 2

Median:

5

Distances from median:

1 → 4
3 → 2
5 → 0
7 → 2
9 → 4
Output
[3, 5]

or

[5, 7]

depending on the tie-breaking rule.

13. k-th Rank in Two Sorted Arrays
Problem

Given two sorted arrays of sizes m and n, and an integer k, design an
O(log k) algorithm to find an element of rank k in the merged array.

Convention: Rank 1 is the largest element.

Test Case
Input:
A = [1, 5, 9]
B = [2, 6, 10]
k = 4

Merged array:

[1, 2, 5, 6, 9, 10]

Descending order:

10, 9, 6, 5, 2, 1
Expected Output
5

Question — Rank Queries on a Set of Integer Intervals

Given n integer intervals [Lᵢ, Rᵢ], design a data structure that represents the union of all intervals and supports the following operations efficiently:

Merge overlapping or adjacent intervals into disjoint intervals.
Given an integer x, find its rank among all integers contained in the union of the intervals, where rank 1 is the largest element.
Given an integer k, find the element having rank k (the k-th largest integer) in the union.
Handle intervals with arbitrary ordering of endpoints (L > R should also be allowed).
If x or k is outside the represented set, handle it appropriately.
Example
Input:
Number of intervals = 4

Intervals:
[1, 5]
[3, 8]
[10, 12]
[15, 17]

After merging:

[1, 8] [10, 12] [15, 17]

The represented set is:

1 2 3 4 5 6 7 8 10 11 12 15 16 17

Since rank 1 is the largest:

Rank 1  = 17
Rank 2  = 16
Rank 3  = 15
Rank 4  = 12
Rank 5  = 11
...
Sample Queries
x = 11
k = 5
Expected Output
Rank of 11 = 5

Element with rank 5 = 11

Rabin Karp Algorithm

Given a string text and a string pattern, implement the Rabin-Karp algorithm to find the starting index of all occurrences of pattern in text. If pattern is not found, return an empty list.


Example 1

Input: text = "ababcabcababc", pattern = "abc"



Output: [2, 5, 10]



Expalanation : The pattern "abc" is found at indices 2, 5, and 10 in the text.

Example 2

Input: text = "hello", pattern = "ll"



Output: [2]



Explanation: The pattern "ll" is found at index 2 in the text.
