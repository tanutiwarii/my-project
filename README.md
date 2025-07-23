# Sorting Algorithms

Sorting algorithms are methods for reorganizing a list of items into a particular order, such as ascending or descending. This README provides an overview of common sorting algorithms and explains their key characteristics.

---

## Table of Contents
1. [Bubble Sort](#bubble-sort)
2. [Selection Sort](#selection-sort)
3. [Insertion Sort](#insertion-sort)
4. [Merge Sort](#merge-sort)
5. [Quick Sort](#quick-sort)
6. [Heap Sort](#heap-sort)
7. [Radix Sort](#radix-sort)
8. [Bucket Sort](#bucket-sort)

---

## Bubble Sort
- **Description:** Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- **Time Complexity:** O(n²) (worst and average case), O(n) (best case when the array is already sorted).
- **Space Complexity:** O(1) (in-place).
- **Stable:** Yes.

---

## Selection Sort
- **Description:** Divides the list into a sorted and unsorted region. Finds the smallest (or largest) element from the unsorted region and moves it to the sorted region.
- **Time Complexity:** O(n²).
- **Space Complexity:** O(1) (in-place).
- **Stable:** No.

---

## Insertion Sort
- **Description:** Builds the final sorted list one item at a time by comparing the current element to already sorted elements and inserting it into its correct position.
- **Time Complexity:** O(n²) (worst and average case), O(n) (best case for nearly sorted arrays).
- **Space Complexity:** O(1) (in-place).
- **Stable:** Yes.

---

## Merge Sort
- **Description:** Divides the list into halves, recursively sorts each half, and then merges the sorted halves back together.
- **Time Complexity:** O(n log n) (all cases).
- **Space Complexity:** O(n).
- **Stable:** Yes.

---

## Quick Sort
- **Description:** Selects a "pivot" element and partitions the array into two sub-arrays: elements less than the pivot and elements greater than the pivot. Recursively applies the process to sub-arrays.
- **Time Complexity:** O(n²) (worst case), O(n log n) (average case).
- **Space Complexity:** O(log n) (in-place, but depends on implementation).
- **Stable:** No.

---

## Heap Sort
- **Description:** Converts the list into a binary heap data structure and repeatedly extracts the maximum (or minimum) element to build the sorted list.
- **Time Complexity:** O(n log n) (all cases).
- **Space Complexity:** O(1) (in-place).
- **Stable:** No.

---

## Radix Sort
- **Description:** Sorts numbers by processing individual digits. Uses counting sort as a subroutine to sort digits at each significant place value.
- **Time Complexity:** O(nk), where k is the number of digits in the largest number.
- **Space Complexity:** O(n + k).
- **Stable:** Yes.

---

## Bucket Sort
- **Description:** Divides the list into several buckets, distributes the elements into these buckets, and then sorts each bucket individually (often using another sorting algorithm).
- **Time Complexity:** O(n + k) (best case), O(n²) (worst case, when all elements are in one bucket).
- **Space Complexity:** O(n + k).
- **Stable:** Yes.

---

This README provides a high-level explanation of sorting algorithms. For implementation details, refer to code examples or algorithm-specific documentation.