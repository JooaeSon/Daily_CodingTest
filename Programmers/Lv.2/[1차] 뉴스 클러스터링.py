import math
import copy

def OPERATION(A, B):

    UNI = copy.deepcopy(A)
    INTER = []
    while B:
        b = B.pop()
        if b in A:
            A.remove(b)
            INTER.append(b)
        else:
            UNI.append(b)

    return [len(INTER), len(UNI)]


def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    A = [str1[i:i + 2] for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    B = [str2[i:i + 2] for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    if len(A) == 0 and len(B) == 0:
        return 1 * 65536

    oper = OPERATION(A, B)
    return math.floor(oper[0] / oper[1] * 65536)