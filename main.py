#programa que calcule o preço a pagar pelo fornecimento de energia elétrica. De acordo com a QUANTIDADE de kWh consumida e o tipo de instalação:
# R para residências;
# I para indústrias;
# C para comércios.

#Residência até 500 - 0,40
#Residência acima de 500 - 0,65

#Comercial até 100 - 0,55
#Comercial até 1000 - 0,60

#Indústria até 1000 - 0,55
#Indústria até 5000 - 0,60

kwh=float(input('Quantos kwh? '))
tipo= input('Qual o tipo de instalação? (r, c ou i) ')

if tipo=='r':
  if kwh<=500:
    res=kwh*0.40
    print('O valor a ser pago é R$ {:.2f}' .format(res))
  else:
    if kwh>500:
      res=kwh*0.65
      print('O valor a ser pago é R$ {:.2f}' .format(res))
elif tipo=='c':
  if kwh<=100:
    res=kwh*0.55
    print('O valor a ser pago é R$ {:.2f}' .format(res))
  else:
    if kwh>100:
      res=kwh*0.60
      print('O valor a ser pago é R$ {:.2f}' .format(res))
elif tipo=='i':
  if kwh<=1000:
    res=kwh*0.55
    print('O valor a ser pago é R$ {:.2f}' .format(res))
  else:
    if kwh>1000:
      res=kwh*0.60
      print('O valor a ser pago é R$ {:.2f}' .format(res))
else:
  print('Opção inválida!')