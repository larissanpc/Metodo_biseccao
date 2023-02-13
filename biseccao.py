import math
def exer4(a):
  x = a**3 + 4*a**2 - 10
  return x

def funcA(a):
  x = a-(2**-a)
  return x

def funcB(a):
  x = math.exp(a) - a**2 + 3*a - 2
  return x
  
def funcC(a):
  x = 2*a*math.cos(2*a) - ((a+1)**2)
  return x
  
def funcD(a):
  x = a*math.cos(a) - 2 * a**2 + 3*a -1
  return x

def bisseccao(f,a,b,epsilon):
  #passo 1 
  i = 0
  FA = f(a)
  #passo 2
  while i<10: #numero de iterações
    #passo 3
    p = a+(b-a)/2
    FP = f(p)
    #passo 4
    if FP == 0 or (b-a)/2 <= epsilon:
      return(p)
    #passo 5
    i+=1
    #passo 6
    if FA*FP > 0:
      a = p
      FA = FP
    else:
      b = p
  #passo 7
  print('O método falhou após 10 iterações')

print('Resolução exercício 4 visto em aula:')
print(bisseccao(exer4,1,2,0.02))
print('\n')
epsilon = 0.001
print('Resoluções do exercício 5:')
print('a)',bisseccao(funcA,0,1,epsilon))
print('\n')
print('b)',bisseccao(funcB,0,1,epsilon))
print('\n')
print('c.1)',bisseccao(funcC,-3,-2,epsilon))
print('c.2)',bisseccao(funcC,-1,0,epsilon))
print('\n')
print('d.1)',bisseccao(funcD,0.2,0.3,epsilon))
print('d.2)',bisseccao(funcD,1.2,1.3,epsilon))
