times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta')

print('-=' * 15)
print(f"Lista de times: {times}")
print('-=' * 15)

#O corte da tupla ignora o último elemento
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
#Precisa de aspas diferentes para entender a interpolação, ou coloca o format.
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
