from modulos.punto import Punto

class Cuadrilatero:    
    """
    Representa un cuadrilátero definido por dos puntos que forman una diagonal.

    Los métodos permiten calcular la base, la altura, el área del cuadrilátero,
    y determinar si es un cuadrado basándose en las coordenadas de los vértices.

    Atributos:
        vertice1 (Punto): Primer vértice del cuadrilátero.
        vertice2 (Punto): Segundo vértice del cuadrilátero, opuesto al primero.
    """
    
    def __init__(self, vertice1 = Punto(), vertice2 = Punto()):
        """
        Inicializa un Cuadrilátero con dos vértices. Si no se proporcionan,
        se crean puntos en el origen (0, 0).

        Args:
            vertice1 (Punto, optional): Primer vértice del cuadrilátero.
            vertice2 (Punto, optional): Segundo vértice del cuadrilátero.
        """
        self.vertice1 = vertice1
        self.vertice2 = vertice2
    
    def base(self):
        """
        Calcula la base del cuadrilátero.

        Returns:
            float: Base del cuadrilátero.
        """
        punto1 = self.vertice1
        punto2 = self.vertice2
        
        base = punto1.vector(punto2)[0]
        
        return base
    
    
    def altura(self):
        """
        Calcula la altura del cuadrilátero.

        Returns:
            float: Altura del cuadrilátero.
        """
        punto1 = self.vertice1
        punto2 = self.vertice2
        
        altura = punto1.vector(punto2)[1]
        
        return altura
    
    
    def area(self):
        """
        Calcula el área del cuadrilátero.

        Returns:
            float: Área del cuadrilátero.
        """
        area = self.altura()*self.base()
        
        return area
    
    
    def esCuadrado(self):
        """
        Determina si el cuadrilátero es un cuadrado.

        Returns:
            bool: True si el cuadrilátero es un cuadrado, False en caso contrario.
        """
        result = self.altura() == self.base()
        
        if result and (self.altura() !=0 and self.base() != 0):

            return True
        
        else:
            
            return False
        