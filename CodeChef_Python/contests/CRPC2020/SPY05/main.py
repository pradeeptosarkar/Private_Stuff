summed = 0
multiplied = 1

for char in input():
    char = int(char)
    summed += char
    multiplied *= char

if summed == multiplied:
    print('spy number')
