def forward(s):
    idx = 1
    while idx < len(s):
        print(s[:idx])
        idx += 1


def backward(s):
    idx = len(s)
    while idx > 0:
        print(s[:idx])
        idx -= 1


s = list(input())
forward(s)
backward(s)
