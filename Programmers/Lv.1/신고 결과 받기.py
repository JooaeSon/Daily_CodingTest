from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    declaration_from_to = defaultdict(set)
    reported_id = defaultdict(int)

    # 누가 신고 했고 신고 당했는지 정보 dict
    for keyword in report:
        declaration_from_to[keyword.split()[0]].add(keyword.split()[1])

    # 각 사람당 신고당한 횟수 정리
    for item, val_set in declaration_from_to.items():
        for v in val_set:
            reported_id[v] += 1

    # k 이상 신고당한 사람 정지 시킴
    stopped = set()
    for item, val in reported_id.items():
        if val >= k:
            stopped.add(item)

    # 신고한 유저가 받을 메일 갯수 확인
    for item, val in declaration_from_to.items():
        answer[id_list.index(item)] = len(stopped & val)

    return answer