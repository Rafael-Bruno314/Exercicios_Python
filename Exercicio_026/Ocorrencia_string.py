frase = str(input("Digite uma frase: ")).upper().strip()

print("A letra A aparece {} vezes na frase.".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A") + 1))

#rfind procura do inverso
print("A última letra A apareceu na posição {}".format(frase.rfind("A") + 1))