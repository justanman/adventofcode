f = open('input', 'r')

total = 0
for dim in f:
    dim = dim.strip('\n')
    dim_array = dim.split('x')
    l = int(dim_array[0])
    w = int(dim_array[1])
    h = int(dim_array[2])

    area_side_a = l*w
    area_side_b = w*h
    area_side_c = h*l

    total = total + (2*area_side_a) + (2*area_side_b) + (2*area_side_c) + min(area_side_a, area_side_b, area_side_c)

print(total)