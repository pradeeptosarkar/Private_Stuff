from string import ascii_lowercase


N = int(input())
S = input()

value = 0
for char in S.lower():
    value += ascii_lowercase.index(char) + 1

print(str(value / N % 1)[2:3])
