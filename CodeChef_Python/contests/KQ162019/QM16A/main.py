t = int(input())

first = []
second = []
for i in range(t):
    result = False
    n = input().lower().split(' ')
    m = input().lower().split(' ')

    for j in m:
        if j in n:
            result = True

    if result is True:
        print('Yes')
    else:
        print('No')
