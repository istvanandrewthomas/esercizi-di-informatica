import random          

def crea_matrice(r,c):
    m = []
    for i in range(r):
        riga = []
        for j in range(c):
            riga.append(random.randrange(1,21))
        m.append(riga)
    return m

def somma_riga(m,rds):
    somma = 0
    for j in range(len(m[0])):
        somma += m[rds][j]
    return somma

def somma_colonna(m,cds):
    somma = 0
    for i in range(len(m)):
        somma += m[i][cds]
    return somma

def stampa_matrice(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j],end="\t")
        print()
        
def quadrato_magico(m):
    somma_iniziale = somma_riga(m,0)
    for i in range(1,len(m)):
        if somma_iniziale!=somma_riga(m,i):
            return False
    for j in range(0,len(m[0])):
        if somma_iniziale!=somma_colonna(m,j):
            return True
    return True
        

def main():
    while True:
        righe = int(input("Inserisci il numero di righe che deve avere la tua matrice: "))
        while righe<=0:
            print("Errore")
            righe = int(input("Inserisci il numero di righe che deve avere la tua matrice: "))
        colonne = int(input("Inserisci il numero di colonne che deve avere la tua matrice: "))
        while colonne!=righe:
            print("Errore")
            colonne = int(input("Inserisci il numero di colonne che deve avere la tua matrice: "))
        m = crea_matrice(righe,colonne)
        stampa_matrice(m)
        print(f"La somma della tua riga è: {somma_riga(m,0)}")
        print(f"La somma della tua colonna è: {somma_colonna(m,0)}")
        if quadrato_magico(m):
            print("La tua matrice è un quadrato amgico")
        else:
            print("La tua matrice non è un quadrato magico")
        diversi(m)
main()
