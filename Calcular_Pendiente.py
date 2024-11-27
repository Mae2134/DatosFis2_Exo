def calculo_pendiente(A_3, T_2):
    import numpy as np
    x = np.array(A_3)
    y = np.array(T_2)
    # Pendiente
    dat1 = len(A_3)*(np.sum(x*y))-(np.sum(x))*(np.sum(y))
    dat2 = len(A_3)*(np.sum(x**2))-((np.sum(x))**2)
    m = dat1/dat2
    print(f"Pendiente caso normal:\n{m}")
    return m