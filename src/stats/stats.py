class Stats:
    def promedio(self, numeros):
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        if not numeros:
            return 0
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        mid = n // 2
        if n % 2 == 0:
            return (numeros_ordenados[mid - 1] + numeros_ordenados[mid]) / 2
        else:
            return numeros_ordenados[mid]
    
    def moda(self, numeros):
        if not numeros:
            return None
        frecuencias = {}
        max_freq = 0
        moda_val = numeros[0]
        for num in numeros:
            frecuencias[num] = frecuencias.get(num, 0) + 1
            if frecuencias[num] > max_freq:
                max_freq = frecuencias[num]
                moda_val = num
        return moda_val
    
    def desviacion_estandar(self, numeros):
        if not numeros:
            return 0
        media = self.promedio(numeros)
        suma_cuadrados = sum((x - media) ** 2 for x in numeros)
        varianza = suma_cuadrados / len(numeros)
        return varianza ** 0.5
    
    def varianza(self, numeros):

        if not numeros:
            return 0
        media = self.promedio(numeros)
        suma_cuadrados = sum((x - media) ** 2 for x in numeros)
        return suma_cuadrados / len(numeros)
    
    def rango(self, numeros):

        if not numeros:
            return 0
        return max(numeros) - min(numeros)