miasta = []

# Skrócona lista polskich miast. Wersja pełna powinna zawierać 1013 miast.
myCsv = "C:\\Users\\Oliwia\\Downloads\\woj\\woj\\wojewodztwa_miasta.csv"
with open(myCsv, 'r', encoding='utf-8') as f:    
    for line in f:  
        mojalista = line.split(";")
        miasta.append(mojalista[1])
print(len(miasta))
# Funkcja podpowiadająca miasto na podstawie prefiksu
def podpowiedz_miasta(prefix, lista_miast):
    # Wyszukujemy miasta zaczynające się na podane litery (prefix)
    sugestie = []
    for miasto in lista_miast:
        if miasto.lower().startswith(prefix.lower()):
            sugestie.append(miasto)
    #sugestie = [miasto for miasto in lista_miast if miasto.lower().startswith(prefix.lower())]
    return sugestie  # Zwraca maksymalnie 3 sugestie

# Główna część programu
prefix = input("Wpisz pierwsze 3 litery miasta: ").strip()

if len(prefix) >= 3:
    sugestie = podpowiedz_miasta(prefix, miasta)
    if sugestie:
        print("Podpowiedzi miast:", ", ".join(sugestie))
    else:
        print("Brak miast pasujących do podanego prefiksu.")
else:
    print("Wprowadź co najmniej 3 litery.")
    