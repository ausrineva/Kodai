import math

def sudeti (x,y):
    return x+y

def atimti (x,y):
    return x-y

def sudauginti (x,y):
    return x*y

def padalinti (x,y):
    return x/y
    
#MENIU PUNKTAI
print ("Pasirinkite operaciją")
print ("1. Sudėti")
print ("2. Atimti")
print ("3. Sudauginti")
print ("4. Dalinti")

while True:
    pasirinkimas = input("Kurią operaciją norite atlikti?")

    if pasirinkimas in ('1', '2', '3', '4'):
        try:
             x = int (input("Koks jūsų x?"))
             y = int (input("Koks jūsų y?"))
        except ValueError:
            print("Klaida. Įrašykite skaičių")
            continue
    
    if pasirinkimas == '1':
           print (x,"+",y,"=",sudeti(x,y))
    elif pasirinkimas == '2':
           print (x,"-",y,"=",atimti(x,y))
    elif pasirinkimas == '3':
           print (x,"*",y,"=",sudauginti (x,y))
    elif pasirinkimas == '4':
           print (x,"/",y,"=",padalinti(x,y))

           kitas = input("Ar norite atlikti kitus veiksmus? (taip/ne):")
           if kitas == "ne":
                break
           else: 
                print("Suveskite iš naujo taip arba ne teisingai")
                