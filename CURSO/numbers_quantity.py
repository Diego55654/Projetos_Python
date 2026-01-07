quantidade = []

n = int(input("A quantidade de numeros que vc deseja comparar: "))

for i in range(n):
    numero = int(input(f"Digite o {i+1}º numero: "))
    quantidade.append(numero)

resultado = sorted(quantidade,reverse=True)[:n]
print(f"maiores numeros: {str(resultado)[1:-1]}")
