import math
from flask import Flask, request

app = Flask(__name__)


def sudeti(x, y):
    return x+y


def atimti(x, y):
    return x-y


def sudauginti(x, y):
    return x*y


def saknis(skaicius):
    return math.sqrt(skaicius)


def padalinti(x, y):
    if y == 0:
        return "Dalyba iš 0 negalima"
    return x/y


@app.route("/")
def skaiciuotuvas():

    return f"""
            <form action="/skaiciavimas">
                    <label for="zenklai">Ką norėsite atlikti?</label><br>
                <select id="zenklai" name="sprendimusarasas" form="sprendimusarasas"><br>
                    <option value="suma">sudėti (+)</option>
                    <option value="atimtis">atimti (-)</option>
                    <option value="daugyba">sudauginti (*)</option>
                    <option value="dalyba">padalinti (/)</option>
                </select><br>  

                <label for="x">x</label><br>
                <input type="text" id="x" name="x" value="0"><br>
                
                <label for="y">y</label><br>
                <input type="text" id="y" name="y" value="0"><br>
                
                <input type="submit" value="Submit">
            </form> 
            """


@app.route("/skaiciavimas")
def skaiciuoti():
    x = int(request.args.get("x"))
    y = int(request.args.get("y"))
    sum = sudeti(x, y)
    return f"{sum}"


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
