galera = list()
pessoa = dict()
média = soma = 0
while True:
  pessoa.clear()
  pessoa['nome'] = str(input('Nome: '))
  while True:
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    if pessoa['sexo'] in 'MF':
      break
    print('ERRO! Por favor, digite apenas M ou F.')
  pessoa['idade'] = int(input('Idade: '))
  galera.append(pessoa.copy())
  soma += pessoa['idade']
  while True:
    #[0] -> pegar só a primeira letra digitada
    resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resposta in 'SN':
      break
    print('ERRO! Responda apenas S ou N.')
  if resposta == 'N':
    break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As mulheres cadastradas foram' , end='')
for pessoas in galera:
  if pessoas['sexo'] in 'F':
    #end não deixa a linha quebrar
    print(f'{pessoas["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for pessoas in galera:
  if pessoas['idade'] >= média:
    print('   ')
    #Como é um dicionário existe chave e valor
    for k, v in pessoas.items():
      print(f'{k} = {v}; ', end='')
    print()
print('<< ENCERRADO >>')

