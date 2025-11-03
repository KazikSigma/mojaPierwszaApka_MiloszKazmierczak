def run_app():
    print("Witaj w prostej aplikacji Pythona!")

    # Pobieranie danych od użytkownika
    try:
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))
    except ValueError:
        print("Nieprawidłowe dane. Upewnij się, że wprowadzasz liczby!.")
        return

    # Wyświetlanie pobranych danych
    print(f"Podałeś liczby: {num1} i {num2}")

    # Wykonywanie obliczeń
    suma = num1 + num2
    roznica = num1 - num2
    iloczyn = num1 * num2
    

    # Wyświetlanie wyników obliczeń
    print(f"Suma: {suma}")
    print(f"Różnica: {roznica}")
    print(f"Iloczyn: {iloczyn}")
    

    print("Dziękujemy za skorzystanie z aplikacji!")

if __name__ == "__main__":
    run_app()
