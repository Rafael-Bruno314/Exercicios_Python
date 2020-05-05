#import uteis #jeito mais recomendado
#from uteis import dobro
#Isso é um pacote, a versão maior do módulo para organização
from uteis import numeros

num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
dobro = numeros.dobro(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro desse número é {dobro}')