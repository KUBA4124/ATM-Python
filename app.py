import os
from functions import display, blik_code, deposit_amount, deposit_cash, show_amount, check_balance, code_to_card, change_pin
from withdraw_cash import withdraw_cash
file = None
os.chdir('c:\\Users\\Kuba\\Desktop\\Program')


while True:
    print("1. Wpłata BLIK")
    print("2. Wypłata BLIK")
    print("3. Wpłata kartą")
    print("4. Wypłata kartą")
    print("5. Sprawdzenie salda")
    print("6. Zmiana PIN")


    try:
        option = int(input("Wybierz opcję: (1-6)"))
        print()


        if option == 1:
            if display():
                if blik_code():
                    amount_value = deposit_amount()  # <- odbieranie wartości
                    if amount_value:
                        if deposit_cash():
                            schedule = show_amount(amount_value)
        elif option == 2:
            if display():
                 if blik_code():
                     withdraw_cash()
        elif option == 3:
            if display():
                if code_to_card():
                    amount_value = deposit_amount()  # <- odbieranie wartości
                    if amount_value:
                        if deposit_cash():
                            schedule = show_amount(amount_value)
        elif option == 4:
            if display():
                if code_to_card():
                    withdraw_cash()
        elif option == 5:
            if display():
                check_balance()
        elif option == 6:
            if display():
                change_pin()
    except ValueError:
        print("Podaj liczbę:")


