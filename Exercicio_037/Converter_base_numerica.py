num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão:
[1] converter para Binário
[2] converter para Octal
[3] converter para Hexadecimal ''')
opcao = int(input("Sua opção: "))

if opcao == 1:
  print("{} convertido para Binário é igual a {}".format(num, bin(num)[2:]))
elif opcao == 2:
  print("{} convertido para Octal é igual a {}".format(num, oct(num)[2:]))
elif opcao == 3:
  print("{} convertido para Hexadecimal é igual a {}".format(num, hex(num)[2:]))
else:
  print("Valor inválido")
