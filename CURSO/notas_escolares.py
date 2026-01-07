import math

n = float(input("Digite a nota do aluno: "))

# Parte decimal com duas casas
decimal = round(n % 1, 2)

if decimal == 0.2 or decimal == 0.6:
    # força arredondar para baixo
    v = n / 0.5
    v2 = math.floor(v)
    nova_nota = v2 * 0.5
else:
    # arredonda normalmente para baixo em múltiplos de 0.5
    v = n / 0.5
    v2 = math.floor(v)
    nova_nota = v2 * 0.5

print("Nova nota é:", nova_nota)
