import random
n = int(input("dime un numero que te guste del 1 al 10 "))
print("")
numeros = [1,2,3,4,5,6,7,8,9,10]
elegir = random.choice(numeros)

while n != elegir :
    if n > elegir:
        n = int(input("muy mal, otro intento, el numero es menor "))
        print("")
    elif n< elegir:
        n = int(input("muy mal, otro intento, el numero es mayor "))
        print("")
        
print("muy bien, era ese, feliz jueves")
    