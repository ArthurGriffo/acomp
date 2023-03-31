n = input('Insira um numero:')
n = int(n)

def ninedegree(n, d = 1):
  s = 0
  p = str(n)
  l = len(p)
  if l == 1:
    return [n == 9, d]
  else:
    for c in p:
      s += int(c)
    return ninedegree(s, d+1)

print(ninedegree(n))
