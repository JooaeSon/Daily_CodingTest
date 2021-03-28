def solution(s):
    answer = True
    # 올바른 괄호 찾기
    stack = []
    stack.append(s[-1])
    for i in range(len(s) - 2, -1, -1):
        if len(stack) == 0:
            stack.append(s[i])
            continue
        if stack[-1] == ")" and s[i] == "(":
            stack.pop()
            continue
        else:
            stack.append(s[i])

    if len(stack) != 0:
        answer = False

    return answer