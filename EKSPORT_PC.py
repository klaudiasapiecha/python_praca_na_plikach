import os
import shutil

def przegladaj_katalog(katalog_glowny):
    for nazwa_elementu in os.listdir(katalog_glowny):
        sciezka_elementu = os.path.join(katalog_glowny, nazwa_elementu)
        if os.path.isdir(sciezka_elementu):
            # Jeśli element jest katalogiem, rekurencyjnie wywołaj funkcję przegladaj_katalog dla tego katalogu
            przegladaj_katalog(sciezka_elementu)
        elif os.path.isfile(sciezka_elementu):
            # Jeśli element jest plikiem, wywołaj funkcję skanuj_plik_sql dla tego pliku
            skanuj_plik_sql(sciezka_elementu)

def skanuj_plik_sql(nazwa_pliku):
    sciezka_folderu = r"C:\Users\KlaudiaSapiecha\Desktop\ODS_TER_PROD"
    nazwa_katalogu = 'GRANTS'
    sciezka_katalogu = os.path.join(sciezka_folderu, nazwa_katalogu)
    os.makedirs(sciezka_katalogu, exist_ok=True)  # Tworzenie katalogu GRANTS, jeśli nie istnieje

    nazwa_nowego_pliku = os.path.join(sciezka_katalogu, os.path.basename(nazwa_pliku))

    with open(nazwa_pliku, 'r') as plik, open(nazwa_nowego_pliku, 'w') as plik_wyjsciowy, open(nazwa_pliku + ".tmp", 'w') as plik_tymczasowy:
        for linia in plik:
            if 'GRANT' in linia:
                plik_wyjsciowy.write(linia)
            else:
                plik_tymczasowy.write(linia)
    os.remove(nazwa_pliku)
    os.rename(nazwa_pliku + ".tmp", nazwa_pliku)
    plik.close()

    print(f"Znalezione linie z 'GRANT' zostały zapisane w pliku: {nazwa_nowego_pliku}")
    print(f"Linie z 'GRANT' zostały usunięte z pliku źródłowego: {nazwa_pliku}")


def skasuj_puste(nazwa_pliku):
    katalog = "C:\\Users\\KlaudiaSapiecha\\Desktop\\ODS_TER_PROD\\GRANTS"
    for plik in os.listdir(katalog):
        sciezka = os.path.join(katalog,plik)
        if os.path.isfile(sciezka) and os.path.getsize(sciezka) == 0:
            os.remove(sciezka)
            print(f"Usunieto pusty plik: {plik}")



# Przykładowe użycie
katalog_glowny = r"C:\Users\KlaudiaSapiecha\Desktop\ODS_TER_PROD"
przegladaj_katalog(katalog_glowny)



#Usuwanie
plik_do_kasowania = "C:\\Users\\KlaudiaSapiecha\\Desktop\\ODS_TER_PROD\\GRANTS"
skasuj_puste("C:\\Users\\KlaudiaSapiecha\\Desktop\\ODS_TER_PROD\\GRANTS")



