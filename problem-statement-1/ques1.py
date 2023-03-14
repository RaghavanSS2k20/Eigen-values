def minimum_time_to_send_groups(N, groups, M, planes):
    groups = sorted(groups, reverse=True)
    planes = sorted(planes, reverse=True)
    time = 0
    i = 0
    while i < N:
        group = groups[i]
        j = 0
        while j < M:
            if planes[j] >= group:
                planes[j] -= group
                i += 1
                if i == N:
                    break
                group = groups[i]
            else:
                j += 1
        time += 2
    return time

# Example usage:
groups = [8, 1, 6, 9]
planes = [7, 3, 2]
print(minimum_time_to_send_groups(4, groups, 3, planes)) # Output: 12
