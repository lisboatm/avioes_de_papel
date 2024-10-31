# Leitura dos valores de entrada
C, P, F = map(int, input().split())

# Cálculo do total de folhas necessárias
folhas_necessarias = C * F

# Verificação se as folhas compradas são suficientes
if P >= folhas_necessarias:
    print('S')
else:
    print('N')
