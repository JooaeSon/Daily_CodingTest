T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N = int(input())

    entral = 9
    part = 9
    for i in range(1, N):
        part *= (10 - i)
        entral *= 10

    result = '%.5f' % round(part / entral, 5)
    print(f'#{test_case} {result}')
