from collections import Counter

numbers = list(map(int, input().split()))

counter = Counter(numbers)


for el in numbers:
    if counter[el] == 1:
        print(el, end=" ")
print()