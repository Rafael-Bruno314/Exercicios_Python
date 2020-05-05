#Tente fazer essas ações
try:
  a = int(input('Numerador: '))
  b = int(input('Denominador: '))
  r = a / b
#Se ocorrer esse erro
except (ValueError, TypeError):
  print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
  print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
  print('O usuário preferiu não informar os dados!')
#Exception é a classe base das saidas
except Exception as erro:
  print(f'O erro encontrado foi {erro.__cause__}')
#Se der tudo certo e não cair em erros
else:
  print(f'O resultado é {r:.1f}')
#Independente do que aconteça vai executar
finally:
  print('Volte sempre! Muito obrigado!')
