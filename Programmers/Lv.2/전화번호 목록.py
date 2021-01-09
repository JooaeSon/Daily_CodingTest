def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j:
                if phone_book[j] in phone_book[i][:len(phone_book[j])]:
                    return False
    else:
        return True