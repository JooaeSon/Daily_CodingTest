from itertools import combinations


def chcek_uniqueness(hubo, relation):
    row_len = len(relation)
    unique_lst = []

    for i in range(row_len):
        temp = []
        for h in hubo:
            temp.append(relation[i][h])
        if temp in unique_lst:
            return False
        unique_lst.append(temp)

    return True


def solution(relation):
    col_len = len(relation[0])
    lst = [i for i in range(col_len)]
    com = [list(combinations(lst, i)) for i in range(1, col_len + 1)]
    minimality_lst = []

    # 유일성 체크
    for i in range(len(com)):
        for j in range(len(com[i])):
            hubo = com[i][j]
            if chcek_uniqueness(hubo, relation):
                minimality_lst.append(hubo)

    # 최소성 체크
    answer = set(minimality_lst)
    for i in range(len(minimality_lst)):
        for j in range(i + 1, len(minimality_lst)):
            if len(minimality_lst[i]) == len(set(minimality_lst[i]).intersection(set(minimality_lst[j]))):
                answer.discard(minimality_lst[j])

    return len(answer)