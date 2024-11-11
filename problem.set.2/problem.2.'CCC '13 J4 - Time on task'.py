time = int(input())

chores = []

for i in range(int(input())):
    chore = int(input())
    chores.append(chore)

chores.sort() 

chore_count = 0
for chore in chores:
    time -= chore

    if time >= 0:
        chore_count += 1
    else:
        break
  
print(chore_count)