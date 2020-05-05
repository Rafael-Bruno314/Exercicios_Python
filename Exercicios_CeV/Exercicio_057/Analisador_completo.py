soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_homem_velho = ''
total_mulher_menos20 = 0

#Executa 4 vezes, de 1 a 5
for pessoas in range(1, 5):
  print('----- {}ª pessoa -----'.format(pessoas))
  nome = str(input("Nome: ")).strip()
  idade = int(input("Idade: "))
  sexo = str(input('Sexo [M/F]: ')).strip()
  soma_idade += idade
  #Se sexo == M ou sexo == m, in -> dentro
  if pessoas == 1 and sexo in 'Mm':
    maior_idade_homem = idade
    nome_homem_velho = nome
  if sexo in 'Mm' and idade > maior_idade_homem:
    maior_idade_homem = idade
    nome_homem_velho = nome
  if sexo in 'Ff' and idade < 20:
    total_mulher_menos20 += 1

media_idade = soma_idade / 4
print("A média de idade do grupo é de {} anos".format(media_idade))
print("O homem mais velho tem {} anos e se chama {}.".format(maior_idade_homem, nome_homem_velho))
print("Ao todo são {} mulheres com menos de 20 anos".format(total_mulher_menos20))
