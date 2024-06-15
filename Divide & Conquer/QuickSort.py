def partition(A, p, r):
    x = A[r]  # Choose the last element as pivot
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]  # Swap elements
    A[i + 1], A[r] = A[r], A[i + 1]  # Move pivot to its correct position
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)  # Partition the array
        quicksort(A, p, q - 1)  # Recursively sort the left part
        quicksort(A, q + 1, r)  # Recursively sort the right part

# Example usage:
A = [3, 6, 8, 10, 1, 2, 1]
quicksort(A, 0, len(A) - 1)
print(A)  # Expected output: [1, 1, 2, 3, 6, 8, 10]

