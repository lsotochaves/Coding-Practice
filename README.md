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

They are both metrics used to evaluate an algorithm's performance.

Imagine the algorithm must identify if values repeat in an array. The programmer could make that, for each number, it checks the array over and over again and compares ($O(n^2)$). However, spatially it consumes O(1) since it's tracking two variables all the time. Program is inefficient in time but it is efficient in memory.

If the programmer instead added data to a set and checked if the number was already in the set, time complexity would be O(n) and spatial complexity would be O(n) too since it would have created a set that could potentially hold all elements in the array.

---

## Data Structures

### Set vs Dictionary
A **Set** in Python is architecturally identical to a **Dictionary** that contains only keys and no values. 
* Both utilize a **Hash Table** for storage.
* Both provide **O(1) average time complexity** for lookups, insertions, and deletions.
* Sets are more memory-efficient when you only need to track the existence of unique items.


### Trees

Hierarchical structure in which each node has a value and pointers to **"children"**. 


* It can point to **multiple** other nodes (unlike linked list).
* A tree cannot go backwards, starts at root and keeps on expanding.`

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
``` 

#### Terminology

* **Edge**: Link between two nodes.
* **Leaf**: Node that has no children.
* **Height**: Length of the longest path between a **node** and a **leaf**.
* **Depth**: Length of the path from **root** to specific **node**.

#### Binary Tree

Each node can have a **maximum** of two children (left child and right child).
```python
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

##### Binary Search Tree (BST)

In a binary search tree, the **left subtree contains values less than the parent's value** while the **right subtree contains values greater than the parent's value**.

###### Utility

The utility of a BST comes from it being **balanced**. If numbers are inserted in order [1, 2, 3, 4, ...] the tree will be a straight line going to the right. That is a **degenerate tree**. In this state it becomes as slow as a linked list.

A **balanced tree** means the height of the left and right subtrees of every node differs by no more than one. To fix this, **self-balancing** is used, in which if new data comes in and one side becomes loaded, the tree performs a rotation (rearrangement of its pointers). An **AVL tree** (strictly balanced) is **faster** at searching data but **slower** at adding or deleting it, while a **Red-Black Tree** is more loosely balanced, hence **slower at searching but faster at inserting/deleting**.

For a balanced BST, operations are O(log n). For a degenerate tree, operations degrade to O(n).

* **Searching items**: If a certain number is being searched, half of the data can be easily discarded in each pass. 
* **Maintaining sorted data**: In an array, if a number must be inserted and the array must be ordered, every single element needs to be shifted. In a BST, the tree is traversed until a **leaf** is found and the data is added there.
* **Efficient range queries**: Imagine all values between a specified range (50k-70k), only the nodes that fall between this range are analyzed (no need to analyze every single node).

###### Cost of building a BST

The use of a BST **must** be justified by the problem the programmer is trying to solve. Building a tree is expensive, but in the long run it can be more efficient than checking a list over and over again.

Building a BST takes O(n log n) on average when inserting n elements one by one.

#### Heap

It is a tree, however it is almost always implemented as a list/array.

There are **max-heap** in which the parent is always bigger than its children (root node is the largest element) and **min-heap**, where the parent is smaller than its children and the root is the smallest element.

A heap must be **complete**, which means that all levels are fully filled except possibly the last level, which is filled from left to right. Because of this, a heap can be mapped into an array in which each **element** can be accessed this way:

* Left Child = 2i + 1

* Right Child = 2i + 2

* Parent = (i - 1) // 2     

##### Insertion

It adds a new element at the **end of the array** (next available position), compares it with its parent, if it violates the heap property they are swapped and repeat until the property is restored. This is called **bubble-up** or **heapify-up**. It has a complexity of O(log n).

##### Deletion (Extract-Min/Max)

The root is removed (min or max), the last element replaces the root, then it's compared with its children and swapped with the smaller child (min-heap) or larger child (max-heap) until the heap property is restored. This is called **bubble-down** or **heapify-down**. It has a complexity of O(log n).

##### Cost of building a Heap

Building a heap from a random list takes O(n) using the **heapify** algorithm (bottom-up construction). 

##### Utility

* **Priority Queues**: Handling the most urgent tasks that need to happen next.
* **Heapsort**: Sorting a list in O(n log n) with O(1) extra space.
* **K-largest/smallest element**: Finding the top or bottom k elements in a stream of data.
* **Median finding**: Using two heaps (max-heap and min-heap) to efficiently track the median in a data stream.




## Sorting Algorithms

Sorting is the process or arranging data into a specific order, typically numerical or alphabetical. It is the foundation of data efficiency.

It is normally used as a preprocessing tool that makes other tasks faster.

* Optimized Searching: Algorithms like **Binary Search** cannot be performed on unsorted data.
* Identifying Relationships: Sorting brings identical or related data points together.

There exist different sorting algorithms and they are useful on different scenarios. And in practice, most libraries use a combination of algorithms to get the best of different implementations.

### Quick Sort
It uses a pivot element to partition an array in two halves, to the left elements smaller thant the pivot and to the right, elements larger than the pivot. Then does this recursively until the array is sorted.

* It provides a speed of O(n logn) but in worst case it is $O(n^2)$ when a bad pivot is chosen. 
* It has low Spatial Complexity, therefore it is useful in scenarios where memory is limited.
* Since it works with the original array it tends to have better cache locality.

### Merge Sort

The algorithm splits the array in half until each sub-array has one element and them merges them back in order.

* Provides time complexity of O(n logn) for all cases.

* It is useful when preserving the relative order of equal elements is necessary.

* It can work with linked lists since it traverses the array using two pointers, one that points to next and another that moves twice as fast. When the second reaches the end of the list the first one is located at the middle. It is efficient with linked lists since sorting involves re positioning the pointers and not copying or shifting data. Even though it takes O(n) to reach the middle of the linked ist, time complexity is still O(n logn).

* Eg: Sorting by last name where preserving first name is important.

### Heap Sort

Utilizes a Heap (ADD LATER) to find the maximum element in **O(log n)** time.

The root node in a binary tree is grater than its children.

An array is arranged into max-heap, then root of heap is swapped with the last element and heap size is reduced by 1, therefore eventually everything is sorted.

* Runs in O(n logn) in all cases.
* It can be used in systems where **predictable** execution time is important (quicksort runs slower at worst case). It is attractive for memory constrained environments, since it works over the original array and uses a small fixed number of variables, its **spatial complexity** is O(1), unlike [merge sort](#merge-sort) which requires  an auxiliary array of O(n).



 





