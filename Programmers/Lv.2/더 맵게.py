import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    factor = 0
    while scoville:
        if scoville[0] >= K:
            break
        elif len(scoville) == 1 and scoville[0] < K:
            return -1

        factor = heapq.heappop(scoville) + 2 * (heapq.heappop(scoville))
        heapq.heappush(scoville, factor)

        answer += 1

    return answer