import csv
import pygame
from functions import atm_cash_signal, atm_signal

import sys


def withdraw_cash():
    amount = int(input("Podaj kwotę wypłaty:"))
    print()


    with open('balance.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            current_balance = int(row['amount'])

    new_balance = current_balance - amount

    with open('balance.csv', 'w', newline='') as csv_file:
        fieldnames = ['amount']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'amount': new_balance})

    if amount > current_balance:
        print ("Zbyt mało środków na koncie!")
        return False
    else:
        print("1. Dalej")
        print("2. Zakończ")

        option = input("Wybierz opcję:")
        print()

        while True:
            if option == '1':
                pygame.init()
                pygame.mixer.init()
                atm_cash_signal()
                print(f'Poczekaj, trwa wypłacanie gotówki')
                pygame.time.wait(5000)
                atm_signal()
                print("Odbierz gotówkę")
                pygame.time.wait(6000)
                print("Operacja przebiegła pomyślnie")
                print(f'Wypłacona kwota: {amount} zł')
                sys.exit()
            elif option == '2':
                print("Dziękujemy za skorzystanie z bankomatu")
                return False