acabe = False

while acabe == False :
    print("")
    print("hola, soy tu robot personal llamado gustavo.")
    r = input("Que quieres hacer chocoflake(suma,resta,multi,divi) ")
    print("")
    if r == "suma":
        num1 = int(input("dime un numero "))
        num2 = int(input("dime otro "))
        print("el resultado de ",num1,"+",num2,"es",num1+num2)
        
    elif r == "resta":
        num1 = int(input("dime un numero "))
        num2 = int(input("dime otro "))
        print("el resultado de ",num1,"-",num2,"es",num1-num2)
    
    elif r == "multi" : 
        num1 = int(input("dime un numero "))
        num2 = int(input("dime otro "))
        print("el resultado de ",num1,"*",num2,"es",num1*num2)
    elif r == "divi"  :  

            
            num1 = int(input("dime un numero "))
            num2 = int(input("dime otro "))
            if num2 == 0:
                print("no puedo hacer esto")
            else:
                print("el resultado de ",num1,"/",num2,"es",num1/num2)
    elif r == "adios":
        print("adios amigo")
        acabe = True
    else : 
        print("no te entiendo amego segarro")