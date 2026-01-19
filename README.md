# Coding-Practice

This repository is a collection of solved algorithms and documentation on core software engineering principles.

---

# Table of Contents
* [Software Theory](#software-theory)
    * [Data Structures](#data-structures)
    * [Set vs Dictionary](#set-vs-dictionary)
    * [Time Complexity](#time-complexity)
        * [Big O Reference Table](#big-o-reference-table)
        * [Python-Specific Complexity](#python-specific-complexity)
    * [Spatial Complexity](#spatial-complexity)
    * [Relationship Between Spatial Complexity and Time Complexity](#relationship-between-spatial-complexity-and-time-complexity)

---

# Software Theory
Important concepts to know for software development (data structures is lacking an explanation, it just compares dictionaries and sets)

## Memory Allocation 

### Heap

Related to **dynamic memory allocation**. 

It is an unorganized pool of memory. Provides flexibility for data that needs to live further than a single function call or data that it is not known ahead of time.

When an object is created or **new** in C++, the system finds memory in the heap and returns its address. It needs garbage collector to free it when it is no longer being used (or to be manually cleaned) to avoid memory leaks.

### The Stack
Operates by LIFO. When a function is called, the CPU moves the Stack Pointer and creates a new stack frame. This frame holds the function's local variables, arguments and return address. Once finished, the pointer moves back.

## Sorting Algorithms

Sorting is the process or arranging data into a specific order, typically numerical or alphabetical. It is the foundation of data efficiency.

It is normally used as a preprocessing tool that makes other tasks faster.

* Optimized Searching: Algorithms like **Binary Search** cannot be performed on unsorted data.
* Identifying Relationships: Sorting brings identical or related data points together.

There exist different sorting algorithms and they are useful on different scenarios.

### Quick Sort
It uses a pivot element to partition an array in two halves, to the left elements smaller thant the pivot and to the right, elements larger than the pivot. Then does this recursively until the array is sorted.

* It provides a speed of O(nlogn)
* It has low Spatial Complexity, therefore it is useful in scenarios where memory is limited.


## Data Structures

### Set vs Dictionary
A **Set** in Python is architecturally identical to a **Dictionary** that contains only keys and no values. 
* Both utilize a **Hash Table** for storage.
* Both provide **O(1) average time complexity** for lookups, insertions, and deletions.
* Sets are more memory-efficient when you only need to track the existence of unique items.

### Trees

Hierarchical structure in which each node has a value and pointers to **"children"**. 


* It can point to **multiple** other nodes (unlike linked list).
* A tree cannot go backwards, starts at root and keeps on expanding.


```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
``` 

 





---

## Time Complexity

### Big O Reference Table

| Notation | Name | Practical Example |
| :--- | :--- | :--- |
| $O(1)$ | Constant | Array index access, Hash Map lookup/insertion. |
| $O(\log n)$ | Logarithmic | Binary search, balanced BST operations. |
| $O(n)$ | Linear | Single loop through an array, linear search. |
| $O(n \log n)$ | Linearithmic | Merge Sort, QuickSort, Heap Sort. |
| $O(n^2)$ | Quadratic | Nested loops over the same input, Bubble Sort. |
| $O(2^n)$ | Exponential | Recursive Fibonacci, Tower of Hanoi. |
| $O(n!)$ | Factorial | Generating all permutations of a list. |



### Python-Specific Complexity

#### O(1) Operations
Beyond index access and appending, these operations are constant time:
* `len(list)`: Python stores the size in the object header.
* `x in dict` / `x in set`: Average case hash lookup.
* `list.pop()`: Removing from the end (no shifting required).

#### O(n) Operations
* `max(list)` / `min(list)`: Requires a full iteration of the collection.
* `list.copy()`: Allocates new memory and copies every reference.
* `x in list`: Sequential search through the array.
* `list.insert(i, val)`: Requires shifting all subsequent elements in memory.
* `list.pop(0)` or `del list[i]`: Requires re-indexing/shifting the array.
* `str1 + str2`: String concatenation creates a new string object (copying both).

---

## Spatial Complexity
Spatial (Space) Complexity measures the total extra memory an algorithm requires relative to the input size $n$.

* **Auxiliary Space:** The temporary space used by the algorithm (excluding input).
* **Stack Space:** Important in recursion; each recursive call adds a frame to the call stack ($O(n)$ depth).
* **Trade-offs:** Often, $O(n)$ space can be used to reduce time complexity from $O(n^2)$ to $O(n)$ (e.g., using a Set for lookups).

---

## Relationship Between Spatial Complexity and Time Complexity

They are both metrics used to evuluate an algorithm's performance.

Imagine the algorithm must identify if values repeat in an array. The programmer could make that, for each number, it checks the array over and over again and compares ($O(n^2)$). However, spatially it consumes O(1) since it's tracking two variables all the time. Program is inefficient in time but it is efficient in memory.

If the programmer instead added data to a set and checked if the number was already in the set, time complexity would be O(n) and spatial complexity would be O(n) too since it would have created a set that could potentially hold all elements in the array.

