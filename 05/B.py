n = int(input())

arr = list(map(int, input().split()))

result = arr[0]
cur_sum = 0

for el in arr:
    cur_sum += el
    result = max(result, cur_sum)
    cur_sum = max(cur_sum, 0)

print(result)