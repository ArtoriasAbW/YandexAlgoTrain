import sys
from collections import Counter

counter = dict()

for line in sys.stdin:
    for word in line.split():
        if word in counter:
            counter[word] +=1
        else:
            counter[word] = 1 

res = list((counter[k], k) for k in counter)

res.sort(key=lambda el: (-el[0], el[1]))

for el in res:
    print(el[1])