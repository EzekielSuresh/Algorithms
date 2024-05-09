def memoized_cut_rod(p, n):
    r = [-1] * (n + 1)  # Array to store results of subproblems

    def memoized_cut_rod_aux(p, n, r):
        if r[n] >= 0:
            return r[n]  # If result for length n is already computed, return it
        if n == 0:
            q = 0  # Base case: rod of length 0 has no value
        else:
            q = float('-inf')
            for i in range(1, n + 1):
                q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))  # Recursive call
        r[n] = q  # Store the result for future reference
        return q  # Return the maximum revenue for rod of length n

    return memoized_cut_rod_aux(p, n, r)

# Example usage:
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # Prices for rods of length 1 to 10
rod_length = 8  # Length of the rod
max_revenue = memoized_cut_rod(prices, rod_length)
print("Maximum revenue:", max_revenue)
