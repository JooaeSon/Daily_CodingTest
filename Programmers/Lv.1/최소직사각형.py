def solution(sizes):
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]

    sizes = list(map(list, zip(*sizes)))

    return max(sizes[0]) * max(sizes[1])