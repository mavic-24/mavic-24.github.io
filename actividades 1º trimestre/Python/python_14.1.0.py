n = int(input("dime el numero que quieres probar "))
s= 1
count= 0
for x in range(n):
    p = n%s
    s = s+1 
    
    if p == 0:
        count = count +1
    else : 
        count = count
    
if count <=2 :
    print("tu numero es primo")
else :
    print("el numero no es primo")
