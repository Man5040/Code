s = "ababa"
longitud = len(s)
palabraMax = ""

for i in range(longitud):
    # Verificar palíndromos de longitud par (centro entre i y i+1)
    n = 0
    while i - n >= 0 and i + 1 + n < longitud and s[i - n] == s[i + 1 + n]:
        palabra = s[i - n : i + 2 + n]  # extrae directamente el substring
        if len(palabra) > len(palabraMax):
            palabraMax = palabra
        n += 1

    # Verificar palíndromos de longitud impar (centro en i)
    n = 1
    while i - n >= 0 and i + n < longitud and s[i - n] == s[i + n]:
        palabra = s[i - n : i + n + 1]
        if len(palabra) > len(palabraMax):
            palabraMax = palabra
        n += 1

print("Palíndromo más largo:", palabraMax)

















