T = int(input())

for i in range(T):
    N = int(input())
    A = [int(j) for j in input().split(' ')]
    result = ''

    initial_mean = 0
    for number in A:
        initial_mean += number
    mean = initial_mean / len(A)

    test_len = len(A) - 1
    for test in range(len(A)):
        test_mean = initial_mean - A[test]
        testing = test_mean / test_len

        if testing == mean:
            result = test + 1
            break
        else:
            result = 'Impossible'

    print(result)
