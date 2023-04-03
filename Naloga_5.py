import numpy as np
content = open("input5.txt", encoding="utf8").readlines()

A = []
a = []
i=0
for line in content:
    i+=1
    line = line.replace('\n','')
    if (len(line) < 26):
        line += ' '*(26-len(line))
    if (i % 26 != 0):
        a.append(list(line))
    else:
        a.append(list(line))
        A.append(a)
        a=[]
arr = np.array(A)

def move(z,y,x,way):
    if way == '-x': x -= 1
    elif way == '+x': x += 1
    elif way == '-y': y -= 1
    elif way == '+y': y += 1
    elif way == '-z': z -= 1
    elif way == '+z': z += 1
    return z,y,x

x = 2
y = 24
z = 2

c = arr[z,y,x]
way = '-y'
znamenje = ''

while c != '*':
    if c in ['<', '>', '^', 'v']:
        if way == '+x':
            if c == '^': way = '-y'
            elif c == 'v': way = '+y'
            elif c == '>': way = '-z'
            elif c == '<': way = '+z'
        elif way == '-x':
            if c == '^': way = '-y'
            elif c == 'v': way = '+y'
            elif c == '>': way = '+z'
            elif c == '<': way = '-z'
        elif way == '-y':
            if c == '^': way = '-z'
            elif c == 'v': way = '+z'
            elif c == '>': way = '+x'
            elif c == '<': way = '-x'
        elif way == '+y':
            if c == '^': way = '+z'
            elif c == 'v': way = '-z'
            elif c == '>': way = '+x'
            elif c == '<': way = '-x'
        elif way == '-z':
            if c == '^': way = '-y'
            elif c == 'v': way = '+y'
            elif c == '>': way = '+x'
            elif c == '<': way = '-x'
        elif way == '+z':
            if c == '^': way = '-y'
            elif c == 'v': way = '+y'
            elif c == '>': way = '+x'
            elif c == '<': way = '-x'
        z,y,x = move(z,y,x,way)
        c = arr[z,y,x]
    elif c.isupper():
        znamenje += c
        z,y,x = move(z,y,x,way)
        c = arr[z,y,x]
    elif c == ' ':
        z,y,x = move(z,y,x,way)
        c = arr[z,y,x]

print(znamenje)
