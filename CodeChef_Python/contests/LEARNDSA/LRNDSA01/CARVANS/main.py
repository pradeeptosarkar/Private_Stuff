T = int(input())

for _ in range(T):
    N = int(input())
    speeds = list(map(int, input().split()))
    full_speed = 0
    car_ahead = speeds[0]

    for car in speeds:
        if car <= car_ahead:
            full_speed += 1
        else:
            car -= car - car_ahead

        car_ahead = car

    print(full_speed)
