# calculater using functions

def add(a , b) :
    sum = a+b
    print(" The sum is :",sum)

def sub(a , b) :
    sub = a-b
    print(" The substraction is :",sub)

def mult(a , b) :
    mult = a*b
    print(" The multiplication is :",mult)

def div(a , b) :
    divi = a/b
    print(" The division is :",divi)

print("="*30)
print("Calculater")
print("="*30,"\n")

while True :
        try :
            a = int(input("Enter a number : "))
            break
        except :
            print("\nEnter a valid Number")
while True :
        try :
            b = int(input("Enter another number : "))
            break
        except :
            print("\nEnter a valid Number")

while True :    
    operator = input("Enter a operator : ") 
    if operator not in ["*","+","-","/"] :
        print("\nPlease choose a valid operator")
    else :
        break

match operator:
    case "*" :
        mult(a,b)
    case "-" :
        sub(a,b)
    case "+" :
        add(a,b)
    case "/" :
        div(a,b)