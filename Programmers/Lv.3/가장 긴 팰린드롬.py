def solution(s):
    size = []

    for i in range(len(s)):
        temp = 0
        while temp <= len(s):
            if s[i:temp] == s[i:temp][::-1]:
                size.append(len(s[i:temp]))
            temp += 1

    return max(size)