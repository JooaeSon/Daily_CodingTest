import heapq


def solution(jobs):
    answer, last = 0, -1
    jobs.sort()
    heap = []
    count = 0
    time = jobs[0][0]
    while count < len(jobs):
        # 디스크가 작업중 요청들어오는 작업만 heap으로 담기
        for i in range(len(jobs)):
            s, t = jobs[i]
            if last < s <= time:
                heapq.heappush(heap, (t, s))  # 나중에 작업시간이 짧은 애부터 먼저 실행 시키기 위해
        if len(heap) != 0:  # 바로 수행할 수 있는 작업이 있는 경우
            count += 1
            last = time
            work, start = heapq.heappop(heap)
            time += work
            answer += (time - start)
        else:  # 바로 수행할 수 있는 작업이 없는 경우
            time += 1

    return answer // len(jobs)