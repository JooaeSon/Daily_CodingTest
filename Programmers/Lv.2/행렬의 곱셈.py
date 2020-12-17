def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            k = 0
            temp = 0
            while k < len(arr1[0]):
                temp += arr1[i][k] * arr2[k][j]
                k += 1

            answer[i][j] = temp

    return answer