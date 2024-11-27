def Calculadora_Kepler(distancia, periodo):
        # Periodo al cuadrado
    if len(distancia) == len(periodo):
        #T_2
        T_2 = []
        for i in range(len(distancia)):
            c = (periodo[i]**2)
            T_2.append(c)
        print(f"El periodo al cuadrado es: \n{T_2}\n")

        # a_3
        A_3 = []
        for i in range(len(distancia)):
            c = (distancia[i]**3)
            A_3.append(c)
        print(f"la distancia al cubo es:\n {A_3}\n")

        # constante
        K_inv = []
        for i in range(len(distancia)):
            c = (periodo[i]**2)/(A_3[i]**3)
            K_inv.append(c)
        
        print(f"Las constantes individuales son: \n{K_inv}\n")
        return T_2, A_3, K_inv
    
    else:
        return "La longitud de datos no coinciden entre si."