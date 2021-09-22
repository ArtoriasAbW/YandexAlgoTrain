def is_correct(brackets):
    stack = list()
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

brackets = input()

print("YES" if is_correct(brackets) else "NO")