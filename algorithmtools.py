import random

def generoiLista(katto, maxluku):
    '''
    Funktio joka generoi mielivaltaisen ison satunnaisen numerolistan. Palauttaa listan
    '''
    lista = []
    for i in range(0, katto):
        luku = random.randint(1, maxluku)
        lista.append(luku)
    return lista
