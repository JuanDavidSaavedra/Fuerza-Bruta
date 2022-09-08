from time import time 

clave = int(input("Digite una clave: "))

x = [int(a) for a in str(clave)]

vector = []

for i in range(0,9):
    if i == x[0]:
        vector.append(i)
for j in range(0,9):
    if j == x[1]:
        vector.append(j)
for z in range(0,9):
    if z == x[2]:
        vector.append(z)
for y in range(0,9):
    if y == x[3]:
        vector.append
print(vector)
