TC = int(input())

for tc in range(1, TC + 1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')