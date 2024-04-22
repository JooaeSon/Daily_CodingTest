a, b = map(int, input().split())
d, c = map(int, input().split())

denominator = b*c # 분모
numerator = a*c+b*d # 분자

# 최대공약수
def GCD(x,y):
    while y:
        x, y = y, x%y
    return x

gcd = GCD(numerator, denominator)
numerator = int(numerator/gcd)
denominator = int(denominator/gcd)

print(numerator, denominator)