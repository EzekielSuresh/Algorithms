def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    # Create left and right subarrays
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    # Copy data to left and right subarrays
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + 1 + j]

    # Add sentinel values at the end of L and R
    L[n1] = float('inf')
    R[n2] = float('inf')

    i = 0
    j = 0

    # Merge the subarrays back into A[p..r]
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

# Example usage
if __name__ == "__main__":
    A = [12, 11, 13, 5, 6, 7]
    print("Given array is:", A)
    merge_sort(A, 0, len(A) - 1)
    print("Sorted array is:", A)