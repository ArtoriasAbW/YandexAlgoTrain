n = int(input()) # max number
yes = set(range(1, n+1))
no = list()
data = input()
while data != "HELP":
    data = map(int, data.split())
    answer = input()
    if answer == "YES":
        yes = yes & set(data)
    else:
        no += data
    data = input()

ful_result = []
result = yes - set(no)
for el in result:
    if el <= n:
        ful_result.append(el)

for el in sorted(ful_result):
    print(el, end=" ")
print()

