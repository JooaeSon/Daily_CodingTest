def binary(num):
    # 이진수로 바꿔주기
    trans = ''

    while True:
        if num == 1 or num == 0:
            trans = str(num)+trans
            break
        trans = str(num % 2)+trans
        num = num // 2

    return trans


T = int(input())

for test_case in range(1, T + 1):
    N, string = map(str, input().split())
    lst = list(string)
    result = ''
    whole_result = ''

    for s in lst:
        num = 0
        if not s.isdigit():  # 숫자일 아닐 경우
            if s == 'A':
                num = 10
            elif s == 'B':
                num = 11
            elif s == 'C':
                num = 12
            elif s == 'D':
                num = 13
            elif s == 'E':
                num = 14
            elif s == 'F':
                num = 15
        else:
            num = int(s)

        result = binary(num)

        if len(result) < 4:
            i = 4-len(result)
            result = '0'*i+result

        whole_result = whole_result+result

    print(f'#{test_case} {whole_result}')