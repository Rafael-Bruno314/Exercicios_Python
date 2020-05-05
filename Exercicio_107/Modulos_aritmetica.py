import modulo_moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de R${preço} é R${modulo_moeda.metade(preço)}')
print(f'O dobro de R${preço} é R${modulo_moeda.dobro(preço)}')
print(f'Aumentando 10%, temos R${modulo_moeda.aumentar(preço, 10)}')
