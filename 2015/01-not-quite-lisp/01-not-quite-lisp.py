input = open('input')

parens = input.readline()

def part1():
    return sum([1 if p == '(' else -1 for p in parens])

def part2():
    floor = 0
    position = 0
    for paren in parens:
        if paren == '(':
            floor += 1
        elif paren == ')':
            floor -= 1
        position += 1

        if floor == -1:
            return position

if __name__ == '__main__':
	print(f'Answer 1: {part1()}')
	print(f'Answer 2: {part2()}')