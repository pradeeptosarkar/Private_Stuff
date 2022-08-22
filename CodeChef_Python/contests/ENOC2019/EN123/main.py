# cook your dish here
T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print('YES' if sum(A) <= K else 'NO')
