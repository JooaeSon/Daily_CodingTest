T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    card_lst = map(int, input())
    card_info = [0] * 10

    for c in card_lst:
        card_info[c] = card_info[c] + 1

    # 카드 장수 제일 많은 것 선택
    maxim = -1000000
    for i in range(len(card_info)):
        if maxim <= card_info[i]:
            maxim = card_info[i]
            cardNum = i

    print(f'#{test_case} {cardNum} {maxim}')