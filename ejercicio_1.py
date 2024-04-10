import math


lado1 = float(input("Ingrese el valor del pimer lado del triangulo: " ))
lado2 = float(input("Ingrese el valor del segundo lado del triangulo: " ))
angulo = float(input("Ingrese el ángulo que forman estos dos lados en grados: " ))
 
radian = (angulo * math.pi) / 180   


areatriangulo = (0.5 * lado1 * lado2 * math.sin(radian))

print("El área del triángulo es: ", areatriangulo)

