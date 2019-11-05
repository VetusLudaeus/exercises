from typing import List

n = int(input("Enter the number of horses to compare "))
horses = []

for i in range(n):
    pi = int(input("Enter the horse strength under the number - " + str(i+1)))
    horses.append(pi)

horses.sort()
difference_horses: List[int] = []

for x in range(len(horses)-1):
    difference_horses.append(horses[x + 1] - horses[x])

print(min(difference_horses))