def solution(s):
    # k는 자르는 단위 갯수
    # i는 자르는 문자열의 시작
    min = len(s) * 100
    #an=[]
    for k in range(1, len(s) + 1):  # s="abcbadb" 7
        result = ''
        i = 0
        while i <= len(s)-k:
            cnt = 0
            string = s[i: i + k]
            #print("i:", i, "string:", string)
            while i <= len(s) - k:
                if s[i:i + k] != string:  # 일정 구간마다 같은 문자인지 비교
                    break
                i = i + k  # 일정 구간 만큼 더해줌
                cnt += 1  # 반복되는 횟수 측정
            if cnt >= 2:
                result = result + str(cnt)+string
            else:
                result += string
        else:
            result = result+s[i:]

        #an.append(result)
        if len(result) < min:
            min = len(result)

    # 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return
    return min