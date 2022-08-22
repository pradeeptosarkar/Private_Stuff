def calculate_score(problems, scores):
    max_scores = {}
    count = 0
    for p in range(len(problems)):
        if problems[p] < 9:
            if problems[p] not in max_scores.keys():
                max_scores[problems[p]] = scores[p]
                count += 1
            else:
                if scores[p] > max_scores[problems[p]]:
                    max_scores[problems[p]] = scores[p]

    score = sum([s for s in max_scores.values()])
    return score if score else 0


T = int(input())
for i in range(T):
    P = []
    S = []
    N = int(input())
    for j in range(N):
        input_ = input().split()
        P.append(int(input_[0]))
        S.append(int(input_[1]))
    print(calculate_score(P, S))
