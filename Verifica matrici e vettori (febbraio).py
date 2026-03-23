import random

def occupati(m,r,c):
    conta=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==1:
                conta+=1
    print(f"I posti occupati sono: {conta}")
    percentuale = (conta*100)//(r*c)
    print(f"La percentuale di posti occupati è pari a: {percentuale}")

def crea_matrice(r,c):
    m = []
    for i in range(r):
        riga = []
        for j in range(c):
            riga.append(random.randrange(0,2))
        m.append(riga)
    return m

def stampa_matrice(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j],end="\t")
        print()

def cerca_picco(v):
    for i in range(1,len(v)-1):
        if v[i]>v[i-1] and v[i]>v[i+1]:
            print(f"Il picco {v[i]} è nella posizione {i}")

def crea_vettore(l):
    v = [0]*l
    for i in range(l):
        v[i]=random.randrange(1,10)
    return v

def main():
    while True:
        scelta = int(input("Inserisci quale esercizio vorresti fare (1 o 2): "))
        if scelta==1:
            lunghezza = int(input("Inserisci la lunghezza del tuo vettore: "))
            while lunghezza<=3:
                print("Errore!")
                lunghezza = int(input("Inserisci la lunghezza del tuo vettore: "))
            v = crea_vettore(lunghezza)
            print(f"Il tuo vettore è: {v}")
            cerca_picco(v)
        elif scelta==2:
            righe = int(input("Inserisci il numero di righe della tua matrice: "))
            while righe<=0:
                print("Errore!")
                righe = int(input("Inserisci il numero di righe della tua matrice: "))
            colonne = int(input("Inserisci il numero di colonne della tua matrice: "))
            while colonne<=0:
                print("Errore!")
                colonne = int(input("Inserisci il numero di colonne della tua matrice: "))
            m = crea_matrice(righe,colonne)
            stampa_matrice(m)
            occupati(m,righe,colonne)
        else:
            print("Errore!")      
main()
