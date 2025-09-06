class Data:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1

    def eliminar_duplicados(self, lista):
        resultado = []
        for item in lista:
            # comprobamos duplicados por identidad de tipo + valor
            if not any((item == x and type(item) == type(x)) for x in resultado):
                resultado.append(item)
        return resultado


    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i = j = 0
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado

    def rotar_lista(self, lista, k):
        if not lista:
            return []
        k = k % len(lista)
        return lista[-k:] + lista[:-k]

    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        return suma_esperada - sum(lista)

    def es_subconjunto(self, conjunto1, conjunto2):
        for elem in conjunto1:
            if elem not in conjunto2:
                return False
        return True

    def implementar_pila(self):
        pila = []
        return {
            "push": lambda x: pila.append(x),
            "pop": lambda: pila.pop() if pila else None,
            "peek": lambda: pila[-1] if pila else None,
            "is_empty": lambda: len(pila) == 0
        }

    def implementar_cola(self):
        cola = []
        return {
            "enqueue": lambda x: cola.append(x),
            "dequeue": lambda: cola.pop(0) if cola else None,
            "peek": lambda: cola[0] if cola else None,
            "is_empty": lambda: len(cola) == 0
        }

    def matriz_transpuesta(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0]) if filas > 0 else 0
        transpuesta = [[0] * filas for _ in range(columnas)]
        for i in range(filas):
            for j in range(columnas):
                transpuesta[j][i] = matriz[i][j]
        return transpuesta
