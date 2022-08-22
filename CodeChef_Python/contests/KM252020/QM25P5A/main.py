num = bin(int(input())).strip('0b')[::-1]
print(int(f'0b{num}', 2))
