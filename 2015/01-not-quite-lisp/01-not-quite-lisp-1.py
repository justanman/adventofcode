f = open('input')
parens = f.readline()
print(sum([1 if p == '(' else -1 for p in parens]))
