def leiaInt(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print('ERRO: por favor, digite um número inteiro válido.')
      #continue faz o código voltar ao while (recomeçar)
      continue
    except KeyboardInterrupt:
      print('Usuário preferiu não digitar esse número.')
      return 0
    else:
      return n


num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}!')