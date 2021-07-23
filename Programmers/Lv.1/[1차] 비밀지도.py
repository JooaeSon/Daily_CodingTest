'''2차 풀이 '''

def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        stream = (n - len(bin(i | j)[2:])) * '0' + str(bin(i | j)[2:])
        stream = stream.replace('0', ' ')
        stream = stream.replace('1', '#')
        answer.append(stream)

    return answer


''' 1차 풀이
def solution(n, arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        decryption1 = (n - len(bin(arr1[i])[2:])) * '0' + str(bin(arr1[i])[2:])
        decryption2 = (n - len(bin(arr2[i])[2:])) * '0' + str(bin(arr2[i])[2:])

        stream = ''
        for j in range(len(decryption1)):
            if (int(decryption1[j]) + int(decryption2[j])) == 2 or (int(decryption1[j]) + int(decryption2[j])) == 1:
                stream += '#'
            else:
                stream += ' '
        answer.append(stream)

    return answer
'''