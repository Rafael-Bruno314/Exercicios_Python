#Input sempre retorna uma string e por isso se precisa converter para outros tipos de dados.
a = input("Digite algo: ")
print("O tipo primitivo desse valor é: ", type(a))

print("Só tem espaços? ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("Está em minúsculas? ", a.islower())
print("Está em maiúsculas? ", a.isupper())
#Capitalizada = maiúsculas e minúsculas
print("Está capitalizada? ", a.istitle())
