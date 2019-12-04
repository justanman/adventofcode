f = open('input', 'r')

current_coord = [0, 0]

visited = {
    '0,0': 1
}
for direction in f.readline():
    if direction == '^':
        current_coord[1] += 1
    elif direction == '>':
        current_coord[0] += 1
    elif direction == 'v':
        current_coord[1] -= 1
    elif direction == '<':
        current_coord[0] -= 1

    str_coord = str(current_coord[0]) + ',' + str(current_coord[1])
    if str_coord not in visited:
        visited[str_coord] = 1
    else:
        visited[str_coord] += 1

print(len(visited))