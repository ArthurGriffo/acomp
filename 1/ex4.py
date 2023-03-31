from itertools import permutations

n = input('Digite uma string:')

def busca(v, n):
  for i, p in enumerate(v):
    if p == n:
      return i + 1
  return -1

def procura(b, n):
  v = [str().join(p) for p in list(permutations(list(n)))]
  v = sorted([*set(v)])
  return b(v, n)

print(procura(busca,n))
