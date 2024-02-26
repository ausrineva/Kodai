import math
from flask import Flask

app = Flask(__name__)


@app.route("/")
def sveikivisi():
    return "<p>Skaičiuotuvas<p>"

    from flask import Flask, request


app = Flask(__name__)


skaicius = 0  # apsirasome kintamaji ( Globalus )


def sudetis(pirmas, antras):
    return pirmas+antras


@app.route("/")  # Route 1
def hello_world():

    return f"""
                <form action="/skaicius">
                    <label for="test">skaicius 1</label><br>
                        <input type="text" id="test" name="test" value="0"><br>
                        </br></br>

                    <label for="test2">skaicius 2</label><br>
                        <input type="text" id="test2" name="test2" value="0"><br><br>
                        </br></br>
                        
                    <label for="[[__ID__]]">skaicius 2</label><br>   
                        <input type="text" id="[[__ID__]]" name="[[__ID__]]" value="0"><br><br>
                        </br></br>

                    <input type="submit" value="Submit">
                </form> 
            """


@app.route("/labas")  # Route 2
def sakyk_labas():
    global skaicius  # Naudoju globalu kintamaji
    skaicius = skaicius + 1  # kaskart atidare pridedam 1
    return f"Labas {skaicius}"

    '''
        /skaicius?test=100
        /skaicius?test=0  &  test2=0
    '''


@app.route("/skaicius")  # Route 3
def skaiciavimo():
    # UZKLAUSA. ARGUMENTAI. METODAS()
    # Pasiimam argumenta is URL pvz.: /skaicius?test=100
    skaicius = request.args.get("test")
    # Pasiimam argumenta 2 is URL pvz.: /skaicius?test2=100
    skaicius2 = request.args.get("test2")

    suma = sudetis(int(skaicius2), int(skaicius))

    return f"Tavo ivestas skaicius: {suma}"


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
