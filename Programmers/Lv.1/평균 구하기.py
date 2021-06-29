def solution(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]

    return sum / len(arr)