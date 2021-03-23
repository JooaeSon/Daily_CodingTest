from collections import deque

Gears = [deque(map(int, input())) for _ in range(4)]
k = int(input())
orders = deque(list(map(int, input().split())) for _ in range(k))

answer = 0

while orders:
    gear_num, direct = orders.popleft()
    gear_num -= 1
    tmp2, tmp6 = Gears[gear_num][2], Gears[gear_num][6]

    # 톱니바퀴 회전 시작
    Gears[gear_num].rotate(direct)
    tmp_direct=direct

    # 시작 톱니 왼쪽 방향
    direct=tmp_direct
    for i in range(gear_num-1, -1, -1):
        if Gears[i][2] != tmp6: # 서로 다른 극
            tmp6 = Gears[i][6]
            direct *= -1
            Gears[i].rotate(direct)
        else:
            break

    # 시작 톱니 오른쪽 방향
    direct = tmp_direct
    for i in range(gear_num+1, 4):
        if Gears[i][6] != tmp2: # 서로 다른 극
            tmp2 = Gears[i][2]
            direct *= -1
            Gears[i].rotate(direct)
        else:
            break

for i in range(4):
    if Gears[i][0] == 1:
        answer += 2**i

print(answer)