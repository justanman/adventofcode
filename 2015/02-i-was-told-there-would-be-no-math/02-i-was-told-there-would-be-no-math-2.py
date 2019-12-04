f = open('input', 'r')

total = 0
for dim in f:
    dim = dim.strip('\n')
    dim_array = dim.split('x')
    l = int(dim_array[0])
    w = int(dim_array[1])
    h = int(dim_array[2])

    per_side_a = (2*l) + (2*w) 
    per_side_b = (2*w) + (2*h) 
    per_side_c = (2*h) + (2*l) 

    bow_size = l*w*h

    total = total + bow_size + min(per_side_a, per_side_b, per_side_c)

print(total)