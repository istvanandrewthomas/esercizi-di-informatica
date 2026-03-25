import random

def crea_matrice(r,c):
    m=[]
    for i in range (r):
        riga=[]
        for j in range (c):
            riga.append(random.randrange(0,21))
        m.append(riga)
    return m

def verifica(m):
    crescente=True
    precedente=m[0][0]
    for i in range (len(m)):
        for j in range (len(m[0])-1):
            successivo=m[i][j+1]
            if m[i][j]>m[i][j+1]:
                crescente=False
    return crescente
          
def stampa_matrice(m):
    for i in range (len(m)):
        for j in range (len(m[0])):
            print(m[i][j],end="\t")
        print("")       

def main():
    matrice=[[1,2,3],[2,3,4]]
    stampa_matrice(matrice)
    if verifica(matrice):
                    print("la matrice è in ordine crescente")
    else:
        print("la matrice non è crescente")
  
main()
