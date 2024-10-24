# uses the sys library for optimization - it makes your inputs faster, that's it
import sys
input = sys.stdin.readline

# this question uses a stack, we'll learn this soon!
t = int(input()) # number of test cases
for i in range(t):
    n = int(input()) # number of cars
    
    train = [] # train carries all cars, order matters here
    for j in range(n):
        car = int(input()) # car number
        train.append(car) # takes in from top to bottom
    train.reverse() # since the car lets go of its cars from bottom to top, see sample input diagram

    stack = [] # initialize stack, in this case it's the branch
    expect = 1 # looking for car 1 at the beginning
    for j in train:
        stack.append(j) # send the cars from the train to the branch
        while stack and stack[-1] == expect: # if the stack still exists and the last one is the desired car number
            stack.pop() # pop the desired car number at the end of the branch to the lake
            expect += 1 # now looking for next car number, e.g. from 1 to 2

    if len(stack) == 0: # if the stack is empty, job is completed and cars have went to lake
        print('Y')
    else: # impossible case, stack cannot move out the cars
        print('N')