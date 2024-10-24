question = int(input())
n = int(input()) # citizens in each country
c1 = sorted([int(x) for x in input().split()]) # country 1's cyclists sorted from slowest to fastest
c2 = sorted([int(x) for x in input().split()]) # country 2's cyclists sorted from slowest to fastest

total = 0

if question == 1: # answers question 1
# q1 is slowest possible speed
# logic is this: pair the slowest from c1 to slowest from c2, etc.
# since it's the max from both countries, this optimizes the amount of speed 'wasted'
    for i in range(n):
        speed = max(c1[i], c2[i])
        total += speed
else: # answers question 2
# q2 is fastest possible speed
# logic is this: pair the slowest from c1 to fastest from c2, etc.
# since it's the max from both countries, this optimizes the amount of speed used from each fastest cyclist
    for i in range(n):
        speed = max(c1[i], c2[-(i+1)])
        total += speed

print(total)