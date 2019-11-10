from typing import List

n = int(input())
horses = []

for i in range(n):
    pi = int(input())
    horses.append(pi)

horses.sort()
difference_horses: List[int] = []

for x in range(len(horses)-1):
    difference_horses.append(horses[x + 1] - horses[x])

print(min(difference_horses))