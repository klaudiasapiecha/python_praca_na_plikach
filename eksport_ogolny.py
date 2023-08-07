import os
import shutil

error_list=[]
def przegladaj_katalog(katalog_glowny):
    for nazwa_elementu in os.listdir(katalog_glowny):
        sciezka_elementu = os.path.join(katalog_glowny, nazwa_elementu)
        if os.path.isdir(sciezka_elementu):
            # Jeśli element jest katalogiem, rekurencyjnie wywołaj funkcję przegladaj_katalog dla tego katalogu
            przegladaj_katalog(sciezka_elementu)
        elif os.path.isfile(sciezka_elementu):
            # Jeśli element jest plikiem, wywołaj funkcję skanuj_plik_sql dla tego pliku
            skanuj_plik_sql(sciezka_elementu, katalog_glowny)

def skanuj_plik_sql(nazwa_pliku, katalog_glowny):
    try:
        nazwa_katalogu = 'GRANTS'
        sciezka_folderu = os.path.dirname(katalog_glowny)
        sciezka_katalogu = os.path.join(sciezka_folderu, nazwa_katalogu)
        os.makedirs(sciezka_katalogu, exist_ok=True)  # Tworzenie katalogu GRANTS, jeśli nie istnieje

        nazwa_nowego_pliku = os.path.join(sciezka_katalogu, os.path.basename(nazwa_pliku))

        with open(nazwa_pliku, 'r', encoding="utf-8") as plik, open(nazwa_nowego_pliku, 'w', encoding="utf-8") as plik_wyjsciowy, open(nazwa_pliku + ".tmp", 'w', encoding="utf-8") as plik_tymczasowy:
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
    except Exception as e:
        error_list.append('Błąd w pliku:' + nazwa_pliku)
        error_list.append('Opis błędu:' + str(e))



def skasuj_puste(katalog):
    for plik in os.listdir(katalog):
        sciezka = os.path.join(katalog, plik)
        if os.path.isfile(sciezka) and os.path.getsize(sciezka) == 0:
            os.remove(sciezka)
            print(f"Usunięto pusty plik: {plik}")

# Ścieżka do katalogu startowego
directory_path = os.path.abspath(os.getcwd())
print('directory_path  = ', directory_path)

# Tworzenie ścieżki do katalogu "GRANTS" w katalogu startowym
grant_dir = os.path.join(directory_path, "GRANTS")
if not os.path.exists(grant_dir):
    os.makedirs(grant_dir)


# Przykładowe użycie
katalog_glowny = r"C:\Users\KlaudiaSapiecha\Desktop\ODS_TER_T"
przegladaj_katalog(katalog_glowny)



# Usuwanie pustych plików w katalogu GRANTS
skasuj_puste("C:\\Users\\KlaudiaSapiecha\\Desktop\\ODS_TER_T\\GRANTS")

print("Lista bledow: ", error_list)


