f = open('input', 'r')

current_coord = [0, 0]
santa_current_coord = [0, 0]
robot_current_coord = [0, 0]

visited = {
    '0,0': 2
}

santas_turn = True

for direction in f.readline():
    if santas_turn:
        current_coord = santa_current_coord
    else:
        current_coord = robot_current_coord

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

    santas_turn = not santas_turn

print(len(visited))