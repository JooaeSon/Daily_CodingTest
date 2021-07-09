def solution(a, b):
    Day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    monthDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    dayCnt = 0
    month = 1
    while month < a:
        dayCnt += monthDays[month - 1]
        month += 1

    dayCnt += b

    return Day[(dayCnt - 3) % 7]