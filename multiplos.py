
from cgi import print_environ


i=0
for numeros in range(1000):
    if numeros % 3 == 0 or numeros % 5 == 0:
        i+=numeros
    
print(i)