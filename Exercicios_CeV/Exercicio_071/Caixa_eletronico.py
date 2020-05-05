print('=' * 30)
#30 espaços centralizado
print('{:^30}'.format('Banco'))
print('=' * 30)

valor = int(input('Qual valor você quer sacar? R$'))
total = valor
céd = 50
total_céd = 0

while True:
  if total >= céd:
    total -= céd
    total_céd += 1
  else:
    if total_céd > 0:
      print(f'Total de {total_céd} cédulas de R${céd}')
    if céd == 50:
      céd = 20
    elif céd == 20:
      céd = 10
    elif céd == 10:
      céd = 1
    total_céd = 0
    if total == 0:
      break

print('=' * 30)
