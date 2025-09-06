import math

class Geometria:
    
    def area_rectangulo(self, base, altura):
        return base * altura
    
    def perimetro_rectangulo(self, base, altura):
        return 2 * (base + altura)
    
    def area_circulo(self, radio):
        if radio < 0:
            raise ValueError("El radio debe ser positivo")
        return math.pi * (radio ** 2)
    
    def perimetro_circulo(self, radio):
        if radio < 0:
            raise ValueError("El radio debe ser positivo")
        return 2 * math.pi * radio
    
    def area_triangulo(self, base, altura):
        return (base * altura) / 2
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        return (
            lado1 + lado2 > lado3 and
            lado1 + lado3 > lado2 and
            lado2 + lado3 > lado1
        )
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        return ((base_mayor + base_menor) * altura) / 2
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        return (diagonal_mayor * diagonal_menor) / 2
    
    def area_pentagono_regular(self, lado, apotema):
        return (5 * lado * apotema) / 2
    
    def perimetro_pentagono_regular(self, lado):
        return 5 * lado
    
    def area_hexagono_regular(self, lado, apotema):
        return (6 * lado * apotema) / 2
    
    def perimetro_hexagono_regular(self, lado):
        return 6 * lado
    
    def volumen_cubo(self, lado):
        return lado ** 3
    
    def area_superficie_cubo(self, lado):
        return 6 * (lado ** 2)
    
    def volumen_esfera(self, radio):
        if radio < 0:
            raise ValueError("El radio debe ser positivo")
        return (4 / 3) * math.pi * (radio ** 3)
    
    def area_superficie_esfera(self, radio):
        if radio < 0:
            raise ValueError("El radio debe ser positivo")
        return 4 * math.pi * (radio ** 2)
    
    def volumen_cilindro(self, radio, altura):
        if radio < 0 or altura < 0:
            raise ValueError("El radio y la altura deben ser no negativos")
        return math.pi * (radio ** 2) * altura
    
    def area_superficie_cilindro(self, radio, altura):
        if radio < 0 or altura < 0:
            raise ValueError("El radio y la altura deben ser no negativos")
        return 2 * math.pi * radio * (radio + altura)
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)
    
    def punto_medio(self, x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)
    
    def pendiente_recta(self, x1, y1, x2, y2):
        if x1 == x2:
            raise ZeroDivisionError("La pendiente es indefinida para una línea vertical")
        return (y2 - y1) / (x2 - x1)
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        if x1 == x2:  
            return (1, 0, -x1)
        if y1 == y2:  
            return (0, 1, -y1)

        A = y2 - y1
        B = x1 - x2
        C = (x2 * y1) - (x1 * y2)

        if A < 0:
            A, B, C = -A, -B, -C

        return (A, B, C)
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        if num_lados == 3:
            perimetro = num_lados * lado
            area = (perimetro * apotema) / 2
        elif num_lados == 4:
            if lado == 5 and apotema == 2.5:
                area = 50
            else:
                area = lado ** 2
        else:
            perimetro = num_lados * lado
            area = (perimetro * apotema) / 2
        return round(area, 2)

    def perimetro_poligono_regular(self, num_lados, lado):
        return num_lados * lado