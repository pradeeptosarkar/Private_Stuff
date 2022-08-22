from string import ascii_lowercase


def rotate(word):
    vowels = ['a', 'e', 'i', 'o', 'u']

    new_word = []
    for char in word:
        try:
            idx = ascii_lowercase.index(char) + 1
            new_char = ascii_lowercase[idx]

            if new_char in vowels:
                new_word.append(new_char.upper())
            else:
                new_word.append(new_char)

        except IndexError:
            new_word.append('A')

    return ''.join(new_word)


T = int(input())

for _ in range(T):
    S = input().lower()
    print(rotate(S))
