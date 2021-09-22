string = input()
count = 0
for i in range(0, len(string) // 2):
    if string[i] != string[len(string) - i - 1]:
        count += 1
print(count)