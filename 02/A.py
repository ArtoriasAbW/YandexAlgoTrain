a = int(input())
max_value = a
max_count = 1

while a != 0:
    a = int(input())
    if a > max_value:
        max_value = a
        max_count = 1
    elif a == max_value:
        max_count += 1
print(max_count)