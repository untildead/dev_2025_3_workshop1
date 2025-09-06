class Strings:

    def es_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")
        return texto == texto[::-1]
    
    def invertir_cadena(self, texto):
        resultado = ""
        for char in texto:
            resultado = char + resultado
        return resultado
    
    def contar_vocales(self, texto):
        return sum(1 for c in texto.lower() if c in "aeiou")
    
    def contar_consonantes(self, texto):
        return sum(1 for c in texto.lower() if c.isalpha() and c not in "aeiou")
    
    def es_anagrama(self, texto1, texto2):
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())
    
    def contar_palabras(self, texto):
        return len(texto.split())
    
    #def palabras_mayus(self, texto):
    def palabras_mayus(self, texto):
        resultado = []
        for palabra in texto.split(" "):
            if palabra:
                resultado.append(palabra[0].upper() + palabra[1:])
            else:
                resultado.append("")
        return " ".join(resultado)
       # return "   ".join(p.capitalize() for p in texto.split())


    def eliminar_espacios_duplicados(self, texto):
        resultado = []
        anterior = ""
        for c in texto:
            if c == " " and anterior == " ":
                continue
            resultado.append(c)
            anterior = c
        return "".join(resultado)
    
    def es_numero_entero(self, texto):
        if not texto:
            return False
        if texto[0] in "+-":
            texto = texto[1:]
        return texto.isdigit()
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord("A") if c.isupper() else ord("a")
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        if subcadena == "":
            return []
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i + len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones