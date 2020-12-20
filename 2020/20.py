s = open('input').read().split('\n\n')
l = []
def add(x):
    global l
    l.append(tuple(x))
    l.append(tuple(reversed(x)))

from collections import Counter
for tile in s:
    tile = tile.split('\n')[1:]
    add(tile[0])
    add(tile[-1])
    add([line[0] for line in tile])
    add([line[-1] for line in tile])
l = [''.join(item) for item in l]
d = dict(Counter(l))
works = set()
for key in d:
    if d[key] == 2:
        works.add(key)
borders = []
for key in d:
    if key[::-1] not in works and d[key] == 1:
        borders.append(key)
fans = 1
for til in s:
    tile = til.split('\n')[1:]
    poss = [tile[0],tile[-1],''.join([line[0] for line in tile]),''.join([line[-1] for line in tile])]
    ans = sum([fg in borders for fg in poss])
    if ans == 2:
        fans *= int(til.split('\n')[0].split()[-1][:-1])
print(fans)
    