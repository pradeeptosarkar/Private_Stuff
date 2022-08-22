T = int(input())


def calculate(K, A):
    storage = 0
    count = 1
    for i in A:
        if i > K:
            storage += i - K
        elif i < K:
            storage -= K - i
            if storage < 0:
                return f'NO {count}'
        count += 1
    return 'YES'


for i in range(T):
    N, K = map(int, input().split())  # Days, Grams of protein each day
    A = list(map(int, input().split()))  # Grams buyed each day
    result = calculate(K, A)
    print(result)
