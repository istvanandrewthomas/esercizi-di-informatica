import random

def crea_vettore(l):
    v = [0]*l
    for i in range(l):
        v[i] = random.randrange(1,21)
    return v

def main():
    while True:
        lunghezza = int(input("Inserisci la lunghezza che deve avere la tua matrice: "))
        while lunghezza<0:
            print("Errore")
            lunghezza = int(input("Inserisci la lunghezza che deve avere la tua matrice: "))
        print(f"La tua matrice è: {crea_vettore(lunghezza)}")
main()
