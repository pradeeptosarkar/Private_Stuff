test_cases = int(input())

while test_cases > 0:
    read_count = 0
    score_dict = {}

    while read_count < 12:
        input_string = input().split()
        team1 = input_string[0]
        team2 = input_string[4]
        goal1 = int(input_string[1])
        goal2 = int(input_string[3])
        team1_score = score_dict.get(team1, [0, 0])
        team2_score = score_dict.get(team2, [0, 0])

        if goal1 > goal2:
            team1_score[0] += 3
        elif goal1 == goal2:
            team1_score[0] += 1
            team2_score[0] += 1
        else:
            team2_score[0] += 3

        team1_score[1] += goal1 - goal2
        team2_score[1] += goal2 - goal1
        score_dict[team1] = team1_score
        score_dict[team2] = team2_score
        read_count += 1

    # print(score_dict)

    first_team = None
    second_team = None

    for k, v in score_dict.items():

        if first_team is None:
            first_team = k

        elif v[0] > score_dict[first_team][0]:
            second_team = first_team
            first_team = k

        elif v[0] == score_dict[first_team][0] and v[1] > score_dict[first_team][1]:
            second_team = first_team
            first_team = k

        elif second_team is None:
            second_team = k

        elif v[0] > score_dict[second_team][0]:
            second_team = k

        elif v[0] == score_dict[second_team][0] and v[1] > score_dict[second_team][1]:
            second_team = k

    print(first_team, second_team)
    test_cases -= 1
