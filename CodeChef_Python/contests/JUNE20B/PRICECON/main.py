T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    revenue_loss = 0
    for item_price in P:
        if item_price > K:
            revenue_loss += item_price - K

    print(revenue_loss)
