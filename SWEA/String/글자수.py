T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    dic = {}
    for s in str1:
        dic[s] = 0

    for value in str2:
        if value in dic:
            dic[value] += 1

    result = max(dic.values())
    print(f'#{test_case} {result}')
