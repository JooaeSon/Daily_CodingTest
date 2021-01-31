from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N개의 화덕, M개의 피자
    cheeses = list(map(int, input().split()))
    pizzas = deque()
    for i in range(len(cheeses)):  # 각 피자당 치즈 인덱싱
        pizzas.append([i + 1, cheeses[i]])

    oven = deque()
    for i in range(N):  # 피자 오븐에 들어오라
        pizza = pizzas.popleft()
        oven.append(pizza)

    result = 0
    while True:  # 오븐에 굽기 시작
        if len(oven) == 1:
            lastPizza = oven.popleft()
            result = lastPizza[0]
            break

        pizza = oven.popleft()
        pizza[1] = pizza[1] // 2
        if pizza[1] != 0:  # 아직 피자가 완성 안됬다면 다시 오븐에 넣는다.
            oven.append(pizza)
        else:  # 피자가 하나가 완성되면? 새로운 피자를 오븐에 넣는다. 없음 말고
            if len(pizzas) != 0:
                pizza = pizzas.popleft()
                oven.append(pizza)

    print(f'#{test_case} {result}')