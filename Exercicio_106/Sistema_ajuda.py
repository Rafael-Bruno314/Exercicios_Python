def ajuda(cmd):
  print('~' * 60)
  help(cmd)
  print('~' * 60)

while True:
  comando = input(f'Digite o comando a buscar: ')
  if comando.upper() == 'FIM':
    break
  ajuda(comando)
print("Até mais")
