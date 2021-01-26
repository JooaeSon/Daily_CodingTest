import heapq

def solution(operations):
    max_heap = []
    min_heap = []

    for operation in operations:
        direct, num = operation.split(' ')
        num = int(num)

        if direct == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-num, num))
        elif direct == 'D' and len(min_heap) != 0:
            if num == 1:
                heapq.heappop(max_heap)
                if max_heap == [] or max_heap[0][1] < min_heap[0]:
                    min_heap = []
                    max_heap = []
            elif num == -1:
                heapq.heappop(min_heap)
                if min_heap == [] or max_heap[0][1] < min_heap[0]:
                    min_heap = []
                    max_heap = []

    if len(min_heap) == 0:
        return [0, 0]
    else:
        return [max_heap[0][1], min_heap[0]]  # 최대값, 최소값