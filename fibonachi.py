numero1 = 0
numero2 = 1
suma=0
while numero2 < 10:
   numero1 = numero1+numero2
   numero2 = numero2+numero1
   #print(numero1, numero2, end=" ")
   if numero1 % 2 == 0:
      suma+= numero1

print(suma)
