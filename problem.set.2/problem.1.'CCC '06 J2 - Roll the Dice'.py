n = int(input())
m = int(input())

ways = 0

# brute force, iterate through all possiblities of 1 to n and 1 to m that add up to 10
for i in range(1, n+1):
    for j in range(1, m+1):
        if i + j == 10:
            ways += 1

if ways == 1:
    print('There is 1 way to get the sum 10.') # account for the 1 way case b/c the sentence is slightly different
else:
    print('There are ' + str(ways) + ' ways to get the sum 10.')