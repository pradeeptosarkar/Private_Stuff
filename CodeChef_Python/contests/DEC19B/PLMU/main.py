from collections import deque
import sys

lines = deque([line.strip() for line in sys.stdin.readlines()])
T = int(lines.popleft())
for _ in range(T):
    N = int(lines.popleft())
    A = list(map(int, lines.popleft().split()))

    pairs = set()
    count1 = 0
    for num1 in A:
        count1 += 1
        count2 = 0
        for num2 in A[count1:]:
            count2 += 1
            if num1 + num2 == num1 * num2:
                pairs.add((count1, count2 + count1))

    sys.stdout.write(str(len(pairs)) + '\n')
