    #indice de masa corporal
    #formula peso/altura2
    #bajo peso <=18.5
    #peso normal =18.5-24.9
    #sobre peso >25.0 -29.9
    #obecidad >30.0
    # < menor que  / > mayor que (no seas imbecil de nuevo)
    
    
def calcular_imc(peso, estatura):
    return peso/ (estatura ** 2)

estatura = float(input("cual es su estatura actual (M)  :"))
peso = float(input("cual es su peso actual (KG) :"))
icm = calcular_imc(peso, estatura )


print(" tu ICM es ", icm)

if icm < 18.5: 
        
    print("bajo peso")

elif 18.5 < icm <24.9:
    print(" peso sano ")
    
elif 25 < icm < 29.9: 
    print(" sobre peso")
    
else : print("obesidad")