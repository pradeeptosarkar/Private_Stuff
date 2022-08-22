T = int(input())

for _ in range(T):
    N = int(input())
    NUMS = set(map(int, input().split()))

    s1 = 0
    s2 = 0
    for num in NUMS:
        if abs(num) != num:
            s2 += num
        else:
            s1 += num
    print(s1, s2)
