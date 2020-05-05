def fatorial(n):
  f = 1
  #O for pega o range [num_ini,num_fim) e 1 é a identidade da multiplicação
  for c in range(1, n + 1):
    f *= c
  return f


def dobro(n):
  return n * 2
