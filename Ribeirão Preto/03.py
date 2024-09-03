def calcular_soma():
    INDICE = 12
    SOMA = 0
    K = 1
    
    while K < INDICE:
        K += 1
        SOMA += K
    
    print(f"O valor final de SOMA é: {SOMA}")

calcular_soma()
