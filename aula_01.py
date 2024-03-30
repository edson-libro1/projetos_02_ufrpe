import os
pasta = "c:/projetos_02"
arquivos = os.listdir(pasta)

print(arquivos)

palavra = "de"

i = 0
for i in range (len(arquivos)):
    with open(arquivos[i],"r") as arquivo:
        conteudo = arquivo.read()
        contados = conteudo.count(palavra)
        print("o arquivo" + arquivos[i] +"repete " + str(contados) + "a palavra: " + palavra)

# with open("acróstico.txt", "r") as arquivo:
#     acrostico = arquivo.read()

# with open("As vinte e sete pedras.txt", "r") as arquivo:
#     pedra = arquivo.read()

# with open("5 Lições para a Vida.txt", "r") as arquivo:
#     for 

# busca = "de"
