n, m, k = [int(x) for x in input().split()]

farm = [m for i in range(n)] # initialize a farm full of potatoes
for i in range(m):
    a, b = [int(x) for x in input().split()]
    farm[i] -= (b-a+1)

