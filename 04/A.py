n = int(input())

res = dict()
for _ in range(n):
    color, number = map(int, input().split())
    if color not in res:
        res[color] = number
    else:
        res[color] += number

for key in sorted(res):
    print("{} {}".format(key, res[key]))
