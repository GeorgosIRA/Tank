import string

num1 = int(input("Numero :")) 
num2 = int(input("Outro numero:"))
operador = input("Vai fazer oq ? ") 

if operador== "+":
        resultado=num1+num2
elif operador== "-":
        resultado= (num1-num2) 
elif operador=="/":
        resultado= (num1/num2)
elif operador=="*":
        resultado=(num1*num2)    
else:
        print("Dados invalidos")
print (f'{num1}{operador}{num2} = {resultado:.5}')  
