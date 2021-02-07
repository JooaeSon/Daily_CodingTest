def BFS(start_node):
    global result
    Q.append(start_node)
    visited[start_node] = 1

    while Q:
        start_node = Q.pop(0)
        for next_node in range(1, v+1):
            if MyMap[start_node][next_node] and not visited[next_node]:
                Q.append(next_node)
                visited[next_node] = 1
                distance[next_node] = distance[start_node] +1
                if next_node == end_node:
                    result = distance[next_node]
                    return
    return

TC = int(input())
for tc in range(1, TC+1):
    v,e = map(int, input().split())
    MyMap = [[0] * (v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    distance = [0] * (v+1)

    for i in range(e):
        start, end = map(int, input().split())
        MyMap[start][end] = 1
        MyMap[end][start] = 1

    start_node, end_node = map(int, input().split())

    Q = []
    result = 0
    BFS(start_node)
    print(f'#{tc} {result}')