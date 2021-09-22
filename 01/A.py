def interactor():
    r = int(input()) # return code
    i = int(input()) # interactor
    c = int(input()) # checker
    if i == 0:
        if r != 0:
            return 3
        return c
    if i == 1:
        return c
    if i == 4:
        if r != 0:
            return 3
        return 4
    if i == 6:
        return 0
    if i == 7:
        return 1
    return i

print(interactor())