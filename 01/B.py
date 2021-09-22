N, i, j = map(int, input().split())

track1 = abs(i - j) - 1
track2 = min(i, j) + (N - max(j,i) - 1)

print(min(track1, track2))
