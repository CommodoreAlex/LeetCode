# Big O Notation Guide

## Introduction to Big O Notation

Big O notation is used to describe the performance or complexity of an algorithm, especially in terms of its time or space requirements. It focuses on how the execution time or memory usage grows as the input size increases. It abstracts away constant factors and lower-order terms, providing a high-level understanding of algorithm efficiency.

## Common Time Complexities

### 1. **O(1) – Constant Time**

An algorithm is said to have O(1) complexity if the execution time or space does not change with the size of the input. It means the algorithm runs in constant time, regardless of how large the input is.

**Example:**
```cpp
int getFirstElement(int arr[]) {
    return arr[0];
}

```

The above function always takes the same amount of time to execute regardless of the array size.

### 2. **O(log n) – Logarithmic Time**

An algorithm is O(log n) if the time taken grows logarithmically with respect to the input size. This usually occurs in algorithms that divide the problem space in half at each step, such as binary search.

**Example:**
```cpp
int binarySearch(int arr[], int target, int left, int right) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1; // not found
}
```

Binary search divides the search space in half each time, resulting in a logarithmic time complexity.

### 3. **O(n) – Linear Time**

An algorithm is O(n) if the execution time grows linearly with the input size. The time complexity increases in direct proportion to the size of the input.

**Example:**
```cpp
int findMax(int arr[], int size) {
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}
```

The time complexity here is O(n) because the algorithm needs to look at each element of the array once.

### 4. **O(n log n) – Linearithmic Time**

Algorithms that perform a logarithmic operation on each element of the input are typically O(n log n). Many efficient sorting algorithms, such as quicksort and mergesort, have this time complexity.

**Example:**
```cpp
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}
```

Mergesort divides the array and recursively sorts each half, resulting in an O(n log n) time complexity.

### 5. **O(n²) – Quadratic Time**

An algorithm has O(n²) time complexity if its execution time is proportional to the square of the input size. This is common in algorithms with nested loops, such as bubble sort.

**Example:**
```cpp
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}
```

Bubble sort compares each element to every other element, leading to quadratic time complexity.

### 6. **O(2^n) – Exponential Time**

An algorithm with O(2^n) time complexity grows exponentially as the input size increases. These algorithms are usually inefficient for large inputs.

**Example:**
```cpp
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
```

The Fibonacci recursive function exhibits exponential growth because it recalculates values multiple times for the same inputs.

### 7. **O(n!) – Factorial Time**

An algorithm with O(n!) time complexity grows at a factorial rate. This happens in certain algorithms that try all permutations of an input set, such as solving the traveling salesman problem.

**Example:**
```cpp
// Generating permutations of an array (brute force)
void permute(int arr[], int l, int r) {
    if (l == r) {
        print(arr); // Output a permutation
    } else {
        for (int i = l; i <= r; i++) {
            swap(arr[l], arr[i]);
            permute(arr, l + 1, r);
            swap(arr[l], arr[i]); // backtrack
        }
    }
}
```

The number of permutations of an input of size `n` is `n!`, leading to factorial time complexity.

## Space Complexity

In addition to time complexity, Big O notation also describes space complexity, which measures the amount of memory an algorithm uses relative to the input size.

### **Common Space Complexities:**

- **O(1) – Constant Space**: The algorithm uses a fixed amount of memory.
- **O(n) – Linear Space**: The memory required increases linearly with the input size.

## Best, Worst, and Average Case

- **Best case**: The scenario in which the algorithm performs the least work (e.g., finding the element at the first position).
- **Worst case**: The scenario in which the algorithm performs the most work (e.g., searching for an element in the entire array).
- **Average case**: The expected performance for typical inputs.

## Conclusion

Big O notation provides a way to express the efficiency of algorithms. Understanding Big O helps you choose the right algorithm for a problem, considering the trade-off between time and space. The goal is to design algorithms that scale well as the input size increases.

---

### **Further Reading**:

- [Wikipedia - Big O Notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
