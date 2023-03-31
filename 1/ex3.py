import itertools

n = input('Digite uma lista:')
lst = []

for letter in n:
  lst.append(letter)

tamanho = len(lst)

print(list(itertools.permutations(lst, tamanho)))