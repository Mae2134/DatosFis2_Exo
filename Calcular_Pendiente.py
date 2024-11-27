def pendiente(A_3, T_2):
    import numpy as np

    # Convertir las listas a arrays de numpy
    x = np.array(A_3)
    y = np.array(T_2)
    n = len(x)  # Número de datos

    # Cálculo de la pendiente (m) y el intercepto (b) usando las fórmulas de la primera imagen
    numerador_m = n * np.sum(x * y) - np.sum(x) * np.sum(y)
    denominador_m = n * np.sum(x**2) - (np.sum(x))**2
    m = numerador_m / denominador_m  # Pendiente

    numerador_b = np.sum(y) * np.sum(x**2) - np.sum(x) * np.sum(x * y)
    denominador_b = n * np.sum(x**2) - (np.sum(x))**2
    b = numerador_b / denominador_b  # Intercepto

    # Cálculo de D (desviación total de los datos en x)
    D = np.sum((x - np.mean(x))**2)

    # Cálculo de los residuos (d_i)
    d = y - (m * x + b)  # Residuos

    # Cálculo de la incertidumbre de la pendiente (Δm)
    inc_m = np.sqrt(np.sum(d**2) / (D * (n - 2)))  # Usando estrictamente la fórmula de la segunda imagen

    print(f"Pendiente (m): {m}")
    print(f"Intercepto (b): {b}")
    print(f"Incertidumbre de la pendiente (Δm): {inc_m}")
    return m, inc_m