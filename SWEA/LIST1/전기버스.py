T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())  # K:한번 충전으로 이동할 수 있는 거리, N:정류장 개수, M:충전기 설치수
    charge_lst = list(map(int, input().split()))
    result=0
    start = 0
    while True:
        #print("start:", start)
        for dist in range(K, 0, -1):
            #print("dist:", dist)
            #print("start+dist:", start+dist)
            if start+dist >= N:
                start = start + dist
                break

            if start+dist in charge_lst:
                start = start + dist
                result = result + 1
                break
        else:
            result = 0
            break

        if start >= N:
            break
    print(f'#{test_case} {result}')