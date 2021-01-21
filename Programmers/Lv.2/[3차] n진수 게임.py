def transAlpha(num):
    if num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'


def calculate(jinsu, amount):
    result = '0'
    for num in range(1, amount + 1):
        s = ''
        while num != 0:
            if num % jinsu >= 10:
                s = transAlpha(num % jinsu) + s
            else:
                s = str(num % jinsu) + s
            num = num // jinsu

        result += s

    return result


def solution(n, t, m, p):
    # 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
    answer = ''

    cal_result = calculate(n, t * m)
    p -= 1
    while len(answer) != t:
        answer += cal_result[p]
        p += m

    return answer