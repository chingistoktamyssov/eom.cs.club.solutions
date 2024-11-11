import sys
input = sys.stdin.readline

t = int(input()) 
for i in range(t):
    n = int(input()) 
    
    train = []
    for j in range(n):
        car = int(input())
        train.append(car) 
    train.reverse() 

    stack = []
    expect = 1
    for j in train:
        stack.append(j) 
        while stack and stack[-1] == expect:
            stack.pop()
            expect += 1

    if len(stack) == 0:
        print('Y')
    else:
        print('N')