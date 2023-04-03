import itertools
from math import floor

content = open("input4.txt", encoding="utf8").readlines()

cps = content[0].replace('\n','')
tps = content[1].replace('\n','')

cps_list = [int(i) for i in list(cps)]
tps_list = [int(i) for i in list(tps)]

#get proper key
AllKeyCombinations = list(itertools.product([0, 1], repeat=6))
key = [0,0,0,0,0,0]
for combination in AllKeyCombinations:
    x = list(combination[0:3])
    for i in range(3,6):
        xi = x[i-2] ^ x[i-3]
        x.append(xi)
    y = list(combination[3:6])
    for i in range(3,6):
        yi = y[i-1] ^ y[i-3]
        y.append(yi)
    start = []
    for i in range(6):
        z = x[i] ^ y[i]
        c = cps_list[i] ^ z
        start.append(c)
    if tps_list[0:6] == start:
        key[0:3] = x[0:3]
        key[3:6] = y[0:3]

x = key[0:3]
y = key[3:6]

#calculate x and y for remaining values
for i in range(3,len(tps_list)+1):
    xi = x[i-2] ^ x[i-3]
    yi = y[i-1] ^ y[i-3]
    x.append(xi)
    y.append(yi)

z = [x[i] ^ y[i] for i in range(len(x))]
b = [tps_list[i] ^ z[i] for i in range(len(tps_list))]

result = ''.join(str(v) for v in b)
step = floor(len(result)/7)

for i in range(0,len(result),step):
    row = result[i:i+step]
    print(row.replace('0',' ').replace('1','#'))