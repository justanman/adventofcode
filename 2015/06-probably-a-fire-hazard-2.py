import cProfile
import helper
import re

def convert(coord):
    return list(map(int, coord.split(',')))

def part2():
    matrix = [[0]*1000 for i in range(1000)]
    on_count = 0

    with open('input/input6.txt') as f:
        for line in f.readlines():
            line = line.strip('\n')
            coords = re.findall(r'\d{1,3},\d{1,3}', line)
            coords = list(map(convert, coords))

            begin_x = coords[0][0]
            begin_y = coords[0][1]
            end_x = coords[1][0]
            end_y = coords[1][1]

            action = None            

            if line.startswith('turn on'):
                action = 'turn on'
            elif line.startswith('toggle'):
                action = 'toggle'
            elif line.startswith('turn off'):
                action = 'turn off'

            for y in range(begin_y, end_y+1):
                for x in range(begin_x, end_x+1):
                    if action == 'turn_on':
                        matrix[y][x] += 1
                    elif action == 'toggle':
                        matrix[y][x] += 2
                    elif action == 'turn_off':
                        if matrix[y][x] > 0:
                            matrix[y][x] -=1

        for y in range(0, 999+1):
            for x in range(0, 999+1):
                on_count += matrix[y][x]

        print(on_count)

print('this one is noticeably slow. try making it faster. blog post? use profiler')
cProfile.run('part2()')