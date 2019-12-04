nice_string_count = 0

f = open('input')
for line in f:
    string = line.strip('\n')
    vowels_seen = []
    has_three_vowels = False
    has_seq_pair = False
    has_forbidden_pair = False
    for i in range(0, len(string)):
        char = string[i]
        if not has_three_vowels and char in ['a', 'e', 'i', 'o', 'u']:
            vowels_seen.append(char)
            if len(vowels_seen) == 3:
                has_three_vowels = True
        
        if not has_seq_pair and i > 0:
            if string[i-1] == char:
                has_seq_pair = True

        if not has_forbidden_pair and i > 0:
            preceding_pair = string[i-1] + char
            if preceding_pair in ['ab', 'cd', 'pq', 'xy']:
                has_forbidden_pair = True

    if has_three_vowels and has_seq_pair and not has_forbidden_pair:
        nice_string_count += 1

print(nice_string_count)