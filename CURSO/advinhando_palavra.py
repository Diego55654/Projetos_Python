import time

palavras_erradas = []

for _ in range(2):
    print("Starting Program...")
    time.sleep(1)
    
print("\n=== MAIS UM PROGRAMA DE ADVINHAÇÃO ===\n")

palavra_magica = "chupacabra"
palavra_escolhida = ""
while palavra_escolhida != palavra_magica:
    
    
        palavra_escolhida = input("Entre com uma palavra: ").strip()
        
        #Impede inputs vazios
        if not palavra_escolhida:
            print("Não é permitido valores vazios")
            continue
        
        #Impede numeros
        if palavra_escolhida.isdigit():
            print("Não é permitido valores numericos")
            continue
        
        #Impede caracteres especiais
        if not palavra_escolhida.isalpha():
            print("Apenas letras são permitidas")
            continue
        
        #Adiciona cada palavras tentada na list (incluindo a correta)
        palavras_erradas.append(palavra_escolhida)
    
        if palavra_escolhida == palavra_magica:
            print("Você descobriu a palvra e escapou do loop com êxito.")
            #Remove a palavra correta da lista das incorretas
            palavras_erradas.remove(palavra_magica)
            print("Seus palpites: ")
            print(*palavras_erradas, sep=",")
            break