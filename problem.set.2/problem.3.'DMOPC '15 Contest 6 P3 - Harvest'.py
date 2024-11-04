def solve(length, lowest, array):
    shortest = length + 1
    first = 0
    total = 0

    for i in range(length):
        total += array[i]

        while total - array[first] >= lowest:
            total -= array[first]
            first += 1

        if total >= lowest:
            shortest = min(shortest, i - first + 1)
            
    if shortest < length + 1:
        return shortest
    else:
        return -1

n, m, k = [int(x) for x in input().split()]

columns = [m] + [0] * n

for i in range(m):
    a, b = [int(x) for x in input().split()]
    
    columns[a - 1] -= 1
    columns[b] += 1

for i in range(1, n + 1):
    columns[i] += columns[i - 1]

width = solve(n, k, columns)
print(width)