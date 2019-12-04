import hashlib

f = open('input', 'r')

provided_key = f.readline()

for i in range(0, 1000000000):
    key = provided_key + str(i)
    current_hash = hashlib.md5(key.encode('utf-8')).hexdigest()
    if current_hash.startswith('000000'):
        print(i)
        break