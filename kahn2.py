#!/usr/bin/env python3

edge = [ {1, 3},
         {3},
         {},
         {2} ]

# change inverse edge matrix to dependency count
def dep_count(e):
    dep_mat = [0]*len(e)
    for a in e:
        for n in a:
            dep_mat[n] += 1
    return dep_mat


def khan(e):
    l = list()
    dep_mat = dep_count(e)
    s = [ i for i, n in enumerate(dep_mat) if n == 0 ]

    while len(s) > 0:
        n = s.pop()
        l.append(n)
        for m in e[n]:
            dep_mat[m] -= 1
            if dep_mat[m] == 0:
                s.append(m)

    if sum(dep_mat) > 0:
        print('error', l, s, dep_mat)
    else:
        print(l)


def main():
    #print(edge)
    #print(dep_count(edge))
    khan(edge)

if __name__ == '__main__':
    main()
