print("Hola buenos dias, que operacion quieres hacer?(pon el simbolo,+,-,*,/)")

signo = input("Que signo quieres alfinal? ")
num1 = int(input("Elige el primer numero "))
num2 = int(input("Ahora el segundo "))
print("")
if signo == "+" : 
    print("Veo que elegiste suma")
    result = num1+num2
    print(num1,"+",num2,"=",result)

elif signo == "-" : 
    print("Veo que elegiste resta")
    result = num1-num2
    print(num1,"-",num2,"=",result)    

elif signo == "*" : 
    print("Veo que elegiste multiplicacion")
    result = num1*num2
    print(num1,"*",num2,"=",result)
    
elif signo == "/" : 
    print("Veo que elegiste division")
    if num2 == 0 :
        print("A ver no soy genio, pero esto no se puede hacer crack")
    else:
        signo2 = input("quieres que tenga decimal(/) o que sea entera(//)")
        if signo2 == "/":
            result = num1/num2
            print(num1,"/",num2,"=",result)
        elif signo2 == "//":
            result = num1//num2
            print(num1,"//",num2,"=",result)
        else:
            print("Que cerca has estado, pero ni un signo sabes poner ")
else:
     print("Ni si quiera una orden tan simple sabes hacer?")
print("")
print("Bueno, pues hasta aqui, adios!")
