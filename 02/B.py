# 10 домов
# 3 вида

buildings = list(map(int, input().split()))

# 1 жилой 2 магазин 0 офис
max_dist = 0
for index, building in enumerate(buildings):
    if building == 1:
        tmp_idx = index
        first_dist = 10
        while tmp_idx > 0 and buildings[tmp_idx] != 2:
            tmp_idx -= 1
        if buildings[tmp_idx] == 2:
            first_dist = abs(tmp_idx - index)
        tmp_idx = index
        second_dist = 10
        while tmp_idx < 9 and buildings[tmp_idx] != 2:
            tmp_idx += 1
        if buildings[tmp_idx] == 2:
            second_dist = abs(tmp_idx - index)
        cur_dist = min(first_dist, second_dist)
        if cur_dist > max_dist:
            max_dist = cur_dist
print(max_dist) 