time = int(input())

chores = []

for i in range(int(input())): # fill up the chores list
    chore = int(input())
    chores.append(chore)

# order the chores from least to greatest, then do them from least to greatest
# this maximizes the number of chores you can do - best bang for your buck
chores.sort() 

chore_count = 0
for chore in chores:
    time -= chore # iterate through chores, subtract the time of each chore from total time

    if time >= 0: # as long as the chore is fully complete, chore_count is added by 1
        chore_count += 1
    else:
        break
  
print(chore_count)