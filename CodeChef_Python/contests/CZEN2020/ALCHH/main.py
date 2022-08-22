import string

S = input()

vowels = set(('A', 'E', 'I', 'O', 'U'))
consonants = set(string.ascii_uppercase).difference(vowels)

consecutive_vowels = False
consonant_count = 0
for i in range(len(S)):
    if S[i] in vowels and S[i + 1] in vowels and S[i + 2] in vowels:
        consecutive_vowels = True
    elif S[i] in consonants:
        consonant_count += 1

if consecutive_vowels is True and consonant_count >= 5:
    print('GOOD')
else:
    print(-1)
