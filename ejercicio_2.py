a = int(input("Ingrese las ventas del producto A: "))   
b = int(input("Ingrese las ventas del producto B: "))   
c = int(input("Ingrese las ventas del producto C: "))   

if a > b and a > c:
    print("Las ventas del producto A son las más elevadas") 
elif b > a and b > c: 
    print("Las ventas del producto B son las más elevadas")
elif c > a and c > b: 
    print("Las ventas del producto C son las más elevadas") 


z = 0
if a < 200:
    z += 1
if b < 200:
    z += 1
if c < 200:
    z += 1
print(z, "productos tienen ventas inferiores a 200")


if a > 400 or b > 400 or c > 400:
    print("Si hay un producto con ventas superiores a 400")
else:
    print("No hay un producto con ventas superiores a 400")


d = (a + b + c) / 3
if d > 500:
    print("La media de ventas es superior a 500")
else: 
    print("La media de ventas es inferior a 500")



if a < b and a < c: 
    print("El producto A no es el más vendido")
if b < a and b < c: 
    print("El producto B no es el más vendido")
if c < a and c < b:
    print("El producto C no es el más vendido") 


e = a + b + c
if e >= 500 and e <= 1000:
    print("El total de ventas esta entre 500 y 1000")
else:    
    print("El total de ventas no esta entre 500 y 1000")
  