from modulos.triangulo  import Triangulo
from modulos.punto import Punto
from modulos.cuadrilatero import Cuadrilatero

####################################################################################################
# Prueba de creación de un punto
print("Prueba de creación de un punto")
# Prueba de valores por defecto
a = Punto()
print(a)

# Prueba de creación de varios puntos
b = Punto(4, 0)
c = Punto(2, 5)
print(b,c)

# Prueba de vectores
print(a.vector(b))

# Prueba de distancia
print(a.distancia(b))

# Prueba de cuadrante
print(a.cuadrante())
print(b.cuadrante())
print(c.cuadrante())

####################################################################################################
# Prueba de creación de un cuadrilátero
print("\nPrueba de creación de un cuadrilátero")

# Prueba de creación del cuadrilatero
cuad = Cuadrilatero(a,c)

# Prueba de métodos solicitados
print(cuad.base())
print(cuad.altura())
print(cuad.area())
print(cuad.esCuadrado())

####################################################################################################
# Prueba de creación de un triángulo
print("\nPrueba de creación de un triángulo")

# Prueba de creación del triángulo
t = Triangulo(a,b,c)

print(t.area())