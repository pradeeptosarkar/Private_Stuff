T = int(input())

for _ in range(T):
    N, B, M = map(int, input().split())
    X = list(map(int, input().split()))

    array = [i for i in range(N)][::-1]
    blocks = []
    while array:
        current_block = []
        for element in range(B):
            if array:
                current_block.append(array.pop())
        blocks.append(current_block)

    cache = []
    cache_loads = 0
    heads = [i for i in range(N)][::B]
    for element in X:
        try:
            block = heads.index(element)
        except ValueError:
            block = heads.index(element - (element % B))

        if cache != blocks[block]:
            cache = blocks[block]
            cache_loads += 1

    print(cache_loads)
