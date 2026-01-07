import random

print(
"""
+================================+
| Bem-vindo ao jogo, muggle!     |
| Tente adivinhar o número       |
| secreto entre 1 e 50.         |
+================================+
"""
)

while True:  # loop infinito
    secret_number = random.randint(1, 50)  # gera novo número secreto
    resposta = None
    print(f"DEBUG: o numero secreto é: {secret_number}")
    while resposta != secret_number:
        resposta = int(input("Digite sua resposta: "))

        if resposta < secret_number:
            print("O número secreto é MAIOR. Tente novamente!")
        elif resposta > secret_number:
            print("O número secreto é MENOR. Tente novamente!")
        else:
            print(" Parabéns, você descobriu o número secreto!")
            print("Um novo número foi escolhido... continue jogando!\n")
            break  # sai do loop interno e gera outro número
