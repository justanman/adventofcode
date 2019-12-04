nice_string_count = 0

f = open('input')
for line in f:
# for line in ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']:
    string = line.strip('\n')
    has_matching_pairs = False
    has_char_sandwich = False

    for i in range(1, len(string)):
        pair = string[i-1] + string[i]
        for j in range(i+2, len(string)):
            possible_match = string[j-1] + string[j]
            if pair == possible_match:
                has_matching_pairs = True

    for k in range(1, len(string) - 1):
        if not has_char_sandwich:
            if string[k-1] == string[k+1]:
                has_char_sandwich = True

    if has_matching_pairs and has_char_sandwich:
        nice_string_count += 1

print(nice_string_count)