T = int(input())

for _ in range(T):
    R, G, B, W, O = map(int, input().split())  # noqa: E741
    METERS = 100

    red_team = METERS / R
    other_teams = tuple(map(lambda x: METERS / x, (G, B, W, O)))
    if any([team < red_team for team in other_teams]):
        print(-1)
    else:
        print('Champions')
