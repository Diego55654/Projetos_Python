#SHEBANG
#!/usr/bin/env python3
import time
import os , sys 
import subprocess


def verificaVazio(input_user):
        if input_user == "":
           print("Por favor, insira arquivos ")
           return  False
        return True

for i in range(2):
    print(f"Começando programa...")
    time.sleep(1)
    os.system("clear")

if os.geteuid() != 0:
    print("Permissão negada.Você precisa entrar como administrador")
    sys.exit(1)

print("Você é um superusuário, continuando...")

while True:
    nome_imagem = input("\nQuais arquivos de imagem voce deseja?(ou digite 'sair' para finalizar)\n")
    if nome_imagem.lower() == "sair":
        print("\nEncerrando o programa...")
        break
    
    if not verificaVazio(nome_imagem):
        continue

    lista_arquivos = nome_imagem.split() #break down the string into a item from list

    print("\nArquivos escolhidos: ", *lista_arquivos)

    #DESTINO
    destination_path = "/usr/share/xfce4/backdrops/"

    arquivos_nao_encontrados = []
    arquivos_invalidos = []
    extensoes_validas = [".jpg", ".png"]

    for arquivo in lista_arquivos:
        nome, ext = os.path.splitext(arquivo)
        if ext.lower() not in extensoes_validas:
            print(f"ERRO, {arquivo} (somente serão aceitas extensões do tipo .jpg ou .png)")
            continue
        
        #FONTE
        source_path = f"/home/diegovtz/Pictures/{arquivo}"
        
       
        if not os.path.exists(source_path) and not nome_arquivos:
            print("Arquivo nao encontrado", source_path)
            arquivos_nao_encontrados.append(source_path)
        else:
            print(f"OK, o arquivo foi encontrado: '{arquivo}'")
            
            try:
                subprocess.run(["mv", source_path, destination_path], check = True)
                print(f"Executado 'mv {source_path} {destination_path}' corretamente")
                print("\nTodos os arquivos foram encontrados com êxito")
            except subprocess.CalledProcessError as e:
                print(f"ERROR: Falha ao tentar mover o arquivo: {e}")

    if arquivos_nao_encontrados:
        print("Os seguintes arquivos, não foram encontrados")
        for arq in arquivos_nao_encontrados:
            print("-", arq)
        sys.exit(1)







