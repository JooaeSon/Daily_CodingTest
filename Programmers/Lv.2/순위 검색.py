from itertools import combinations
from collections import defaultdict


def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_val = int(info[-1])
        for i in range(5):
            # 하나의 info에서 경우의 수 16개 만들기
            for c in combinations(info_key, i):
                tmp_key = ''.join(c)
                # 가능한 info 조합을 key, 점수를 value로 딕셔너리에 저장
                info_dict[tmp_key].append(info_val)

    for key in info_dict.keys():
        # value 값 점수들은 오름차순으로 정리
        info_dict[key].sort()

    for query in queries:
        query = query.split(' ')
        query_score = int(query[-1])
        query = query[:-1]

        for i in range(3):
            query.remove('and')
        while '-' in query:
            query.remove('-')
        tmp_q = ''.join(query)

        # lower bound 사용해 query_score보다 큰 점수들의 개수 구하기
        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:  # 알맞는 점수 이분탐색
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)

    return answer