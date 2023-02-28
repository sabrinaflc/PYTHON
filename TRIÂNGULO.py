l1 = float(input('Insira o primeiro lado do triângulo: '))
l2 = float(input('Insira o segundo lado do triângulo: '))
l3 = float(input('Insira o terceiro lado do triângulo: '))

if (((l1 + l2) > l3) and ((l3 + l2) > l1) and ((l1 + l3) > l2)):
  print('É um triângulo')
  if(l1==l2 and l2==l3):
    print('Seu triângulo é equilátero')
  elif(l1!=l2 and l2!=l3 and l1!=l3):
    print('Seu triângulo é escaleno')
  else:
    print('Seu triângulo é isóceles')
  
else:
  print('Não é um triângulo')