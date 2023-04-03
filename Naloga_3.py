content = open("input3.txt", encoding="utf8").readlines()
tecajHU = 390
meso = {'1003':4.8,
        '1005':5.5,
        '1006':5.2,
        '1024':4.5,
        '1028':5.4,
        '1095':4.6}
totalkg = 0
totaleuro = 0
totalforint = 0

for line in content:
    line = line.replace('\n','')
    m, k = line.split()
    eur = meso[m]
    kg, batch = k.split('x')
    totalkg += int(kg)
    batch = batch.replace('kg','')
    totaleuro += int(kg)*int(batch)*eur

paid = (totaleuro+2800)*tecajHU
tecajSI = paid/totaleuro
print(int(tecajSI))