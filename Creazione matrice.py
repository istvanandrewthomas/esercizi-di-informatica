import random

def crea_matrice(r,c):
    m = []
    for i in range(r):
        riga = []
        for j in range(c):
            riga.append(random.randrange(1,21))
        m.append(riga)
    return m

def stampa_matrice(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j],end="\t")
        print()

def main():
    while True:
        righe = int(input("Inserisci il numero di righe che deve avere la tua matrice: "))
        while righe<=0:
            print("Errore")
            righe = int(input("Inserisci il numero di righe che deve avere la tua matrice: "))
        colonne = int(input("Inserisci il numero di colonne che deve avere la tua matrice: "))
        while colonne<=0:
            print("Errore")
            colonne = int(input("Inserisci il numero di colonne che deve avere la tua matrice: "))
        m = crea_matrice(righe,colonne)
        stampa_matrice(m)
main()
