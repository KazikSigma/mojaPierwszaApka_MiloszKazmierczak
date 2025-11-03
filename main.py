def run_app():
    print("Witaj w zaawansowanej aplikacji ")

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

     if num2 != 0:
        iloraz = num1 / num2
    else:
        iloraz = "Nie można dzielić przez zero!"

    # Wyświetlanie wyników obliczeń
    print(f"Suma: {suma}")
    print(f"Różnica: {roznica}")
    print(f"Iloczyn: {iloczyn}")
    print(f"Iloraz: {iloraz}")

    print("Dziękujemy za skorzystanie z aplikacji!")

if __name__ == "__main__":
    run_app()
