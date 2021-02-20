def solution(tickets):
    dic = {}
    for ticket in tickets:  # 목록화
        if ticket[0] not in dic:
            dic[ticket[0]] = list()
        dic[ticket[0]].append(ticket[1])

    for key, value in dic.items():  # 알파벳 순서 고려를 위한 내림차순
        dic[key].sort(reverse=True)

    answer = []
    stack = ["ICN"]
    while stack:
        top = stack[-1]
        if top not in dic or len(dic[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(dic[top].pop())

    answer.reverse()

    return answer