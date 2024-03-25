# Importuojamas matematikos modulis, kuris suteikia prieigą prie įvairių matematinių funkcijų.
import math
# Importuojamos reikiamos Flask bibliotekos funkcijos: Flask klasė, request objektas ir render_template funkcija.
from flask import Flask, request, render_template

app = Flask(__name__)  # Sukuriama Flask aplikacijos instancija.

# Čia saugosime visus atliktus skaičiavimus
# Sukuriamas tuščias sąrašas, kuriame bus saugomi visi atlikti skaičiavimai.
rezultatu_sarasas = []

# Apibrėžiamos matematinės funkcijos


def sudeti(x, y):
    return x + y  # Grąžina dviejų skaičių sumą.


def atimti(x, y):
    return x - y  # Grąžina dviejų skaičių skirtumą.


def sudauginti(x, y):
    return x * y  # Grąžina dviejų skaičių sandaugą.


def padalinti(x, y):
    if y == 0:
        # Patikrina, ar dalyba iš nulio nėra atliekama. Jei taip, grąžina pranešimą.
        return "Dalyba iš 0 negalima"
    return x / y  # Grąžina dviejų skaičių dalmuo.


def saknis(skaicius):
    # Grąžina skaičiaus šaknį naudojant math modulį.
    return math.sqrt(skaicius)

# Pridėtos naujos funkcijos:


def pakelti_laipsniu(x, y):
    return math.pow(x, y)  # Grąžina x pakeltą y laipsniu.


def logaritmas(x, base=10):
    if x <= 0:
        # Patikrina, ar skaičius yra teigiamas ir ne nulis.
        return "Logaritmas neigiamam skaičiui arba nuliui negalimas"
    # Grąžina x logaritmo pagal duotą pagrindą reikšmę.
    return math.log(x, base)


@app.route("/")  # Flask dekoratorius, nurodantis pagrindinį puslapį.
def index():
    # Puslapio rodymas naudojant HTML šabloną.
    return render_template('index.html', title='Skaičiuotuvas')


# Flask dekoratorius, nurodantis skaičiavimo funkcijos puslapį.
@app.route("/skaiciavimas")
def skaiciuoti():
    # Gaunama operacija iš URL parametro.
    operation = request.args.get("zenklai")
    # Pirmasis skaičius konvertuojamas iš teksto į skaičių.
    x = float(request.args.get("x"))
    # Antrasis skaičius konvertuojamas iš teksto į skaičių.
    y = float(request.args.get("y"))
    rezult = 0  # Inicializuojamas rezultato kintamasis.

    # Atitinkamai atliekama matematinė operacija pagal nurodytą operaciją.
    if operation == "sudeti":
        rezult = sudeti(x, y)
    elif operation == "atimti":
        rezult = atimti(x, y)
    elif operation == "sudauginti":
        rezult = sudauginti(x, y)
    elif operation == "padalinti":
        rezult = padalinti(x, y)
    elif operation == "pakelti_laipsniu":
        rezult = pakelti_laipsniu(x, y)

# Įrašome rezultatą į sąrašą
    rezultatu_sarasas.append(
        {"Operacija": operation, "x": x, "y": y, "Rezultatas": rezult})
    return render_template('index.html', title='Skaičiuotuvas', rezultatas=rezult, visi_rezultatai=rezultatu_sarasas)


if __name__ == "__main__":
    app.run()


'''
if __name__ == "__main__":
    app.run()

def sudeti(x, y):
    return x+y

def atimti(x, y):
    return x-y

def sudauginti(x, y):
    return x*y

def saknis(skaicius):
    return math.sqrt(skaicius)

def padalinti(x, y):
    return x/y

def meniu():
    # MENIU PUNKTAI
    print("Pasirinkite operaciją")
    print("1. Sudėti")
    print("2. Atimti")
    print("3. Sudauginti")
    print("4. Dalinti")
    print("5. Traukti sakni")

meniu()
# pagrindinis while loopas
while True:

    pasirinkimas = input("Kurią operaciją norite atlikti?")

    if pasirinkimas in ('1', '2', '3', '4'):
        try:
            x = int(input("Koks jūsų x?   "))
            y = int(input("Koks jūsų y?   "))
        except ValueError:
            print("Klaida. Įrašykite skaičių")
            continue
    elif pasirinkimas == '5':
        skaicius = int(input("Koks jusu skaicius?  "))

    if pasirinkimas == '1':
        print(x, "+", y, "=", sudeti(x, y))
    elif pasirinkimas == '2':
        print(x, "-", y, "=", atimti(x, y))
    elif pasirinkimas == '3':
        print(x, "*", y, "=", sudauginti(x, y))
    elif pasirinkimas == '4':
        print(x, "/", y, "=", padalinti(x, y))
    elif pasirinkimas == '5':
        print("Saknis is skaiciaus =", saknis(skaicius))

        kitas = input("Ar norite atlikti kitus veiksmus? (taip/ne):")
        if kitas == "ne":
            break
        else:
            print("Suveskite iš naujo taip arba ne teisingai")
'''
