num = int(811281128112811281644112)
current = 1
steps = 0

while current < num:
    steps+=1
    foundb5 = False
    l = list(str(current))
    temp = reversed(l)
    for i, n in enumerate(temp):
        if int(n) > 5:
            p1 = ''.join(l[:len(l)-i-1])
            p2 = int(''.join(l[len(l)-i-1:]))
            p2 *= 2
            current = int(p1+str(p2))
            foundb5 = True
            break
    if foundb5 == False:
        current *= 2

print(steps)
