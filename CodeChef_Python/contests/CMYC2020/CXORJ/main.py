T = int(input())

total_tax = 0
for _ in range(T):
    s = [i for i in input()]
    current_tax = [0, 0]

    for char in s:
        if char.islower():
            current_tax[0] += 1
        elif char.isupper():
            current_tax[1] += 1

    total_tax += abs(current_tax[0] - current_tax[1])

print(total_tax)
