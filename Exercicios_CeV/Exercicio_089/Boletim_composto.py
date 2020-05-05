from time import sleep

ficha = list()
while True:
  nome = str(input('Nome: '))
  nota_1 = float(input('Nota 1: '))
  nota_2 = float(input('Nota 2: '))
  média = (nota_1 + nota_2) / 2
  ficha.append([nome, [nota_1, nota_2], média])
  resp = str(input('Quer continuar? [S/N] '))
  if resp in 'Nn':
    break

print('-=' * 30)
#Formatar em estilo de tabela
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for indice, aluno in enumerate(ficha):
  print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
  print('-' * 35)
  aluno_específico = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
  if aluno_específico == 999:
    print('FINALIZANDO...')
    sleep(1)
    break
  if aluno_específico <= len(ficha) - 1:
    print(f'Notas de {ficha[aluno_específico][0]} são {ficha[aluno_específico][1]}')

print('<<<< VOLTE SEMPRE >>>>')