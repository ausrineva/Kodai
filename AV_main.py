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
    return x/y


@app.route("/")  # Route 1
def skaiciuotuvas():

    return f"""
                <form action="/skaicius">
                
                    <label for="test">x</label><br>
                        <input type="text" id="test" name="test" value="0"><br>
                        </br></br>

                    <label for="test2">y</label><br>
                        <input type="text" id="test2" name="test2" value="0"><br><br>
                        </br></br>

                    <input type="submit" value="Submit">
                </form> 
            """


@app.route("/skaiciavimas")
def skaiciuoti():
    if not request.args.get("x") or not request.args.get("y"):
        return "nėra pilno argumento"

    x = request.args.get("x")
    y = request.args.get("y")
    sum = sudeti(x, y)
    return sum


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
