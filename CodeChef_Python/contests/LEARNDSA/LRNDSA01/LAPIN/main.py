from collections import Counter

T = int(input())

for _ in range(T):
    string = [i for i in input()]
    length = len(string)

    if length % 2 != 0:
        del string[length // 2]
        length = len(string)

    start = Counter(''.join(string[:length // 2]))
    end = Counter(''.join(string[length // 2:]))

    if start == end:
        print('YES')
    else:
        print('NO')
