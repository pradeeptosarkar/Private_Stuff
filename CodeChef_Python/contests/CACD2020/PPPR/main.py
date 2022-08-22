def mcd(a, b):
    remainder = 0
    while b > 0:
        remainder = b
        b = a % b
        a = remainder
    return a


T = int(input())

for _ in range(T):
    A, B = [int(i) for i in input().split()]
    print(mcd(A, B))
