def solution(s, n):
    answer = ''

    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        else:
            num = ord(s[i]) + n
            if s[i].islower() and num > 122:
                num = num - 122 + 96
            elif s[i].isupper() and num > 90:
                num = num - 90 + 64
            answer = answer + chr(num)

    return answer