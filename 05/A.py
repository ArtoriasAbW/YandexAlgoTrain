n, q = map(int, input().split())

arr = list(map(int, input().split()))

prefix_sum = [0]
sum_el = 0
for el in arr:
    sum_el += el
    prefix_sum.append(sum_el)

for _ in range(q):
    l, r = map(int, input().split())
    print(prefix_sum[r] - prefix_sum[l - 1])