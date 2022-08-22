x, y = list(map(int, input().split()))

grid = {
    'filled': [],
    'empty': []
}

for i in range(x):
    line = input()

    for i, char in enumerate(line):
        if char == '#':
            grid['filled'].append(i)
        elif char == '.':
            grid['empty'].append(i)

if len(grid['filled']) > 1 and len(set(grid['filled'])) == 1:
    print(1)
else:
    print(0)
