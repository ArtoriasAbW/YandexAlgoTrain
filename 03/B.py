memory = set()

numbers = map(int, input().split())

for number in numbers:
    if number not in memory:
        print("NO")
        memory.add(number)
    else:
        print("YES")