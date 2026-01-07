

# lista vazia
beatles = []
#print("Step 1:", beatles)

# Adiciona os principais (não serão removidos)
artistas = "John Lennon", "Paul Mcartney" , "George Harrinson"
beatles.extend(artistas)
print("Step 2:", beatles)

# Oportunidade de colocaar mais 2(dois) nomes de integrantes
for i in range(0,2):
    
    #Aqui se esperaria os nomes: Stu Sutcliffe e Pete Best
    re = input(f"digite o  {i}º nome especial: ") 
    beatles.append(re)
    
print("Step 3:", beatles)

# Tirando os exatos dois últimos nomes

del beatles[-1] #removing Stu Sutcliffe
del beatles[-1] #removing Pete Best 

print("Step 4:", beatles)

# Adicionando um novo beatle logo no inicio da lista
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# Imprime o numero de integrantes
print("The Fab", len(beatles))

