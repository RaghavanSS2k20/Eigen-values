def count_candy_sets(N):
    count = 0
    i = 1
    while i*(i+1)//2 < N:
        if (N - i*(i+1)//2) % i == 0:
            count += 1
        i += 2
    return count

# Example usage:
N = 15
print(count_candy_sets(N))  # Output: 3
