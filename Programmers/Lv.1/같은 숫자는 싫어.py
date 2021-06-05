def solution(s):
    result = []
    for i, v in enumerate(s):
        if i == 0:
            result.append(v)
        elif s[i-1] == v:
            continue
        else:
            result.append(v)
    return result