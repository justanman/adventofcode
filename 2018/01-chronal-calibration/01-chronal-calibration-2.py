import itertools
with open('input') as i:
    freq = 0
    seen = {0}
    for ln in itertools.cycle(i):
        freq += int(ln)
        if freq in seen:
            print(freq)
            break
        seen.add(freq)
