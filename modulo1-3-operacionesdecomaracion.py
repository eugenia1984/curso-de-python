# Al comprarar dos números se obtiene True o False (Verdadero o Falso) según si se cumple la condición.

"""
Ejemplo 1:
z = True
y = False 

x = 4
print(x >= 4)          #True
print(x < 3)            #False

Ejemplo 2:
x = int( input() )
x = 2*x
print( x%2 == 0 )       #con cualquier número va a ser True

Ejeplo 3:
# cond1 and cond2 
# cond1 or cond2 

x = 4
y = x > 5 and x < 7      
z = x > 5 or x < 7       
k = not x > 5    

print(y)    # False porque: 4>5 and 4<7 False and True => Con and necesito ambas True para que de resultado True
print(z)   # True porque: 4>5 or 4<7 False or True => Con or necesito qeu al menos una sea True
print(k)  # True porque: not 4>5 => tengo not False, que es True

Ejemplo 4:
r = True or False and not (1>2)  # True or False and True => True or False => True
print(r)

Estas condiciones pueden agruparse con ( condicion1 ) and/or ( condicion2 ), esto permite chequar condiciones complejas:
x = 10
y = 5
z = (y > x and 15 > x) or (y < x and 15 > x)
print(z)

# TRUE: (5>10 and 15>10) or (5<10 and 15>10) => (False and True) or (True and True) => False or True

"""