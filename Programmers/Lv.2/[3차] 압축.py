def solution(msg):
    answer = []

    dictionary = [chr(i) for i in range(65, 91)]
    dictionary.insert(0, 0)

    i = 0
    while True:
        k = 0
        if i >= len(msg):
            break

        for j in range(i + 1, len(msg) + 1):
            if msg[i:j] not in dictionary:
                k = j - 1
                break
        else:
            k = len(msg)

        w = msg[i:k]
        answer.append(dictionary.index(w))
        if k < len(msg):
            c = msg[k]
            dictionary.append(w + c)

        i = k

    return answer