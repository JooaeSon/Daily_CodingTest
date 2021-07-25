def solution(dartResult):
    board = []

    pivot = 0
    while True:
        if pivot >= len(dartResult):
            break
        if dartResult[pivot].isdigit() and dartResult[pivot+1].isdigit():
            point=int(dartResult[pivot]+dartResult[pivot+1])
            pivot=pivot+1
        else:
            point = int(dartResult[pivot])

        bonus = dartResult[pivot + 1]
        if pivot+2 < len(dartResult):
            option = dartResult[pivot + 2]
        else: option = '-1'

        if bonus == 'S':
            point = point ** 1
        elif bonus == 'D':
            point = point ** 2
        else:
            point = point ** 3

        if not option.isalnum():
            if option=='*':
                if board: board[-1]*=2
                point*=2
            elif option=='#':
                point*=-1
            pivot = pivot + 3
        else:
            pivot = pivot + 2

        board.append(point)

    return sum(board)