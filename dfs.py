#!/usr/bin/env python3

edge = [ {1, 3},
         {3},
         {},
         {2} ]

# l: result list
l = list()
state = ['notvisited'] *len(edge)

def visit(node):
    if state[node] == 'parmanent':
        return
    if state[node] == 'tmporary':
        print('error', l, node)
        exit(1)
    state[node] = 'tmporary'
    for neigh in edge[node]:
        visit(neigh)
    state[node] = 'parmanent'
    l.insert(0, node)


def main():
    #print(edge)

    for node in range(len(edge)):
        visit(node)
    print(l)


if __name__ == '__main__':
    main()
