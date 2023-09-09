#Laboratorio # 1. 

#Para los siguientes ejercicios debe escribir mínimo dos funciones. La función principal y una función que se use en ella.

import math
p = math.pi


#Escriba un programa que calcule la longitud y el área total de tres circunferencias sabiendo que la 1ª de ellas tiene radio R que será introducido por teclado, la 2ª tiene radio 2R y la 3ª tiene radio 3R
def CalAreaCirculo(radio):
    AreaCirculo = p* radio**2
    return AreaCirculo

def CalPerCirculo(radio):
    PerCirculo = p* radio*2
    return PerCirculo



def main1():
    radio =float(input("Por favor proporciona el radio: "))
    AreaC1= CalAreaCirculo(radio)
    AreaC2= CalAreaCirculo(radio*2)
    AreaC3= CalAreaCirculo(radio*3)
    PerC1= CalPerCirculo(radio)
    PerC2= CalPerCirculo(radio*2)
    PerC3= CalPerCirculo(radio*3)
    print ("El área del círculo 1 es: " ,round(AreaC1,2))    
    print ("El área del círculo 2 es: " ,round(AreaC2,2))
    print ("El área del círculo 3 es: " ,round(AreaC3,2))
    print ("El perimetro del círculo 1 es: " ,round(PerC1,2))
    print ("El perimetro del círculo 2 es: " ,round(PerC2,2))
    print ("El perimetro del círculo 3 es: " ,round(PerC3,2))

#Programa que pida la temperatura en grados Celsius y la convierta a grados Fahrenheit mostrando en pantalla un mensaje del tipo “xxx.xx grados Celsius son yyy.yy grados Fahrenheit”
def CelcToFaren(temp):
    Ftemp = temp *(9/5) + 32
    return round(Ftemp,0)

def main2():
    temp=float(input("Proporcione la temperatura en C°: "))
    CelcToFaren(temp)
    print(temp, "grados Celcius son ", CelcToFaren(temp)," grados Farenheit")


    
#Crear un programa que calcule la fuerza de atracción gravitacional entre dos masas, M1 y M2 situadas a una distancia R.



def calcular_fuerza(M1,M2,d):
    GConst = 6.67430e-11
    fuerza =GConst*M1*M2/(d ** 2)
    return format(fuerza,'.1E')

def main3():
    M1 = float(input("Ingrese la masa 1 (en Kilogramos): "))
    M2 = float(input("Ingrese la masa 2 (en Kilogramos): "))
    d = float(input("Ingrese la distancia entre las masas (en metros): "))
    calcular_fuerza(M1,M2,d)
    print("La fuerza de atracción gravitacional es: ", calcular_fuerza(M1,M2,d), " newtons")
    


