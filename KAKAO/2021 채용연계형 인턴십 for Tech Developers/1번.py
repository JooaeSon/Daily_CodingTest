def solution(s):
    answer = ''
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    idx = 0
    stream = ''
    while idx < len(s):

        if s[idx].isdigit():  # 숫자라면
            answer += str(s[idx])
            stream = ''
        else:
            stream += s[idx]
            if stream in number:
                answer += str(number.index(stream))
                stream = ''

        idx += 1

    return int(answer)