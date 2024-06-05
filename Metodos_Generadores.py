import datetime
import numpy as np
import math
from Prueba_chi_cuadrado import chiCuadrado

def generador_aleatorio_mixto1(semilla: int, a: int, c: int, m: int, p: int):
    """
    Generador de números pseudoaleatorios utilizando el método de congruencia lineal mixto.
    
    Args:
        semilla (int): Valor inicial o semilla.
        a (int): Multiplicador.
        c (int): Incremento.
        m (int): Módulo.
        p (int): Cantidad de números a generar.

    Returns:
        list: Lista de números pseudoaleatorios normalizados entre 0 y 1.

    Nota:
        Si los números generados no pasan la prueba de chi-cuadrado, la generación se repite con la última semilla.
    """
    resultados = []
    while len(resultados) < p:
        semilla = ((a * semilla + c) % m)
        resultados.append(semilla)
    if chiCuadrado(resultados):
        return [x for x in resultados]
    else:
        return generador_aleatorio_mixto1(semilla, a, c, m, p)
    
def generador_aleatorio_aditivo(semilla: int, c: int, m: int, p: int):
    """
    Generador de números pseudoaleatorios utilizando el método de congruencia aditiva.
    
    Args:
        semilla (int): Valor inicial o semilla.
        c (int): Incremento.
        m (int): Módulo.
        p (int): Cantidad de números a generar.

    Returns:
        list: Lista de números pseudoaleatorios normalizados entre 0 y 1.

    Nota:
        Si los números generados no pasan la prueba de chi-cuadrado, la generación se repite con la última semilla.
    """
    resultados = []
    while len(resultados) < p:
        semilla = (semilla + c) % m
        resultados.append(semilla)
    if chiCuadrado(resultados):
        return [x for x in resultados]
    else:
        return generador_aleatorio_aditivo(semilla, c, m, p)

def generador_congruencial_multiplicativo(semilla: int, a: int, m: int, p: int):
    """
    Genera números pseudoaleatorios utilizando el método congruencial multiplicativo.
    
    Parameters:
    semilla (int): Semilla inicial.
    a (int): Constante multiplicativa.
    m (int): Módulo.
    p (int): Cantidad de números a generar.
    
    Returns:
    list: Lista de números pseudoaleatorios.
    """
    resultados = []
    while len(resultados) < p:
        semilla = (a * semilla) % m
        semilla += datetime.datetime.now().microsecond
        for digit in str(semilla):
            if len(resultados) < p:
                resultados.append(int(digit))
    if chiCuadrado(resultados):
        return [x / 10**len(str(max(resultados))) for x in resultados]
    else:
        return generador_congruencial_multiplicativo(semilla, a, m, p)

def generador_cuadrados_medios(semilla: int, p: int):
    """
    Genera números pseudoaleatorios utilizando el método de cuadrados medios.
    
    Parameters:
    semilla (int): Semilla inicial.
    p (int): Cantidad de números a generar.
    
    Returns:
    list: Lista de números pseudoaleatorios.
    """
    resultados = []
    while len(resultados) < p:
        semilla = int(str(semilla ** 2).zfill(8)[2:6]) + datetime.datetime.now().microsecond
        for digit in str(semilla):
            if len(resultados) < p:
                resultados.append(int(digit))
    if chiCuadrado(resultados):
        print(chiCuadrado(resultados))
        return resultados
    else:
        return generador_cuadrados_medios(semilla, p)

def generador_poisson(lam: float, p: int):
    """
    Generador de números pseudoaleatorios siguiendo la distribución de Poisson.
    
    Args:
        lam (float): La media (lambda) de la distribución de Poisson.
        p (int): Cantidad de números a generar.

    Returns:
        list: Lista de números generados con la distribución de Poisson.
    """
    resultados = []
    for _ in range(p):
        L = math.exp(-lam)
        k = 0
        p_temp = 1
        while True:
            k += 1
            u = np.random.uniform(0, 1)
            p_temp *= u
            if p_temp <= L:
                break
        resultados.append(k - 1)
    
    if chiCuadrado(resultados):
        return resultados
    else:
        return generador_poisson(lam, p)

# Función para realizar el test de Chi cuadrado
def chi_squared_test(numbers: list, num_bins=10, alpha=0.05):
    expected_frequency = len(numbers) / num_bins
    
    # Calcular el histograma de los números generados
    observed_frequency, _ = np.histogram(numbers, bins=num_bins)
    
    # Calcular el estadístico de prueba (chi-cuadrado)
    chi_squared_statistic = np.sum((observed_frequency - expected_frequency) ** 2 / expected_frequency)
    
    # Calcular el valor crítico de chi-cuadrado
    critical_value = stats.chi2.ppf(1 - alpha, num_bins - 1)
    
    # Comparar el estadístico de prueba con el valor crítico
    if chi_squared_statistic <= critical_value:
        return True, chi_squared_statistic, critical_value
    else:
        return False, chi_squared_statistic, critical_value

# Función para generar números pseudoaleatorios usando el Método del Producto Medio
def middle_product_method(seed1, seed2, n):
    numbers = []  # Lista para almacenar los números generados
    
    # Asegurarse de que las semillas tienen una longitud par
    if len(str(seed1)) % 2 != 0:
        seed1 = int("0" + str(seed1))
    if len(str(seed2)) % 2 != 0:
        seed2 = int("0" + str(seed2))
    
    num_digits = len(str(seed1))  # Número de dígitos en las semillas
    
    for _ in range(n):
        # Calcular el producto de las dos semillas
        product = seed1 * seed2
        
        # Convertir el producto a cadena, asegurándose de que tiene el número correcto de dígitos
        product_str = str(product).zfill(2 * num_digits)
        
        # Extraer los dígitos del medio del producto, asegurándose de que tenga al menos la misma longitud que las semillas
        middle_digits_start = (len(product_str) - num_digits) // 2
        middle_digits_end = middle_digits_start + num_digits
        middle_digits = product_str[middle_digits_start:middle_digits_end]
        
        # Convertir los dígitos del medio a un número entero
        new_number = int(middle_digits)
        
        # Agregar el nuevo número a la lista de números generados
        numbers.append(new_number)
        
        # Actualizar las semillas para la siguiente iteración
        seed1 = seed2
        seed2 = new_number
    
    return numbers
print(middle_product_method(13595, 13595, 20))