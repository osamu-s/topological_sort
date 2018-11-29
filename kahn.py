#!/usr/bin/env python3

edge = [ {1, 3},
         {3},
         {},
         {2} ]


def inverse(e):
    inv_e = [set() for i in e]
    for i, a in enumerate(e):
        for n in a:
            inv_e[n].add(i)
    return inv_e


def khan(e):
    inv_e = inverse(e)
    s = [ i for i, n in enumerate(inv_e) if len(n) == 0 ]
    l = list()

    while len(s) > 0:
        n = s.pop()
        l.append(n)
        for m in edge[n]:
            inv_e[m].remove(n)
            if len(inv_e[m]) == 0:
                s.append(m)

    if sum([len(e) for e in inv_e]) > 0:
        print('error', l, s, inv_e)
    else:
        print(l)


def main():
    #print(edge)
    #print(inverse(edge))
    khan(edge)

if __name__ == '__main__':
    main()
