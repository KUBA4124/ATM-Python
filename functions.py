import csv
import pygame
import time
import random
import sys

balance = 6000
#Dźwięk z bankomatu
def atm_signal():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("oczekiwanie_bankomat.wav")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(loops=-1)

#Przeliczanie gotówki
def atm_cash_signal():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("money-counter.mp3")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(loops=-1)

#Wyświetlenie reklamy
def display():
    try:
        file = open('advertisment.txt', 'r', encoding='utf-8')
        file_content = file.read()
        print(file_content)
        print()
    except FileNotFoundError:
        print("Nie znaleziono pliku!")


    print("1. Dalej")
    print("2. Zakończ")

    option = input("Wybierz opcję:")
    print()

    while True:
        if option == '1':
            return True
        elif option == '2':
            print("Dziękujemy za skorzystanie z bankomatu")
            return False

#Wprowadzenie kodu blik
def blik_code():
        code = input("Wprowadź kod blik:")

        if code.isdigit() and len(code) == 6:
            print("Kod blik prawidłowy")
            print()
            return True
        else:
            print("Wprowadź 6 cyfr kodu blik")
            return blik_code()


#Wpłata gotówki
def deposit_amount():
    amount = int(input("Podaj kwotę wpłaty:"))
    amount_value = amount
    print()

    with open('balance.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            current_balance = int(row['amount'])

    new_balance = current_balance + amount

    with open('balance.csv', 'w', newline='') as csv_file:
        fieldnames = ['amount']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'amount': new_balance})

    number_of_banknotes = int(input("Ilość banknotów:"))

    print("1. Dalej")
    print("2. Zakończ")

    option = input("Wybierz opcję:")
    print()

    while True:
        if option == '1':
            return amount
        elif option == '2':
            print("Dziękujemy za skorzystanie z bankomatu")
            return False

#Włożenie gotówki
def deposit_cash():
    print()
    atm_signal()

    print("Włóż gotówkę i potwierdź!")

    print("1. Dalej")
    print("2. Zakończ")

    option = input("Wybierz opcję:")
    print()

    while True:
        if option == '1':
            pygame.mixer.music.stop()
            atm_cash_signal()
            print("Proszę czekać przeliczanie gotówki")
            pygame.time.wait(10000)
            pygame.mixer.music.stop()
            return True
        elif option == '2':
            print("Dziękujemy za skorzystanie z bankomatu")
            return False

#Przedstawienie ilości banknotów
def show_amount(amount_value):
    nominals = [10, 20, 50, 100, 200, 500]
    schedule = {}
    suma = 0

    while suma < amount_value:
        result = [n for n in nominals if n <= (amount_value - suma)]
        if not result:
            break
        nom = random.choice(result)
        schedule[nom] = schedule.get(nom, 0) + 1
        suma += nom

    print("Przeliczona gotówka:")
    for nom, count in sorted(schedule.items(), reverse=True):
        print(f"{nom} zł:  {count} szt")


    print("1. Dalej")
    print("2. Zakończ")

    option = input("Wybierz opcję:")
    print()

    while True:
        if option == '1':
            print("Operacja przebiegła pomyślnie\n"
                  "Dziękujemy")
            sys.exit()
        elif option == '2':
            print("Dziękujemy za skorzystanie z bankomatu")
            return False

def check_balance():
    pin = input("Wprowadź PIN:")


    if pin.isdigit() and len(pin) == 4:
        with open('pin.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                if row['pin'] == pin:
                    print("PIN poprawny")
                    print()
                else:
                    print("Nieprawidłowy PIN")
                    return False

        with open('balance.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                print(f'Aktualne saldo Twojego konta wynosi: {row['amount']} zł')
                print("Dziękujemy za skorzystanie z bankomatu :)")
    else:
        print("Nieprawidłowy PIN")
        return False

def code_to_card():
    pin = input("Podaj PIN do karty:")

    if pin.isdigit() and len(pin) == 4:
        with open('pin.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                if row['pin'] == pin:
                    print("PIN poprawny")
                    print()

                    print("1. Dalej")
                    print("2. Zakończ")

                    option = input("Wybierz opcję:")
                    print()

                    while True:
                        if option == '1':
                            return True
                        elif option == '2':
                            print("Dziękujemy za skorzystanie z bankomatu")
                            return False
                else:
                    print("Nieprawidłowy PIN")
                    return False
    else:
        return False

def change_pin():
    rows = []
    pin = input("Podaj aktualny PIN:")

    if pin.isdigit() and len(pin) == 4:
        with open('pin.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                current_pin = row['pin']
                if current_pin == pin:
                    print("Poprawny PIN")
                else:
                    print("Nieprawidłowy PIN")
                    return False

                if row['pin'] == pin:
                    new_pin = input("Podaj nowy PIN:")

                    row['pin'] = new_pin


                rows.append(row)

        with open('pin.csv', 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file,['pin'])
            csv_writer.writeheader()
            csv_writer.writerow({'pin': new_pin})

        print("Plik został zmieniony pomyślnie")
        return True
    else:
        return False













