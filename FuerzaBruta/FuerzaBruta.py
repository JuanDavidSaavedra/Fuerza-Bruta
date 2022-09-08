from time import time 

inicio = time()

for i in range(1, 100000):
    c = 0
    for j in range(1,(i // 2)+1):
        if(i % j == 0):
            c = c + j
    if (c == i):
        print("El número " + str(i) + " es un número perfecto ")
    else:
        print("El número " + str(i) + " no es un número perfecto ")

tiempo = time() - inicio
print("\nTiempo de ejecucción: ", tiempo)