import heapq


def solution(n, works):
    answer = 0
    heap = []

    for work in works:
        heapq.heappush(heap, (-work, work))

    while True:
        if n == 0:
            break
        work = heapq.heappop(heap)[1] - 1
        heapq.heappush(heap, (-work, work))
        n -= 1  # 시간 감소

    for h in heap:
        if h[1] < 0:
            continue
        answer += h[1] ** 2

    return answer