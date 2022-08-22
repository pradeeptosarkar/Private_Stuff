T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    total_damage = 0
    for item in A:
        if item & 0b1 == 0:
            total_damage += item

    print(total_damage)
