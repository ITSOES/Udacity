from collections import Counter, defaultdict
from itertools import combinations as combo
from time import time
d = defaultdict(set)
i=time()
with open('Marvel Graph.tsv') as f:
    for line in f.read().split('\n'):
        if not d.keys():
            print(time()-i, 'i')
        # if len(line.split())
        x, y = [h.strip('\"') for h in line.split('"\t"')]
        d[x].add(y)
        # print i
        # print(x, y)
print(time()-i)

weights = {}
ex =time()

t = max(((x,y) for x,y in combo(d,2) if d[x]&d[y]), key=lambda e:len(d[e[0]] & d[e[1]]))
# t = max(combo(d,2), key=lambda e: len(d[e[0]] & d[e[1]]))
# t = {(x,y): len(d[x] & d[y]) for x,y in combo(d,2) if d[x]&d[y]}
r =time()-ex
print(r, 'the time')
print(len(d), len(t), t)
# print(max(t, key=t.get))
# print(d[t[0]] & d[t[1]])
print('finished:', time()-i)

