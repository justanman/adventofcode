with open('input') as i:
    freq = 0
    for ln in i:
        freq += int(ln)
    print(freq)
