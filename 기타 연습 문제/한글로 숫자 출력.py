# 숫자를 입력하면 그 숫자가 한글로 출력 된다.
# N의 범위는 0 <= num <= 1000000000000 (1조=10^12)
def solution(num):
    answer = ''
    note1 = ['', '십', '백', '천']
    note2 = ['', '만', '억', '조']
    note3 = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    # 일 십 백 천 / 만 십만 백만 천만 / 억 십억 백억 천억 / 조
    N = len(str(num))

    count = N
    while count != 0: # 6 151100 372900
        n3 = note3[int(str(num)[(N-count)])]
        if (count-1) % 4 == 0: # '', 만, 억, 조 단위는 4개의 단위 당 한번만 반복해준다.
            n2 = note2[(count-1) // 4]
        else:
            n2 = ''

        n1 = note1[(count-1)%4]

        if n3 == '': # n3가 가르키는것이 0일 때는 단위 붙일 필요 없음. ex) 99009: 구만 구천 백 십 구(x) -> 구만 구천 구 (O)
            n1 = ''

        if n3 == '일' and count != 1: # 마지막 일의 자리 숫자가 아니고 2, 3, 4,... 자리에 '일' 이라는 문자는 필요가 없다. ex) 100: 일백(x) -> 백
            n3 = ''

        answer += n3+n1+n2
        count -= 1

    print(answer)
    return answer


solution(1000045)