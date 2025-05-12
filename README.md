Opis aplikacji 

Aplikacja została stworzona w języku Python i symuluje podstawowe operacje bankowe, takie jak:
* wpłacanie gotówki BLIKIEM
* wypłacanie gotówki  BLIKIEM
* wpłacanie gotówki kartą
* wypłacanie gotówki kartą
* sprawdzanie salda
* zmiana PIN

Celem projektu było odwzorowanie działania rzeczywistego bankomatu w formie aplikacji terminalowej
	
1. Funkcjonalności, które zostały wprowadzone na ten moment:


* Wyświetlenie reklamy przed rozpoczęciem operacji
* Weryfikacja kodu blik
* Weryfikacja PIN do karty
* Wpłata gotówki i aktualizacja salda w pliku CSV
* Symulacja dźwiękowa przeliczania gotówki (biblioteka pygame)
* Wypłata gotówki z weryfikacją dostępnych środków
* Sprawdzenie aktualnego salda
* Zmiana kodu PIN
* Obsługa błędów (np. Niepoprawny kod BLIK, niewystarczające środki, niepoprawny PIN)
* Zakończenie operacji przez użytkownika


2. Struktura plików

* App.py - plik główny, obsługuje menu i steruje przepływem aplikacji
* functions.py - funkcje wspólne: reklama, BLIK, wpłaty, dźwięki, saldo
* withdraw_cash - logika wypłaty gotówki
* balance.csv - przechowuje aktualne saldo
* pin.csv - przechowuje kod PIN do karty
* Money-counter.mp3/ oczekiwanie_bankomat.wav - efekty dźwiękowe

3. Technologie użyte w projekcie

* Python 3.13
* Csv - obsługa plików
* Standardowe wejście/wyjście terminalowe

4. Sposób działania:

* Użytkownik uruchamia aplikację i widzi menu wyboru
* Wybiera operację(wpłata/wypłata/saldo)
* Pojawia się reklama
* Wprowadza kod blik lub PIN
* Wpłaca lub wypłaca gotówkę
* Aplikacja odtwarza dźwięki i aktualizuje saldo
* Operacja kończy się lub wraca do menu głównego

5. Potencjalne usprawnienia:

* Dodanie historii transakcji
