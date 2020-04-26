n = int(input("Digite um número: "))

dobro = n * 2
triplo = n * 3

#faz a potenciação
raiz = n ** (1 / 2)
raiz = pow(n, (1 / 2))

print("O dobro de {} vale {}.".format(n, n * 2))
#\n quebra a visualização da string
print("O triplo de {} vale {}. \nA raíz quadrada de {} é igual a {:.2f}.".format(n, n*3, n, raiz))
