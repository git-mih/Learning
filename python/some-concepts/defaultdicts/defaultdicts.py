from collections import defaultdict

d = defaultdict(int)

with open('cars_2014.csv') as f:
    next(f)
    for row in f:
        mk, _ = row.strip('\n').split(',')
        d[mk] += 1

for k, v in d.items():
    print(f'{k}: {v}')
