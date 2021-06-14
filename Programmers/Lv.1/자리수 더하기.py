def solution(n):
    answer = 0

    for i in str(n):  # 문자열에서 하나씩 문자 가져오기
        answer += int(i)

    return answer