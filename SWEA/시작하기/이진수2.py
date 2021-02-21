T = int(input())

for test_case in range(1, T + 1):
    N = float(input())
    result = ''

    jisu = 1 / 2
    cnt = 0
    while True:
        #print(N)
        #print(jisu)
        if N == 0:
            break
        if cnt >= 13:
            result = 'overflow'
            break
        if N < jisu:
            jisu = jisu * (1/2)
            cnt += 1
            result += '0'
            continue

        N = N - jisu
        jisu = jisu * (1/2)
        cnt += 1
        result += '1'

    print(f'#{test_case} {result}')