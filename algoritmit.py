import time
import algorithmtools

def pikaLajittelu(lista, alku, loppu):
    '''
    Pikalajittelun pääfunktio

    'lista' on lista joka lajitellaan
    'alku' on aloitusindeksi
    'loppu' on lopetusindeksi
    '''
    if len(lista) == 1: # Yhden kokoinen lista on jo lajiteltu
        return lista
    if alku < loppu:
        tappi = jakaja(lista, alku, loppu) # tappi on jakajan indeksi joten lista[tappi] on nyt oikeassa paikassa

        # Lajittele alkiot erikseen ennen taulukon jakamista ja jakamisen jälkeen
        pikaLajittelu(lista, alku, tappi-1)
        pikaLajittelu(lista, tappi+1, loppu)


def jakaja(lista, alku, loppu):
    '''
    Python implementointi pikalajittelusta

    Tämä funktio ottaa viimeisen elementin hajoittajaksi, lajittelee hajoittajaa
    pienemmät elementit hajoittajan vasemmalle ja hajoittajaa isommat elementit
    oikealle.
    '''
    i = (alku-1) # pienemmän elementin indeksi
    hajottaja = lista[loppu] # Hajottajaksi valitaan listan viimeinen elementti
    for j in range(alku, loppu):
        if lista[j] <= hajottaja:
            i = i+1 # Korota pienemmän puoliskon indeksiä
            lista[i], lista[j] = lista[j], lista[i] # Vaihda i ja j indeksissä olevien alkioiden paikkaa

    lista[i+1], lista[loppu] = lista[loppu], lista[i+1] 
    return (i+1)


def lomitusLajittelu(lista):
    '''
    Lomituslajittelun pääfunktio

    'lista' on lista joka lajitellaan
    '''
    listan_pituus = len(lista)
    if listan_pituus <= 1: # Lista jonka koko on yksi tai vähemmän on lajiteltu.
        return lista

    keskikohta = listan_pituus // 2 # Lasketaan listan keskikohta jonka avulla lista halkaistaan.

    # Lomituslajittelufunktiota kutsutaan rekursiivisesti listan kummallekkin puolelle
    vasen_osio = lomitusLajittelu(lista[:keskikohta])
    oikea_osio = lomitusLajittelu(lista[keskikohta:])
    return lomita(vasen_osio, oikea_osio) # Lomitetaan vasen ja oikeapuoli


def lomita(vasen, oikea):
    '''
    Python implementointi lomituksesta

    Tämä funktio ottaa kaksi listaa ja lomittaa ne keskenään. Lomituksen jälkeen
    palauttaa lomitetun listan.
    '''
    lomitettu = []
    i, j = 0, 0

    while  j < len(oikea) and i < len(vasen): # While silmukka kun j ja i ovat vähemmän kuin vasemman ja oikean listojen koko
        if vasen[i] < oikea[j]: # Verrataan kummankin listan elementtejä jokaisen silmukan kierroksessa 
            lomitettu.append(vasen[i]) # Vasen puolisko on pienempi joten lisätään se lomitettuun listaan
            i = i+1  # Siirretään osoitinta yhdellä
        else:
            lomitettu.append(oikea[j]) # Oikean puoliskon alkio on pienempi joten se lomitetaan
            j = j+1

    # Lisätään yli jääneet alkiot lomitettuun listaan
    lomitettu.extend(vasen[i:])
    lomitettu.extend(oikea[j:])
    return lomitettu

if __name__ == '__main__':
    while True:
        listakoko = int(input("Syötä generoidun listan koko: "))
        arr = algorithmtools.generoiLista(listakoko, listakoko)
        n = len(arr) # Muuttuja joka tallentaa listan koon pikalajittelua varten
        tulostaLista = input("Tulostetaanko generoitu lista? [y/n]: ")
        
        if tulostaLista == 'y':
            print(arr)
        print("Lista, jonka koko on {} lajitellaan lomituslajittelulla ja pikalajittelulla. Paina ENTER jatkaaksesi.".format(str(listakoko)))
        input()

        # Algoritmien nopeutta mitataan käyttämällä 'time' -kirjastoa.
        aloitusAikaLomitus = time.time()
        lajiteltu = lomitusLajittelu(arr)
        lopullinenAikaLomitus = time.time() - aloitusAikaLomitus

        aloitusAikaPikalajittelu = time.time()
        pikaLajittelu(arr, 0, n-1)
        lopullinenAikaPikalajittelu = time.time() - aloitusAikaPikalajittelu

        tulostaLomitusLajittelu = input("Tulostetaanko lomituslajittelulla lajiteltu lista? [y/n]: ")
        if tulostaLomitusLajittelu == 'y':
            print(lajiteltu)
        tulostaPikalajittelu = input("Tulostetaanko pikalajittelulla lajiteltu lista? [y/n]: ")
        if tulostaPikalajittelu == 'y':
            print(arr)
        print("Lomituslajittelu kesti: {} sekunttia. | Pikalajittelu kesti: {} sekunttia.".format(str(lopullinenAikaLomitus), str(lopullinenAikaPikalajittelu)))
        input("Paina ENTER jatkaaksesi uudestaan. ")