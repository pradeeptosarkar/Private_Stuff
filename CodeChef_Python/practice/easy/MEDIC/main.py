from datetime import date
from datetime import timedelta

T = int(input())

for _ in range(T):
    year, month, day = [int(s) for s in input().split(':')]
    d = date(year, month, day)
    odd = d.day % 2
    count = 0

    while d.day % 2 == odd:
        d = d + timedelta(days=2)
        count += 1

    print(count)
