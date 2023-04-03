content = open("input.txt", encoding="utf8").readlines()

for i, line in enumerate(content):
    line = line.replace('\n','')
    num = int(line,  base=16)
    if num == 35210148:
        print('Line {} has value 35210148'.format(i+1))