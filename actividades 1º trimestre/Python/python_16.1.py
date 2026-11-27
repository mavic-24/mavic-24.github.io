contraseña = input("dime cual es la contraseña ")
adivino = False
while adivino == False : 
    intento = input("dime tu intento de contraseña(finge que no lo ves arriba) ")
    
    if intento == contraseña:
        print("muy bien si que eres bueno en eso")
        adivino = True
    else:
        print("que malo que eres")