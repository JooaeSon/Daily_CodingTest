array = [1, 5, 2, 6, 3, 7, 4]  # array 배열 설정
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []

    for i in commands:
        temp = array[i[0] - 1:i[1]]

        # 이제 자른 것을 정렬하기.
        temp.sort()
        sorted(temp)

        # 정렬된 값 중 k 번째 수 가져오기, 그리고 answer 리스트에 집어 넣기.
        answer.append(temp[i[2] - 1])
    return answer