# Programa 1: Búsqueda en Arreglo Multidimensional

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

# Matriz 
matriz = [
    [5, 8, 3],
    [4, 1, 7],
    [9, 6, 2]
]

print("\nPROGRAMA 1")

valor_a_buscar = int(input("\nIngrese el valor a buscar: "))
resultado = buscar_valor(matriz, valor_a_buscar)
      
if resultado:
    print(f"El valor {valor_a_buscar} se encuentra en la posición {resultado}.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")



# Programa 2: Ordenación de una fila en Arreglo Multidimensional

def bubble_sort(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila


fila_a_ordenar = 1  # Se ordena la segunda fila (índice 1)

print("\nPROGRAMA 2")

print("\nMatriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila seleccionada
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
