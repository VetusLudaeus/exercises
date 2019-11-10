# https://www.codingame.com/ide/puzzle/skynet-revolution-episode-1

import sys
import math

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
gateways = []
web = {}

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    web.setdefault(n1, []).append(n2)
    web.setdefault(n2, []).append(n1)
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.append(ei)


def search_deleted_link(skynet_agent_index, gateways):
    for i in gateways:
        if i in web[skynet_agent_index]:
            return [skynet_agent_index, i]
    for i in gateways:
        if len(web[i]) > 0:
            return [i, web[i][0]]


def delete_link(c1, c2):
    web[c1].remove(c2)
    web[c2].remove(c1)


# game loop
while True:
    skynet_agent_index = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    c1, c2 = search_deleted_link(skynet_agent_index, gateways)
    delete_link(c1, c2)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print("{0} {1}".format(c1, c2))

