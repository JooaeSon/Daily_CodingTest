def findDifferMinium(num):
    tmp = num + 1

    while True:
        binNum, binTmp = bin(num)[2:], bin(tmp)[2:]
        s_binNum, s_binTmp = str(binNum), str(binTmp)

        if len(s_binNum)>len(s_binTmp):
            maxlength=len(s_binNum)
            s_binTmp='0'*(len(s_binNum)-len(s_binTmp))+s_binTmp
        else:
            maxlength = len(s_binTmp)
            s_binNum = '0' * (len(s_binTmp) - len(s_binNum)) + s_binNum

        flag = True
        cnt = 0
        i = -1
        while True:
            if s_binNum[i] != s_binTmp[i]:
                cnt += 1

            if cnt > 2:
                flag = False
                break

            if maxlength==abs(i):
                break
            i-=1

        if flag:
            return tmp
        tmp += 1


def solution(numbers):
    answer = []

    for number in numbers:
        answer.append(findDifferMinium(number))
    print(answer)
    return answer

solution([2,7])