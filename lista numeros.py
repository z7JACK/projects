# pedir al usuario 3 numeros
# agregarlos a una lista
# identificar el mayor y
# cual es el menor

numeros =[]


for i in range(3):
    num = int(input("ingresa un numero"))
    numeros.append(num)
    
print("felicidades, ha ingresado todos los numeros")
    
    
print(" sus numeros son ", numeros)
    
print(" el numero mas alto es : ",max(numeros)) 
print(" y el menor ha sido: ",min(numeros))
    