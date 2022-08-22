num = int(input())
head = ''
while num > 0:
    line = head + (str(num) * num)
    head += str(num)
    num -= 1
    print(line)
