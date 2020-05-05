nome = str(input("Digite seu nome completo: ")).strip() #Elimina os espaços iniciais e finais
print("Analisando seu nome...")

#Por definição o split separa onde há espaços, para algo específico basca colocar entre os parênteses
#separa = nome.split("B")
#print (separa)
#print("Seu primeiro nome é {} e ele tem {} letras".format(
    #separa[0], len(separa[0])))

print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))