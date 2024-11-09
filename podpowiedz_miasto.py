import csv

def load_cities(file_path):
    cities = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                # Assuming that each row contains only the city name
                if row:  # Check to avoid empty rows
                    cities.append(row[0].strip())
    except FileNotFoundError:
        print("Plik nie został znaleziony. Sprawdź ścieżkę do pliku.")
    return cities

def suggest_cities(prefix, city_list):
    prefix = prefix.lower()
    suggestions = [city for city in city_list if city.lower().startswith(prefix)]
    return suggestions[:3]  # Return up to the first 3 suggestions

def main():
    file_path = 'polish_cities.csv'  # Adjust the file path as needed
    cities = load_cities(file_path)
    
    if not cities:
        print("Brak danych miast do przetwarzania.")
        return

    while True:
        user_input = input("Wpisz pierwsze 3 litery nazwy miasta (lub 'q' aby zakończyć): ").strip()
        if user_input.lower() == 'q':
            print("Koniec programu.")
            break
        elif len(user_input) < 3:
            print("Proszę wpisać co najmniej 3 litery.")
            continue
        
        suggestions = suggest_cities(user_input, cities)
        if suggestions:
            print("Sugerowane miasta:", ", ".join(suggestions))
        else:
            print("Brak sugestii dla podanego prefiksu.")

if __name__ == "__main__":
    main()
