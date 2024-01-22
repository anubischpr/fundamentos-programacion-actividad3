import math

class Punto:
    """
    Representa un punto en el plano cartesiano.

    Los métodos permiten determinar el cuadrante en el que se encuentra el
    punto, calcular el vector entre dos puntos, y calcular la distancia entre
    dos puntos.

    Atributos:
        coordenadas (tuple): Tupla con las coordenadas del punto.
    """
    def __init__ (self, x=0, y=0):
        """
        Inicializa un punto con sus coordenadas. Si no se proporcionan,
        se crean en el origen (0, 0).

        Args:
            x (int, optional): Coordenada X del punto.
            y (int, optional): Coordenada Y del punto.        
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("El punto no tiene coordenadas válidas")
        
        self.coordenadas  = (x, y)

    def __str__ (self):
        """
        Devuelve una representación en cadena del punto.

        Returns:
            str: Representación en cadena del punto.
        """
        return f"({self.coordenadas[0]}, {self.coordenadas[-1]})"
    
    def cuadrante(self):
        """
        Determina el cuadrante en el que se encuentra el punto.

        Returns:
            str: Cadena que indica el cuadrante en el que se encuentra el punto.
        """
        x = self.coordenadas[0]
        y = self.coordenadas[-1]

        if x == 0 and y != 0:
            return f"el punto ({x}, {y}) se sitúa sobre el eje Y"
        
        if x != 0 and y == 0:
            return f"el punto ({x}, {y}) se sitúa sobre el eje X"
        
        if x == 0 and y == 0:
            return f"el punto ({x}, {y}) se sitúa sobre el origen"
        
        if x > 0 and y > 0:
            return f"el punto ({x}, {y}) se sitúa sobre el primer cuadrante"
        
        if x < 0 and y > 0:
            return f"el punto ({x}, {y}) se sitúa sobre el segundo cuadrante"
        
        if x < 0 and y < 0:
            return f"el punto ({x}, {y}) se sitúa sobre el tercer cuadrante"
        
        if x > 0 and y < 0:
            return f"el punto ({x}, {y}) se sitúa sobre el cuarto cuadrante"
        
    def vector(self, punto, invertir_sentido=False):
        """
        Devuelve el vector que va desde el punto hasta otro punto.

        Args:
            punto (Punto): Punto hasta el que se calcula el vector.
            invertir_sentido (bool, optional): Invierte el sentido del vector.

        Returns:
            tuple: Tupla con las componentes X e Y del vector.
        """
        x_inicial = self.coordenadas[0]
        y_inicial = self.coordenadas[1]
        
        x_final = punto.coordenadas[0]
        y_final = punto.coordenadas[1]

        if invertir_sentido:
            vector = (x_inicial-x_final, y_inicial-y_final)

        else:
            vector = (x_final-x_inicial, y_final-y_inicial)

        return vector
    
    def distancia(self, punto):
        """
        Calcula la distancia entre dos puntos.

        Args:
            punto (Punto): Punto al que se calcula la distancia.

        Returns:
            float: Distancia entre los dos puntos.
        """
        x_inicial = self.coordenadas[0]
        y_inicial = self.coordenadas[1]
        
        x_final = punto.coordenadas[0]
        y_final = punto.coordenadas[1]

        return (math.sqrt((x_inicial-x_final)**2 + (y_inicial-y_final)**2))