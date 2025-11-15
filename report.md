# Assignment 5: Quicksort Algorithm – Implementation, Analysis & Randomization

1. Introduction

Quicksort is one of the most widely used sorting algorithms due to its average-case efficiency, cache-friendliness, and practical performance on large datasets.
This assignment explores:

1.Deterministic Quicksort

2.Randomized Quicksort

3.Time and space complexity analysis

4.Empirical benchmarking of both algorithms

Through theoretical understanding and experiments, we demonstrate how randomization improves the reliability and performance of Quicksort.

2. Design Choices & Implementation Details
2.1 Deterministic Quicksort

Pivot Selection
Deterministic Quicksort chooses the last element of the array as the pivot.

Reason:
1.Easy to implement
2.Simplifies partition function
3.Maintains consistency for analysis
4.Partition Method
5.We implemented Lomuto partition scheme, which:
6.Maintains index i for smaller elements
7.Swaps elements <= pivot into the left region
8.Places pivot in its correct sorted position
9.Recursion Strategy
10.The algorithm recursively sorts:
Left partition (elements ≤ pivot)
Right partition (elements > pivot)

This follows the divide-and-conquer paradigm.

2.2 Randomized Quicksort:

Objective:
Deterministic Quicksort fails on:
Sorted arrays
Reverse-sorted arrays
Duplicate-heavy arrays
This leads to O(n²) performance.
Random Pivot Selection

Randomized Quicksort:
Selects a pivot index uniformly at random
Swaps it with the last element
Performs normal partition

Why Randomization Helps
Random pivoting eliminates adversarial patterns and makes worst-case extremely unlikely.
Probability of worst-case for randomized version: n!/1​(nearly impossible)

3. Time & Space Complexity Analysis:

3.1 Time Complexity Summary
| Case             | Deterministic | Randomized          | Explanation                                                              |
| ---------------- | ------------- | ------------------- | ------------------------------------------------------------------------ |
| Best Case    | O(n log n)    | O(n log n)          | Balanced partitions                                                      |
| Average Case | O(n log n)    | O(n log n)          | Expected behavior                                                        |
| Worst Case   | O(n²)         | O(n log n) expected | Deterministic worst-case triggered on sorted input; randomized avoids it |



3.2 Why Average Case is O(n log n):

At each recursive level, the work done is proportional to n (linear partitioning).

Number of recursion levels in average case ≈ log n.

Thus: T(n)=n+n/2+n/4+⋯=O(nlogn)

3.3 Why Worst Case is O(n²)

Worst case occurs when pivot produces the most unbalanced partitions:
[n-1 elements] [pivot] [0 elements]

Then recursion depth becomes n:
T(n)=T(n−1)+O(n)
Expands to:
O(n+(n−1)+(n−2)+…)=O(n2)

3.4 Space Complexity:
| Case         | Space Complexity         |
| ------------ | ------------------------ |
| Best/Average | O(log n) recursion stack |
| Worst        | O(n) stack depth         |

Randomized Quicksort reduces probability of worst-case stack usage.

4. Empirical Analysis (Experiment Results):
4.1 Setup

We measured execution time for:

Deterministic Quicksort

Randomized Quicksort

On arrays of size:
1000, 3000, 5000, 7000, 10000

All tests run on:

Random arrays

Same input passed to both algorithms (copied every time)

4.2 Observed Results:

Deterministic Quicksort performed well for random data.

Randomized Quicksort was consistently faster.

Its performance did not degrade for large sizes.

Deterministic version’s time increased more sharply as size grew.

4.3 Interpretation:

The experiment supports the theory:

Randomized pivot selection prevents worst-case behavior.

Deterministic pivot selection risks poor performance depending on input distribution.

Randomization ensures more balanced partitions on expectation.

5. Conclusion:

This assignment demonstrates:

Quicksort is highly efficient and widely applicable.

Deterministic implementation is simple but vulnerable to worst-case scenarios.

Randomized Quicksort stabilizes performance and reduces worst-case likelihood.

Empirical tests confirm theoretical predictions.

Randomization makes Quicksort reliable, which is why it is commonly used in:

Databases (PostgreSQL)

Programming languages (C++, Python sort inspiration)

Large-scale distributed systems (Hadoop, Spark)
