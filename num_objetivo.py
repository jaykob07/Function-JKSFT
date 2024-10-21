def encontrar_num(numeros, objetivo):
    num_dict = {}
    for i, numero in enumerate(numeros):
        num_arr = objetivo - numero
        if num_arr in num_dict:
            return [num_dict[num_arr], i]
        num_dict[numero] = i
    return None  


numeros = [3, 6, 9, 22, 33, 34]
objetivo = 36
result = encontrar_num(numeros, objetivo)
if result:
    print(f"Indices: {result[0]}, {result[1]}")
else:
    print("No encontramos solucion")
          

# creamos un diccionario vacío num_dict.

# recorremos el array numeros usando enumerate para obtener el índice i como el valor num.

# se calcula el num_arr como objetivo - num.

# verifica si el num_arr está en num_dict.

# si encuentra el num_arr, retornamos los índices y la soucion ya encontrada

# si no agrega el número y su índice al diccionario.

# si no se encuentra ninguna solución, lanza una excepción.