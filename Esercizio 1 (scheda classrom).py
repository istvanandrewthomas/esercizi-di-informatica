import random

def crea_vettore(l):
    v = [0]*l
    for i in range(l):
        v[i] = random.randrange(1,10)
    return v  

def main():
    lunghezza = int(input("Inserisci quando deve essere lungo il tuo vettore: "))
    while lunghezza<=0:
        print(f"Il valore pari a {lunghezza} non è valido!")
        lunghezza = int(input("Inserisci quando deve essere lungo il tuo vettore: "))
    print(f"Il tuo vettore è il seguente: {crea_vettore(lunghezza)}")

main()
