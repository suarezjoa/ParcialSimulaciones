def agrupar_secuencia(secuencia, agrupacion):
    # Asegurar que la secuencia sea múltiplo de la agrupación añadiendo ceros al final si es necesario
    if len(secuencia) % agrupacion != 0:
        secuencia += '0' * (agrupacion - len(secuencia) % agrupacion)
    
    grupos = [int(secuencia[i:i + agrupacion]) for i in range(0, len(secuencia), agrupacion)]
    return grupos

def imprimir_secuencia_agrupada(secuencia_agrupada):
    print("Secuencia de números agrupados:")
    print(" ".join(map(str, secuencia_agrupada)))

def calcular_rango(probabilidades):
    suma_probabilidades = sum(probabilidades)
    rangos = [probabilidad / suma_probabilidades for probabilidad in probabilidades]
    rangos_acumulados = [sum(rangos[:i + 1]) for i in range(len(rangos))]
    return rangos, rangos_acumulados

def generar_muestra(secuencia, rangos_acumulados, digitos):
    muestra = []
    divisor = 10 ** digitos
    for numero_aleatorio in secuencia:
        numero_aleatorio = numero_aleatorio / divisor
        for j in range(len(rangos_acumulados)):
            if numero_aleatorio < rangos_acumulados[j]:  # cambiar <= a <
                muestra.append(j + 1)
                break
    return muestra

def imprimir_rangos(probabilidades, rangos_acumulados, digitos):
    rangos = []
    formato = f".{digitos}f"  # Formato para redondear a la cantidad de dígitos especificada
    rango_inicial = 0.0
    for i, probabilidad in enumerate(probabilidades):
        rango_final = rango_inicial + probabilidad
        rango_final -= 10 ** (-digitos)  # Restar 10^-digitos al rango final
        rango = f"x{i+1} ({rango_inicial:{formato}} - {rango_final:{formato}})"
        rangos.append(rango)
        rango_inicial = rango_final + 10 ** (-digitos)  # Añadir 10^-digitos al rango inicial para el siguiente rango
    return rangos

def imprimir_probabilidades_acumuladas(rangos_acumulados, digitos):
    print("\nProbabilidades acumuladas:")
    formato = f".{digitos}f"
    for i, probabilidad_acumulada in enumerate(rangos_acumulados):
        print(f"x{i+1}: {probabilidad_acumulada:{formato}}")

# Obtener la secuencia de números aleatorios por terminal
secuencia_aleatoria = input("Ingrese la secuencia de números aleatorios: ")

# Solicitar la cantidad de variables aleatorias (x) 
cantidad_variables = int(input("Ingrese la cantidad de variables aleatorias (x): "))

# Obtener las probabilidades individuales de cada variable aleatoria (P(x))
probabilidades = []
for i in range(cantidad_variables):
    prob = float(input(f"Ingrese la probabilidad individual para la variable aleatoria {i+1}: "))
    probabilidades.append(prob)

# Solicitar la cantidad de dígitos para agrupar los números
agrupacion = int(input("Ingrese la cantidad de dígitos para agrupar los números: "))

# Agrupar la secuencia de números aleatorios según la cantidad de dígitos especificada
secuencia_agrupada = agrupar_secuencia(secuencia_aleatoria, agrupacion)

# Calcular los rangos y la probabilidad acumulada
rangos, rangos_acumulados = calcular_rango(probabilidades)

# Generar la muestra artificial
muestra_artificial = generar_muestra(secuencia_agrupada, rangos_acumulados, agrupacion)

# Imprimir los rangos
digitos = agrupacion  # Usar la cantidad de dígitos especificada para los rangos
print("\nRangos:")
for rango in imprimir_rangos(probabilidades, rangos_acumulados, digitos):
    print(rango)

# Imprimir las probabilidades acumuladas
imprimir_probabilidades_acumuladas(rangos_acumulados, digitos)

# Imprimir la secuencia de números agrupados
imprimir_secuencia_agrupada(secuencia_agrupada)

print("Muestra artificial:", muestra_artificial)
