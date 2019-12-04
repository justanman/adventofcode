f = open('input', 'r')
floor = 0
position = 0
for paren in f.readline():
    if paren == '(':
        floor += 1
    elif paren == ')':
        floor -= 1
    position += 1

    if floor == -1:
        print(position)
        break