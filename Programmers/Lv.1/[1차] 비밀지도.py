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