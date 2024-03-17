#연습문제 8번
#최소공배수를 구하는 알고리즘
#202111417 조성훈 

def gcd(a, b):
    #유클리드 호제법을 사용하여 최대공약수(GCD)를 계산한다

    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    #최소공배수(LCM)

    return a * b // gcd(a, b)

a = 20
b = 40
print("최대공약수:", gcd(a, b))
print("최소공배수:", lcm(a, b))