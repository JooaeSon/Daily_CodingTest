def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = list()
        dic[genres[i]].append((i, plays[i]))

    # 1.속한 노래가 많이 재생된 장르를 먼저 수록합니다.
    populer_dic = {}
    for i in range(len(genres)):
        if genres[i] not in populer_dic:
            populer_dic[genres[i]] = 0
        populer_dic[genres[i]] += plays[i]

    populer_lst = []
    for key, value in populer_dic.items():
        populer_lst.append((value, key))
    populer_lst = sorted(populer_lst, key=lambda x: -x[0])

    # 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
    # 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
    for i in range(len(populer_lst)):
        dic[populer_lst[i][1]] = sorted(dic[populer_lst[i][1]], key=lambda x: (-x[1], x[0]))

    for i in range(len(populer_lst)):
        lst = dic[populer_lst[i][1]]
        if len(lst) >= 2:
            for j in range(2): answer.append(lst[j][0])
        else:
            answer.append(lst[0][0])

    return answer