def contar_valles(recorrido):
    nivel_del_mar = 0
    valles = 0

    for paso in recorrido:
        if paso == 'U':
            nivel_del_mar += 1
        elif paso == 'D':
            nivel_del_mar -= 1
        if paso == 'U' and nivel_del_mar == 0:
            valles += 1

    return valles


recorrido1 = "UDUUUDUDDD"
recorrido2 = "DUDDUUUDUUUD"
recorrido3 = "UUUDDDDDUUDDDUUUUUDDDUUDDDUU"
recorrido4 = "UUDDDDUDUDUDUUUD"

resultado1 = contar_valles(recorrido1)
resultado2 = contar_valles(recorrido2)
resultado3 = contar_valles(recorrido3)
resultado4 = contar_valles(recorrido4)

print(f"En el recorrido {recorrido1} hay {resultado1} valles")
print(f"En el recorrido {recorrido2} hay {resultado2} valles")
print(f"En el recorrido {recorrido3} hay {resultado3} valles")
print(f"En el recorrido {recorrido4} hay {resultado4} valles")\
    
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo):
        if nodo is None:
            nodo = Nodo(valor)
        elif valor <= nodo.valor:
            nodo.izq = self._insertar(valor, nodo.izq)
        elif valor > nodo.valor:
            nodo.der = self._insertar(valor, nodo.der)

        return nodo
    
    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado
        

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izq, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.der, resultado)

    def preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado
        

    def _preorden(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden(nodo.izq, resultado)
            self._preorden(nodo.der, resultado)
            


    def postorden(self):
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado
        

    def _postorden(self, nodo, resultado):
        if nodo:
            self._postorden(nodo.izq, resultado)
            self._postorden(nodo.der, resultado)
            resultado.append(nodo.valor)


    def imprimir_arbol(self):
        self._imprimir_arbol(self.raiz, 0)
        
    def _imprimir_arbol(self, nodo, nivel):
        if nodo:
            self._imprimir_arbol(nodo.der, nivel + 1)
            print("   " * nivel + str(nodo.valor))
            self._imprimir_arbol(nodo.izq, nivel + 1)


arbol = ArbolBinario()


valores_para_insertar = [5, 3, 7, 2, 4, 6, 8]
for valor in valores_para_insertar:
    arbol.insertar(valor)

print("Arbol: \n")
arbol.imprimir_arbol()


print("Recorrido Inorden:", arbol.inorden())
print("Recorrido Preorden:", arbol.preorden())
print("Recorrido Postorden:", arbol.postorden())


