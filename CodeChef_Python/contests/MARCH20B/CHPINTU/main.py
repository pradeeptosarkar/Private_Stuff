T = int(input())

for _ in range(T):
    N, M = list(map(int, input().split()))
    F = [int(i) for i in input().split()]
    P = [int(i) for i in input().split()]

    prices = {}
    for i, v in enumerate(F):
        if v in prices:
            prices[v] += P[i]
        else:
            prices[v] = P[i]

    print(min(prices.values()))
