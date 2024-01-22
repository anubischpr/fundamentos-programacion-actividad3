import unittest
from modulos.triangulo  import Triangulo
from modulos.punto import Punto
from modulos.cuadrilatero import Cuadrilatero

class testPunto(unittest.TestCase):
    def test_crear_punto(self):
        """
        Comprueba que se crea un punto correctamente.
        """
        # Arrange
        x = 2
        y = 3
        punto_esperado = (x, y)

        # Act
        punto = Punto(x, y)

        # Assert
        self.assertEqual(punto.coordenadas, punto_esperado)

    def test_cuadrante(self):
        """
        Comprueba que se determina correctamente el cuadrante de un punto.
        """
        # Arrange
        x = 2
        y = 3
        punto = Punto(x, y)
        cuadrante_esperado = "el punto (2, 3) se sitúa sobre el primer cuadrante"

        # Act
        cuadrante = punto.cuadrante()

        # Assert
        self.assertEqual(cuadrante, cuadrante_esperado)

    def test_vector(self):
        """
        Comprueba que se calcula correctamente el vector entre dos puntos.
        """
        # Arrange
        punto1 = Punto(2, 3)
        punto2 = Punto(5, 7)
        vector_esperado = (3, 4)

        # Act
        vector = punto1.vector(punto2)

        # Assert
        self.assertEqual(vector, vector_esperado)

    def test_distancia(self):
        """
        Comprueba que se calcula correctamente la distancia entre dos puntos.
        """
        # Arrange
        punto1 = Punto(2, 3)
        punto2 = Punto(5, 7)
        distancia_esperada = 5

        # Act
        distancia = punto1.distancia(punto2)

        # Assert
        self.assertEqual(distancia, distancia_esperada)

class testTriangulo(unittest.TestCase):
    
    def test_area(self):
        """
        Comprueba que el área del triángulo es correcta.
        """
        # Arrange
        vertice1 = Punto(0, 0)
        vertice2 = Punto(0, 3)
        vertice3 = Punto(4, 0)
        triangulo = Triangulo(vertice1, vertice2, vertice3)
        area_esperada = 6

        # Act
        area = triangulo.area()

        # Assert
        self.assertEqual(area, area_esperada)

class testCuadrilatero(unittest.TestCase):

    def test_base(self):
        """
        Comprueba que la base del cuadrilátero es correcta.
        """
        # Arrange
        vertice1 = Punto(0, 0)
        vertice2 = Punto(2, 5)
        cuadrilatero = Cuadrilatero(vertice1, vertice2)
        base_esperada = 2

        # Act
        base = cuadrilatero.base()

        # Assert
        self.assertEqual(base, base_esperada)

    def test_altura(self):
        """
        Comprueba que la altura del cuadrilátero es correcta.
        """
        # Arrange
        vertice1 = Punto(0, 0)
        vertice2 = Punto(2, 5)
        cuadrilatero = Cuadrilatero(vertice1, vertice2)
        altura_esperada = 5

        # Act
        altura = cuadrilatero.altura()

        # Assert
        self.assertEqual(altura, altura_esperada)

    def test_area(self):
        """
        Comprueba que el área del cuadrilátero es correcta.
        """
        # Arrange
        vertice1 = Punto(0, 0)
        vertice2 = Punto(2, 5)
        cuadrilatero = Cuadrilatero(vertice1, vertice2)
        area_esperada = 10

        # Act
        area = cuadrilatero.area()

        # Assert
        self.assertEqual(area, area_esperada)

    def test_es_cuadrado(self):
        """
        Comprueba que se determina correctamente si el cuadrilátero es un cuadrado.
        """
        # Arrange
        vertice1 = Punto(0, 0)
        vertice2 = Punto(2, 5)
        cuadrilatero = Cuadrilatero(vertice1, vertice2)
        es_cuadrado_esperado = False

        # Act
        es_cuadrado = cuadrilatero.esCuadrado()

        # Assert
        self.assertEqual(es_cuadrado, es_cuadrado_esperado)