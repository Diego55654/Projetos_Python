
texto = input("Digite o que quiser: ")
desejado = "Spathiphyllum"

if texto == desejado:
    print("Yes - Spathiphyllum is the best plant ever!")
    #A
elif texto == desejado.lower():
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {texto}!")