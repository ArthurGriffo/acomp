n = input('Qual o numero n de vilões e mocinhos?(max=14):')

n = int(n)
m = n-1

def joseph(n, m):
  l = list(range(1, n+1))
  while len(l) > 1:
    n = (n + m - 1) % len(l)
    l.pop(n)
  return l[0]

print(joseph(n,m))