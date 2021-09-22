L, K = map(int, input().split())

blocks = list(map(int, input().split()))

if L % 2 and L // 2 in blocks:
    print(L // 2)
else:
    mem_blocks = blocks.copy()
    blocks.reverse()
    for block in blocks:
        if block < L // 2:
            print(block, end=' ')
            break
    for block in mem_blocks:
        if block >= L // 2:
            print(block)
            break