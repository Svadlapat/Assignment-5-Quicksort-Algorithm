# Assignment-5-Quicksort-Algorithm
Assignment 5 – Quicksort Algorithm: Implementation, Analysis & Randomization

This repository contains:

 Deterministic Quicksort implementation
 Randomized Quicksort implementation
 Empirical runtime comparison code
 Full detailed report (REPORT.md)

Files in This Repository:
| File                      | Description                           |
| ------------------------- | ------------------------------------- |
| `quicksort.py`            | Deterministic Quicksort (fixed pivot) |
| `randomized_quicksort.py` | Randomized pivot Quicksort            |
| `analysis.py`             | Runtime performance benchmarking      |
| `REPORT.md`               | Full detailed assignment report       |
| `README.md`               | This file                             |


How to Run the Code
1. Run Deterministic Quicksort:
``` bash 
python quicksort.py
```
2. Run Randomized Quicksort
``` bash
python randomized_quicksort.py
```

3. Run Empirical Analysis (Benchmark)
``` bash
python analysis.py
```

Deterministic Quicksort performs well on random input but can degrade to O(n²) on sorted or adversarial input.

Randomized Quicksort consistently gives O(n log n) expected performance.

Random pivot selection eliminates deterministic worst-case patterns.

Empirical results match theoretical expectations:
Randomized version shows smoother and faster performance across all input sizes.