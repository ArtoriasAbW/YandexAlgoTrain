from collections import OrderedDict

def check_sv(sv, number):
    for c in sv:
        if c not in number:
            return False
    return True

m = int(input())
sv_numbers = list()

for _ in range(m):
    sv_numbers.append(input())

n = int(input())

result = OrderedDict()
res_list = list()
max_value = 0

for _ in range(n):
    number = input()
    value = 0
    for sv in sv_numbers:
        if check_sv(sv, number):
            value += 1
    if value > max_value:
        max_value = value
    result[number] = value
    res_list.append(number)


print()
print()
for number in res_list:
    if result[number] == max_value:
        print(number)
