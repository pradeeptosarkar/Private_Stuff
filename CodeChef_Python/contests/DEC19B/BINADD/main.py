def add_function(a, b):
    count = 0
    while b > 0:
        count += 1
        u = a ^ b
        v = a & b
        a = u
        b = v * 2
    return count


T = int(input())
for _ in range(T):
    A = int(input(), 2)
    B = int(input(), 2)
    print(add_function(A, B))
