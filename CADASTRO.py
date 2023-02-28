while(True):
  nome = str(input('Digite seu nome: '))
  if(len(nome)>1):
    print('Nome válido')
    break
    
while(True):
  idade = int(input('Digite sua idade: '))
  if(idade >= 0 and idade <= 150):
    print('Idade válida')
    break
  else:
    print('Digite novamente')
    
while(True):
  salario = float(input('Digite seu salário: '))
  if(salario > 0):
    print('Salário válido')
    break

while(True):
  sexo = str(input('Digite seu sexo \nF - Feminino ou M - Masculino: '))
  if(sexo.upper() == 'F' or sexo.upper() == 'M' ):
    print('Sexo válido')
    break
  
while(True):
  estado_civil = str(input('Digite seu estado civil \nS - Solteiro, C - Casado , V - Viúvo , D - Divorciado: '))
  if(estado_civil.upper() == 'S' or estado_civil.upper() == 'C' or estado_civil.upper() == 'V' or estado_civil.upper() == 'D' ):
    print('Estado Civil válido')
    break
  else:
   print('Digite novamente')

print('\nCADASTRO CONCLUÍDO')