def solution(s):
    answer = ''

    for word in list(s.split(" ")):
        for i in range(len(word)):
            if i % 2:
                answer += word[i].lower()
            else:
                answer += word[i].upper()

        answer += ' '

    return answer[:-1]